document.addEventListener('DOMContentLoaded', () => {
    initPosterTransition();
    initSkillTags();
    initTiltCards();
    initBackgroundDepth();
    initMobileMenu();
});

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
        if (indicator) {
            if (window.scrollY > 50) indicator.style.opacity = '0';
            else indicator.style.opacity = '1';
        }
        
        if (nav) {
            if (window.scrollY > window.innerHeight * 0.9) nav.classList.add('visible');
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
