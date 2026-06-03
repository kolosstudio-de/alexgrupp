/**
 * Oleksandr Halushka i18n — Language Switcher v6
 * Clean, reliable, no edge-case bugs.
 */

const LANGS = [
    { code: 'de', label: 'DE' },
    { code: 'en', label: 'EN' },
    { code: 'uk', label: 'UK' },
    { code: 'ru', label: 'RU' },
];

// Resolve path to /locales/ regardless of page depth
const BASE_PATH = (function () {
    const parts = window.location.pathname.split('/').filter(Boolean);
    // Remove the filename (last part)
    const dirParts = parts.slice(0, -1);
    const depth = dirParts.length;
    return depth > 0 ? '../'.repeat(depth) + 'locales/' : 'locales/';
})();

// In-memory cache — load each file only once per page visit
const _cache = {};

function getLang() {
    const stored = localStorage.getItem('ag-lang');
    return (stored && LANGS.find(l => l.code === stored)) ? stored : 'de';
}

async function fetchLocale(lang) {
    if (_cache[lang]) return _cache[lang];
    
    const cachedData = localStorage.getItem('ag-i18n-' + lang);
    if (cachedData) {
        try {
            const parsed = JSON.parse(cachedData);
            _cache[lang] = parsed;
            fetch(BASE_PATH + lang + '.json')
                .then(res => res.json())
                .then(data => localStorage.setItem('ag-i18n-' + lang, JSON.stringify(data)))
                .catch(e => console.error(e));
            return parsed;
        } catch(e) {}
    }

    try {
        const res = await fetch(BASE_PATH + lang + '.json');
        if (!res.ok) throw new Error('HTTP ' + res.status);
        const data = await res.json();
        _cache[lang] = data;
        localStorage.setItem('ag-i18n-' + lang, JSON.stringify(data));
        return data;
    } catch (err) {
        console.error('[i18n] Cannot load ' + lang + '.json:', err.message, '| BASE_PATH:', BASE_PATH);
        return null;
    }
}

function applyTranslations(strings) {
    if (!strings) return;

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (strings[key] !== undefined) {
            el.textContent = strings[key];
        }
    });

    document.querySelectorAll('[data-i18n-html]').forEach(el => {
        const key = el.getAttribute('data-i18n-html');
        if (strings[key] !== undefined) {
            el.innerHTML = strings[key];
        }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (strings[key] !== undefined) {
            el.setAttribute('placeholder', strings[key]);
        }
    });

    document.documentElement.lang = getLang();
}

function updateSwitcherUI(activeLang) {
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === activeLang);
    });
}

function buildSwitcherButtons(container) {
    if (!container) return;
    container.innerHTML = '';
    const current = getLang();
    LANGS.forEach(({ code, label }) => {
        const btn = document.createElement('button');
        btn.className = 'lang-btn' + (code === current ? ' active' : '');
        btn.textContent = label;
        btn.dataset.lang = code;
        btn.setAttribute('aria-label', 'Language: ' + label);
        container.appendChild(btn);
    });
}

function renderSwitchers() {
    document.querySelectorAll('#langSwitcher, .langSwitcher-clone').forEach(buildSwitcherButtons);
}

// Single delegated listener — catches ALL .lang-btn clicks anywhere on page
document.addEventListener('click', async function (e) {
    const btn = e.target.closest('.lang-btn[data-lang]');
    if (!btn) return;

    const code = btn.dataset.lang;
    const current = getLang();

    // Always re-apply even if same lang (useful for page refresh scenarios)
    localStorage.setItem('ag-lang', code);

    const strings = await fetchLocale(code);
    if (strings) {
        applyTranslations(strings);
        updateSwitcherUI(code);
        console.log('[i18n] Switched to:', code, '| Keys applied:', Object.keys(strings).length);
    }
});

// On page load: render switchers, apply stored language
document.addEventListener('DOMContentLoaded', async function () {
    renderSwitchers();
    const lang = getLang();
    const strings = await fetchLocale(lang);
    applyTranslations(strings);
    updateSwitcherUI(lang);
    console.log('[i18n] Page loaded with lang:', lang, '| BASE_PATH:', BASE_PATH);
});
