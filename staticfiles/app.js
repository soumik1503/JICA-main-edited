

// Mobile menu toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
}

// Close mobile menu when clicking on links
const mobileLinks = mobileMenu.querySelectorAll('a');
mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
// Smooth scroll enhancement
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({
                behavior: "smooth",
                block: "start",
            });
        }
    });
});

const swiper = new Swiper(".mySwiper", {
    loop: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false
    },

    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev"
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    spaceBetween: 4,
    slidesPerView: 6,
    breakpoints: {
        360: {
            slidesPerView: 2,
            spaceBetween: 4,
        },
        // when window width is >= 768px
        768: {
            slidesPerView: 4,
            spaceBetween: 4
        },
        // when window width is >= 1024px
        1024: {
            slidesPerView: 6,
            spaceBetween: 4
        }
    }
});

const backToTopBtn = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    backToTopBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
});

if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Apply saved theme on load
const savedColourScheme = localStorage.getItem('colour-scheme') || 'blue';
setColourScheme(savedColourScheme);

// Theme switcher
function setColourScheme(colourScheme) {
    document.documentElement.setAttribute('data-theme', colourScheme);
    localStorage.setItem('colour-scheme', colourScheme);
}

// Text size adjuster
const body = document.querySelector('body');
const decreaseText = document.getElementById('decreaseText');
const resetText = document.getElementById('resetText');
const increaseText = document.getElementById('increaseText');

let currentFontSize = 16;

if (decreaseText) {
    decreaseText.addEventListener('click', () => {
        currentFontSize = Math.max(12, currentFontSize - 1);
        body.style.fontSize = `${currentFontSize}px`;
    });
}

if (resetText) {
    resetText.addEventListener('click', () => {
        currentFontSize = 16;
        body.style.fontSize = `${currentFontSize}px`;
    });
}

if (increaseText) {
    increaseText.addEventListener('click', () => {
        currentFontSize = Math.min(24, currentFontSize + 1);
        body.style.fontSize = `${currentFontSize}px`;
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide-container');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const carouselDotsContainer = document.getElementById('carouselDots');
    let activeIndex = 0; // Start with the first slide

    // Function to update slide visibility
    function showSlide(index) {
        slides.forEach((slide, i) => {
            if (i === index) {
                slide.classList.remove('slide-hidden');
                slide.classList.add('slide-visible');
            } else {
                slide.classList.remove('slide-visible');
                slide.classList.add('slide-hidden');
            }
        });
        updateDots(index);
    }

    // Function to generate and update navigation dots
    function createDots() {
        if (carouselDotsContainer) {
            carouselDotsContainer.innerHTML = ''; // Clear existing dots
            slides.forEach((_, i) => {
                const dot = document.createElement('span');
                dot.classList.add('dot');
                dot.dataset.index = i; // Store index for click handling
                dot.addEventListener('click', () => showSlide(i));
                carouselDotsContainer.appendChild(dot);
            });
        }
    }

    // Function to highlight active dot
    function updateDots(newIndex) {
        const dots = document.querySelectorAll('.dot');
        dots.forEach((dot, i) => {
            if (i === newIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    // Event Listeners for buttons
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            activeIndex = (activeIndex - 1 + slides.length) % slides.length;
            showSlide(activeIndex);
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            activeIndex = (activeIndex + 1) % slides.length;
            showSlide(activeIndex);
        });
    }

    // Initialize carousel
    createDots(); // Create dots based on the number of slides
    showSlide(activeIndex); // Show the first slide initially

    // Optional: Auto-play functionality
    let autoPlayInterval = setInterval(() => {
        activeIndex = (activeIndex + 1) % slides.length;
        showSlide(activeIndex);
    }, 2000); // Change slide every 4 seconds

    // Optional: Pause auto-play on hover
    const carouselWrapper = document.querySelector('.carousel-wrapper');
    if (carouselWrapper) {
        carouselWrapper.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
        carouselWrapper.addEventListener('mouseleave', () => {
            autoPlayInterval = setInterval(() => {
                activeIndex = (activeIndex + 1) % slides.length;
                showSlide(activeIndex);
            }, 2000);
        });
    }
});

// Simple tab switcher (Vanilla JS)
const tabs = document.querySelectorAll("[data-tab]");
const contents = document.querySelectorAll("[id^='content-']");

tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        // Reset all
        tabs.forEach((t) =>
            t.classList.replace("bg-blue-600", "bg-gray-600")
        );

        contents.forEach((c) => c.classList.add("hidden"));

        // Activate clicked
        tab.classList.replace("bg-gray-600", "bg-blue-600");
        tab.classList.add("text-white");
        document.getElementById("content-" + tab.dataset.tab).classList.remove("hidden");
    });
});