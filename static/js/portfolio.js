document.addEventListener('DOMContentLoaded', () => {
    initPosterTransition();
    initSkillTags();
    initTiltCards();
    initBackgroundDepth();
});

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
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    
    const elements = document.querySelectorAll('.project-card, .skill-card, .cert-card, .exp-card, .edu-card, .btn-primary, .btn-secondary, .profile-frame, .poster-3d-element');
    
    elements.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            const multiplier = el.classList.contains('project-card') ? 0.02 : 0.05;
            
            el.style.transform = `perspective(1000px) rotateX(${-y * multiplier}deg) rotateY(${x * multiplier}deg) scale3d(1.02, 1.02, 1.02)`;
        });
        
        el.addEventListener('mouseleave', () => {
            el.style.transform = '';
        });
    });
}

// Background depth parallax
function initBackgroundDepth() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    
    const bgElements = document.querySelectorAll('.bg-orb, .bg-ring, .bg-grid, .bg-timeline-graphic, .bg-orbital-paths, .bg-pattern-dots');
    
    // Mouse interaction for desktop
    window.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        
        bgElements.forEach((el, index) => {
            // Give different elements slightly different movement ratios
            const factor = (index % 3 + 1) * 0.5;
            el.style.transform = `translate3d(${x * factor}px, ${y * factor}px, 0)`;
        });
    });

    // Scroll interaction
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        bgElements.forEach((el, index) => {
            const speed = (index % 4 + 1) * 0.05;
            const currentTransform = el.style.transform.replace(/translateY\([^)]*\)/g, '').trim();
            el.style.transform = `${currentTransform} translateY(${scrolled * speed}px)`;
        });
        
        // Navbar shadow on scroll
        const nav = document.querySelector('.nav');
        if (nav) {
            if (scrolled > 50) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        }
    });
}
