document.addEventListener('DOMContentLoaded', () => {
    initHeroAnimation();
    initSkillTags();
    initTiltCards();
    initMobileMenu();
    initScrollReveal();
    initPosterTransition();
    initBackgroundDepth();
});

function initHeroAnimation() {
    const title = document.querySelector('.poster-title');
    const subtitle = document.querySelector('.poster-subtitle');
    const tagline = document.querySelector('.poster-tagline');
    const indicator = document.querySelector('.scroll-indicator');
    const bg = document.querySelector('.poster-3d-element');
    
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        // Show everything immediately for reduced motion
        [title, subtitle, tagline, indicator, bg].forEach(el => {
            if (el) { el.style.opacity = '1'; el.style.transform = 'none'; el.style.filter = 'none'; }
        });
        return;
    }
    
    // Safety check to prevent duplicate initialization
    if (title && title.hasAttribute('data-animated')) return;
    if (title) title.setAttribute('data-animated', 'true');
    
    // Split title into words for subtle stagger
    if (title) {
        const text = title.textContent;
        title.setAttribute('aria-label', text);
        title.innerHTML = '';
        title.style.opacity = '1'; // Fix: make parent visible so child span animations show
        title.style.transform = 'none';
        title.style.filter = 'none';
        const words = text.split(' ');
        words.forEach((word, i) => {
            const span = document.createElement('span');
            span.textContent = word;
            span.style.display = 'inline-block';
            span.style.opacity = '0';
            span.style.transform = 'translateY(35px)';
            span.style.filter = 'blur(8px)';
            span.style.animation = `heroTextReveal 1.5s cubic-bezier(0.2, 0.8, 0.2, 1) ${0.3 + (i * 0.1)}s forwards`;
            title.appendChild(span);
            
            if (i < words.length - 1) {
                title.appendChild(document.createTextNode(' '));
            }
        });
    }
    
    if (bg) {
        bg.style.opacity = '0';
        bg.style.transform = 'scale(0.92)';
        bg.style.animation = 'heroBgReveal 1.8s ease-out forwards, heroBgBreathe 12s ease-in-out infinite 1.8s';
    }
    
    if (subtitle) {
        subtitle.style.opacity = '0';
        subtitle.style.transform = 'translateY(15px)';
        subtitle.style.letterSpacing = '8px';
        subtitle.style.animation = 'heroSubtitleReveal 1s cubic-bezier(0.2, 0.8, 0.2, 1) 1.2s forwards';
    }
    
    if (tagline) {
        tagline.style.opacity = '0';
        tagline.style.transform = 'translateY(12px)';
        tagline.style.animation = 'heroFadeUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) 1.6s forwards';
    }
    
    if (indicator) {
        indicator.style.opacity = '0';
        indicator.style.transform = 'translateX(15px)';
        indicator.style.animation = 'heroFadeLeft 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) 2.0s forwards';
    }
}

// The hamburger button was rendered on small screens but nothing was wired to it,
// so the nav links (hidden via CSS at <=900px) could never be opened.
function initMobileMenu() {
    const btn = document.querySelector('.menu-btn');
    const links = document.querySelector('.navlinks');
    if (!btn || !links) return;

    const setOpen = (open) => {
        links.classList.toggle('open', open);
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    };

    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', () => setOpen(!links.classList.contains('open')));
    links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
}

function initSkillTags() {
    document.querySelectorAll('.skill-tags').forEach(el => {
        const skillsAttr = el.getAttribute('data-skills');
        if (!skillsAttr) return;
        const skills = skillsAttr.split(',');
        skills.forEach(skill => {
            if (skill.trim()) {
                const span = document.createElement('span');
                span.textContent = skill.trim();
                el.appendChild(span);
            }
        });
    });
}

function initPosterTransition() {
    const introScreen = document.querySelector('.intro-screen');
    const indicator = document.querySelector('.intro-scroll-line');
    const nav = document.querySelector('.portfolio-navbar');
    
    // If no intro screen, nav should be visible immediately
    if (nav && !introScreen) {
        nav.classList.add('visible');
    }
    
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        
        if (indicator) {
            if (scrolled > 50) indicator.style.opacity = '0';
            else indicator.style.opacity = '1';
        }
        
        if (introScreen && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            if (scrolled > 0 && scrolled < window.innerHeight) {
                const progress = Math.min(scrolled / (window.innerHeight * 0.5), 1);
                introScreen.style.opacity = 1 - (progress * 0.25);
                introScreen.style.transform = `translateY(${-20 * progress}px) scale(${1 - (0.02 * progress)})`;
            } else if (scrolled === 0) {
                introScreen.style.opacity = '1';
                introScreen.style.transform = 'translateY(0) scale(1)';
            }
        }
        
        if (nav && introScreen) {
            if (scrolled > window.innerHeight * 0.9) nav.classList.add('visible');
            else nav.classList.remove('visible');
        }
    });
}

function initTiltCards() {
    // Removed excessive 3D tilt animation on every card to maintain a calm, premium editorial feel
}

// Background depth parallax
function initBackgroundDepth() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    
    // Scroll interaction only (removed excessive mousemove parallax)
    const bgElements = document.querySelectorAll('.bg-orb, .bg-ring, .bg-grid, .bg-timeline-graphic, .bg-orbital-paths, .bg-pattern-dots');
    
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        bgElements.forEach((el, index) => {
            const speed = (index % 4 + 1) * 0.02; // Reduced speed for subtlety
            el.style.transform = `translateY(${scrolled * speed}px)`;
        });
        
        // Navbar shadow on scroll
        const nav = document.querySelector('.portfolio-navbar');
        if (nav) {
            if (scrolled > 50) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        }
    });
}

function initScrollReveal() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        document.querySelectorAll('.reveal-on-scroll').forEach(el => {
            el.classList.add('is-revealed');
        });
        return;
    }
    
    const elements = document.querySelectorAll('.reveal-on-scroll');
    if (!elements.length) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-revealed');
                observer.unobserve(entry.target);
            }
        });
    }, { rootMargin: '0px 0px -50px 0px', threshold: 0.1 });
    
    elements.forEach(el => observer.observe(el));
}


// Keyboard Shortcuts System
const PortfolioShortcuts = (function() {
    let shortcutsEnabled = true;
    const storageKey = 'portfolioKeyboardShortcuts';
    
    const modal = document.getElementById('shortcuts-modal');
    const toggle = document.getElementById('keyboard-shortcuts-toggle');
    const closeBtn = document.getElementById('close-shortcuts-btn');
    const footerBtn = document.getElementById('open-shortcuts-footer');
    
    // Init state
    const saved = localStorage.getItem(storageKey);
    if (saved === 'disabled') {
        shortcutsEnabled = false;
        if(toggle) toggle.checked = false;
    }

    function isTypingTarget(el) {
        if (!el) return false;
        const tag = el.tagName.toUpperCase();
        if (['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON'].includes(tag)) return true;
        if (el.isContentEditable) return true;
        return false;
    }

    function openHelp() {
        if (!modal) return;
        modal.style.display = 'flex';
        if (closeBtn) closeBtn.focus();
    }

    function closeHelp() {
        if (!modal) return;
        modal.style.display = 'none';
        if (footerBtn) footerBtn.focus();
    }

    function handleKeydown(e) {
        // Protect inputs
        if (isTypingTarget(e.target)) return;
        
        // Protect modifiers
        if (e.ctrlKey || e.metaKey || e.altKey) return;
        
        const key = e.key;
        
        // Always allow Escape to close modal
        if (key === 'Escape') {
            closeHelp();
            return;
        }

        // Always allow ? to open modal regardless of disabled state
        if (key === '?') {
            openHelp();
            return;
        }

        if (!shortcutsEnabled) return;

        // Navigation
        const routes = window.portfolioRoutes;
        if (!routes) return;
        
        const lowerKey = key.toLowerCase();
        
        switch (lowerKey) {
            case 'h':
                window.location.href = routes.home;
                break;
            case 'p':
                window.location.href = routes.projects;
                break;
            case 'r':
                window.location.href = routes.resume;
                break;
            case 'l':
                window.location.href = routes.learn;
                break;
            case 's':
                window.location.href = routes.status;
                break;
            case 'a':
                if (typeof window.openAIChat === 'function') {
                    e.preventDefault();
                    window.openAIChat();
                } else {
                    const aiBtn = document.getElementById('ai-chat-btn');
                    if (aiBtn) aiBtn.click();
                }
                break;
        }
    }

    function setup() {
        document.addEventListener('keydown', handleKeydown);
        
        if (modal) {
            modal.addEventListener('click', closeHelp);
        }
        
        if (closeBtn) {
            closeBtn.addEventListener('click', closeHelp);
        }
        
        if (footerBtn) {
            footerBtn.addEventListener('click', openHelp);
        }
        
        if (toggle) {
            toggle.addEventListener('change', function(e) {
                shortcutsEnabled = e.target.checked;
                localStorage.setItem(storageKey, shortcutsEnabled ? 'enabled' : 'disabled');
            });
        }
    }

    return {
        init: setup
    };
})();

document.addEventListener('DOMContentLoaded', function() {
    PortfolioShortcuts.init();
});


// Scroll Progress Bar & Navbar background
window.addEventListener('scroll', () => {
    const scrollProgress = document.getElementById('scroll-progress');
    if (scrollProgress) {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrollPercent = (scrollTop / scrollHeight) * 100;
        scrollProgress.style.width = scrollPercent + '%';
    }
});

