/**
 * Smart Header & Cookie Banner Component — V4
 *
 * Header behavior:
 * - Hides immediately when scrolling DOWN (any scroll-down = hide)
 * - Shows ONLY when: (a) user is at the very top (scrollY < 10) OR (b) mouse near top edge
 * - Never shows while user is scrolling down (even slowly)
 */

class SmartHeader {
    constructor() {
        this.header = document.getElementById('mainHeader');
        if (!this.header) return;

        this.prevScrollY = window.scrollY;
        this.hidden = true; // start in hidden state
        this.ticking = false;
        this.mouseNearTop = false;
        this.entryDone = false;
        this.menuOpen = false;

        this.init();
    }

    hide() {
        if (!this.hidden && !this.menuOpen) {
            this.hidden = true;
            this.header.classList.add('header-hidden');
            this.header.classList.remove('visible');
        }
    }

    show() {
        if (this.hidden) {
            this.hidden = false;
            this.header.classList.remove('header-hidden');
            this.header.classList.add('visible');
            if (!this.entryDone) {
                this.entryDone = true;
                // slight delay so CSS transition has time to register
                requestAnimationFrame(() => {
                    requestAnimationFrame(() => {
                        this.header.classList.add('header-loaded');
                    });
                });
            }
        }
    }

    init() {
        // Add scrolled style when not at top
        const updateScrolledClass = () => {
            if (window.scrollY > 20) {
                this.header.classList.add('scrolled');
            } else {
                this.header.classList.remove('scrolled');
            }
        };

        window.addEventListener('scroll', () => {
            if (this.ticking) return;
            this.ticking = true;

            window.requestAnimationFrame(() => {
                const currentY = window.scrollY;
                updateScrolledClass();

                if (currentY <= 10) {
                    // At very top — always visible
                    this.show();
                } else if (currentY > this.prevScrollY) {
                    // Scrolling DOWN — hide immediately
                    this.hide();
                } else if (currentY < this.prevScrollY && this.mouseNearTop) {
                    // Scrolling UP and mouse is near top — show
                    this.show();
                }
                // Scrolling UP without mouse near top — stay hidden

                this.prevScrollY = currentY;
                this.ticking = false;
            });
        }, { passive: true });

        // Mouse near top edge: reveal header
        document.addEventListener('mousemove', (e) => {
            if (e.clientY < 72) {
                this.mouseNearTop = true;
                if (window.scrollY > 10) this.show();
            } else {
                this.mouseNearTop = false;
            }
        });

        // Touch: swipe up near top reveals header
        let touchStartY = 0;
        document.addEventListener('touchstart', (e) => {
            touchStartY = e.touches[0].clientY;
        }, { passive: true });
        document.addEventListener('touchend', (e) => {
            const delta = e.changedTouches[0].clientY - touchStartY;
            if (delta > 40 && window.scrollY <= 10) this.show();
        }, { passive: true });

        // Initial state — always show on load with entrance animation
        setTimeout(() => {
            if (window.scrollY <= 10) {
                this.show();
            } else {
                // scrolled down on load — show briefly then hide
                this.header.classList.add('header-loaded');
                this.entryDone = true;
                this.hide();
            }
            updateScrolledClass();
        }, 120);

        // Burger Menu Toggle
        const burger = document.getElementById('burgerToggle');
        const nav = document.getElementById('headerNav');

        if (burger && nav) {
            burger.addEventListener('click', () => {
                this.menuOpen = !this.menuOpen;
                burger.classList.toggle('active');
                nav.classList.toggle('active');
                document.body.style.overflow = this.menuOpen ? 'hidden' : '';
            });

            // Close menu when link is clicked
            nav.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    this.menuOpen = false;
                    burger.classList.remove('active');
                    nav.classList.remove('active');
                    document.body.style.overflow = '';
                });
            });

            // V-05: Inject empty lang switcher slot into mobile nav
            // i18n.js v6 populates all .langSwitcher-clone divs automatically on DOMContentLoaded
            if (!nav.querySelector('.langSwitcher-clone')) {
                const mobileLang = document.createElement('div');
                mobileLang.className = 'langSwitcher-clone';
                nav.appendChild(mobileLang);
            }
        }
    }
}

// ==========================================
// Cookie Banner Logic
// ==========================================
class CookieBanner {
    constructor() {
        this.bannerId = 'oh-cookie-banner';
        this.storageKey = 'oh_cookie_consent';
        // Compute root path dynamically so the Datenschutz link works on all pages
        const depth = window.location.pathname.replace(/\/[^/]*$/, '').split('/').filter(Boolean).length;
        this.rootPath = depth > 0 ? '../'.repeat(depth) : '';
        this.init();
    }

    init() {
        if (localStorage.getItem(this.storageKey)) return;
        this.injectCSS();
        this.render();
    }

    injectCSS() {
        const style = document.createElement('style');
        style.textContent = `
            #${this.bannerId} {
                position: fixed;
                bottom: 24px;
                left: 24px;
                right: auto;
                width: min(520px, calc(100vw - 48px));
                background: #fff;
                box-shadow: 0 20px 60px rgba(0,0,0,0.18), 0 2px 8px rgba(0,0,0,0.1);
                border-radius: 16px;
                padding: 24px 28px;
                z-index: 9999;
                font-family: 'DM Sans', 'Inter', sans-serif;
                border: 1px solid rgba(0,0,0,0.07);
                transform: translateY(calc(100% + 40px));
                transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
            }
            #${this.bannerId}.show { transform: translateY(0); }
            #${this.bannerId} h3 { font-size: 1rem; color: #0f172a; margin-bottom: 6px; font-weight: 700; }
            #${this.bannerId} p { font-size: 0.82rem; color: #64748b; line-height: 1.6; margin-bottom: 16px; }
            #${this.bannerId} .cookie-buttons { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
            #${this.bannerId} button {
                padding: 9px 18px;
                border-radius: 8px;
                font-size: 0.82rem;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.2s;
                border: none;
                font-family: inherit;
            }
            .btn-cookie-accept { background: #3b7dd8; color: #fff; }
            .btn-cookie-accept:hover { background: #2d68bf; transform: translateY(-1px); }
            .btn-cookie-necessary { background: #f1f5f9; color: #475569; }
            .btn-cookie-necessary:hover { background: #e2e8f0; }
            .cookie-more-link { font-size: 0.8rem; color: #94a3b8; margin-left: auto; text-decoration: underline; white-space: nowrap; }
            
            @media (max-width: 600px) {
                #${this.bannerId} { bottom: 12px; left: 12px; right: 12px; width: auto; padding: 18px; }
                #${this.bannerId} .cookie-buttons { flex-direction: column; }
                #${this.bannerId} button { width: 100%; }
            }
        `;
        document.head.appendChild(style);
    }

    render() {
        const rootPath = this.rootPath;
        const banner = document.createElement('div');
        banner.id = this.bannerId;
        banner.innerHTML = `
            <h3 data-i18n="cookie-title">🍪 Ihre Privatsphäre ist uns wichtig</h3>
            <p data-i18n="cookie-desc">Wir verwenden Cookies zur Optimierung unserer Website. Mit „Alle akzeptieren" stimmen Sie allen Cookies zu. Sie können Ihre Auswahl jederzeit ändern.</p>
            <div class="cookie-buttons">
                <button class="btn-cookie-accept" id="btn-accept-all" data-i18n="cookie-accept">Alle akzeptieren</button>
                <button class="btn-cookie-necessary" id="btn-accept-necessary" data-i18n="cookie-necessary">Nur Notwendige</button>
                <a href="${rootPath}legal/datenschutz.html" class="cookie-more-link" data-i18n="cookie-privacy">Datenschutz</a>
            </div>
        `;
        document.body.appendChild(banner);

        setTimeout(() => banner.classList.add('show'), 800);

        document.getElementById('btn-accept-all').addEventListener('click', () => this.saveConsent('all'));
        document.getElementById('btn-accept-necessary').addEventListener('click', () => this.saveConsent('necessary'));
    }

    saveConsent(level) {
        localStorage.setItem(this.storageKey, level);
        const banner = document.getElementById(this.bannerId);
        banner.classList.remove('show');
        setTimeout(() => banner.remove(), 600);
        if (level === 'all') console.log('Analytics allowed');
    }
}

// Initialize robustly
function initComponents() {
    new SmartHeader();
    new CookieBanner();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initComponents);
} else {
    initComponents();
}
