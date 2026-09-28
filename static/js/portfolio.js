document.addEventListener('DOMContentLoaded', () => {
    initHeroAnimation();
    initPosterTransition();
    initSkillTags();
    initTiltCards();
    initBackgroundDepth();
    initMobileMenu();
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
    const poster = document.getElementById('introPoster');
    const indicator = document.getElementById('scrollIndicator');
    const nav = document.querySelector('.nav');
    
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        
        if (indicator) {
            if (scrolled > 50) indicator.style.opacity = '0';
            else indicator.style.opacity = '1';
        }
        
        if (poster && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            if (scrolled > 0 && scrolled < window.innerHeight) {
                const progress = Math.min(scrolled / (window.innerHeight * 0.5), 1);
                poster.style.opacity = 1 - (progress * 0.25); // 1 to 0.75
                poster.style.transform = `translateY(${-20 * progress}px) scale(${1 - (0.02 * progress)})`;
            } else if (scrolled === 0) {
                poster.style.opacity = '1';
                poster.style.transform = 'translateY(0) scale(1)';
            }
        }
        
        if (nav) {
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
        const nav = document.querySelector('.nav');
        if (nav) {
            if (scrolled > 50) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        }
    });
}
