/**
 * AlexGruppe i18n — Language Switcher
 * 
 * Loads a JSON locale file and replaces all [data-i18n] attribute values.
 * Language is stored in localStorage. Defaults to 'de'.
 * 
 * Usage: just include this script on every page. It runs on DOMContentLoaded.
 */

const LANGS = [
    { code: 'de', flag: '🇩🇪', label: 'DE' },
    { code: 'en', flag: '🇬🇧', label: 'EN' },
    { code: 'uk', flag: '🇺🇦', label: 'UK' },
    { code: 'ru', flag: '🇷🇺', label: 'RU' },
];

const BASE_PATH = (function () {
    // Resolve the correct path to /locales/ regardless of page depth
    const depth = window.location.pathname.replace(/\/[^/]*$/, '').split('/').filter(Boolean).length;
    return depth > 0 ? '../'.repeat(depth) + 'locales/' : 'locales/';
})();

let currentLang = localStorage.getItem('ag-lang') || 'de';

async function loadLocale(lang) {
    try {
        const res = await fetch(BASE_PATH + lang + '.json');
        if (!res.ok) throw new Error('Locale not found: ' + lang);
        return await res.json();
    } catch (e) {
        console.warn('[i18n] Note: Translations may not load properly when viewing via file:// protocol due to CORS.', e.message);
        try {
            const res = await fetch(BASE_PATH + 'de.json');
            return await res.json();
        } catch (e2) {
            console.error('[i18n] Safe fallback triggered for local viewing.');
            return {}; // Prevent unhandled promise rejection
        }
    }
}

function applyLocale(strings) {
    // Plain text content
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (strings[key] !== undefined) {
            el.textContent = strings[key];
        }
    });
    // Placeholder attribute (input / textarea)
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (strings[key] !== undefined) {
            el.setAttribute('placeholder', strings[key]);
        }
    });
    // innerHTML — for strings that contain inline HTML like <strong>
    document.querySelectorAll('[data-i18n-html]').forEach(el => {
        const key = el.getAttribute('data-i18n-html');
        if (strings[key] !== undefined) {
            el.innerHTML = strings[key];
        }
    });
    document.documentElement.lang = currentLang;
}

function renderSwitcher() {
    const container = document.getElementById('langSwitcher');
    if (!container) return;

    container.innerHTML = '';

    LANGS.forEach(({ code, flag, label }) => {
        const btn = document.createElement('button');
        btn.className = 'lang-btn' + (code === currentLang ? ' active' : '');
        btn.textContent = label;
        btn.title = flag + ' ' + label;
        btn.setAttribute('aria-label', 'Sprache wechseln zu ' + label);
        btn.addEventListener('click', async () => {
            if (code === currentLang) return;
            currentLang = code;
            localStorage.setItem('ag-lang', code);
            const strings = await loadLocale(code);
            applyLocale(strings);
            renderSwitcher(); // re-render to update active state
        });
        container.appendChild(btn);
    });
}

document.addEventListener('DOMContentLoaded', async () => {
    renderSwitcher();
    const strings = await loadLocale(currentLang);
    applyLocale(strings);
});
