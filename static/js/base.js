// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mainNav = document.getElementById('mainNav');

function resetMessages() {
        // Скрываем все сообщения
        document.querySelectorAll('.error-message, .success-message').forEach(el => {
            el.style.display = 'none';
            el.textContent = '';
        });
        
        // Очищаем ошибки полей
        document.querySelectorAll('.error').forEach(el => {
            el.textContent = '';
        });
    }

function showSuccess(message) {
    const successEl = document.getElementById('success-message');
    successEl.textContent = message;
    successEl.style.display = 'block';
}

function showErrors(errors, generalMessage) {
    if (errors) {
        Object.keys(errors).forEach(field => {
            const errorEl = document.getElementById(`${field}-error`);
            if (errorEl) {
                errorEl.innerHTML = errors[field].join('<br>');
            }
        });
    }
    
    if (generalMessage) {
        const errorEl = document.getElementById('error-message');
        errorEl.textContent = generalMessage;
        errorEl.style.display = 'block';
    }
}

function showError(message) {
    const errorEl = document.getElementById('error-message');
    errorEl.textContent = message;
    errorEl.style.display = 'block';
}

mobileMenuBtn.addEventListener('click', () => {
    mainNav.classList.toggle('active');
    mobileMenuBtn.innerHTML = mainNav.classList.contains('active') 
        ? '<i class="bi bi-x"></i>' 
        : '<i class="bi bi-list"></i>';
});

// Close mobile menu on link click
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', () => {
        mainNav.classList.remove('active');
        mobileMenuBtn.innerHTML = '<i class="bi bi-list"></i>';
    });
});

// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
const themeIcon = themeToggle.querySelector('i');

// Check for saved theme or prefer-color-scheme
const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
const currentTheme = localStorage.getItem('theme') || 
                    (prefersDarkScheme.matches ? 'dark' : 'light');

if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    themeIcon.className = 'bi bi-sun';
}

themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    let newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    themeIcon.className = newTheme === 'dark' ? 'bi bi-sun' : 'bi bi-moon';
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Form submission
// const contactForm = document.getElementById('contactForm');
// contactForm.addEventListener('submit', function(e) {
//     e.preventDefault();
//     const submitBtn = document.getElementById('submit-btn');
//     const csrfToken = document.getElementById('csrf_token').value;
//     // Here you would normally send the data to a server
//     // Сброс сообщений и ошибок
//     resetMessages();
        
//     // Показываем спиннер
//     submitBtn.disabled = true;
//     spinner.style.display = 'inline-block';
        
//     try {
//         const formData = new FormData(contactForm);
//         // const formData = {
//         // name: document.getElementById('id_name').value,
//         // email: document.getElementById('id_email').value,
//         // subject: document.getElementById('id_subject').value,
//         // message: document.getElementById('id_message').value
//         // };
//         console.log(formData)
//         const response = fetch('/contact/ajax/', {
//             method: 'POST',
//             body: formData,
//             headers: {
//                 'X-Requested-With': 'XMLHttpRequest',
//                 'X-CSRFToken': csrfToken
//             }
//         });
        
//         const data = response.json();
//         console.log(data)
//         if (response.ok && data.success) {
//             showSuccess(data.message);
//             form.reset();
//         } else {
//             showErrors(data.errors, data.message);
//         }
//     } catch (error) {
//         showError('Произошла ошибка сети. Попробуйте еще раз.');
//     } finally {
//         submitBtn.disabled = false;
//         spinner.style.display = 'none';
//     }
//     // For now, just show an alert
//     // alert(`Спасибо, ${formData.name}! Ваше сообщение отправлено. Я свяжусь с вами в ближайшее время.`);
    
//     // Reset form
//     contactForm.reset();
// });

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submit-btn');
    const spinner = document.getElementById('spinner');
    const csrfToken = document.getElementById('csrf_token').value;
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Сброс сообщений и ошибок
        resetMessages();
        
        // Показываем спиннер
        submitBtn.disabled = true;
        spinner.style.display = 'inline-block';
        
        try {
            const formData = new FormData(form);
            
            const response = await fetch('contact/ajax/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                }
            });
            
            const data = await response.json();
            
            if (response.ok && data.success) {
                showSuccess(data.message);
                form.reset();
            } else {
                showErrors(data.errors, data.message);
            }
        } catch (error) {
            showError('Произошла ошибка сети. Попробуйте еще раз.');
        } finally {
            submitBtn.disabled = false;
            spinner.style.display = 'none';
        }
    });
    
    function resetMessages() {
        // Скрываем все сообщения
        document.querySelectorAll('.error-message, .success-message').forEach(el => {
            el.style.display = 'none';
            el.textContent = '';
        });
        
        // Очищаем ошибки полей
        document.querySelectorAll('.error').forEach(el => {
            el.textContent = '';
        });
    }
    
    function showSuccess(message) {
        const successEl = document.getElementById('success-message');
        successEl.textContent = message;
        successEl.style.display = 'block';
    }
    
    function showErrors(errors, generalMessage) {
        if (errors) {
            Object.keys(errors).forEach(field => {
                const errorEl = document.getElementById(`${field}-error`);
                if (errorEl) {
                    errorEl.innerHTML = errors[field].join('<br>');
                }
            });
        }
        
        if (generalMessage) {
            const errorEl = document.getElementById('error-message');
            errorEl.textContent = generalMessage;
            errorEl.style.display = 'block';
        }
    }
    
    function showError(message) {
        const errorEl = document.getElementById('error-message');
        errorEl.textContent = message;
        errorEl.style.display = 'block';
    }
    
    // Очистка ошибок при вводе
    document.querySelectorAll('.form-control').forEach(input => {
        input.addEventListener('input', function() {
            const fieldName = this.name;
            const errorEl = document.getElementById(`${fieldName}-error`);
            if (errorEl) {
                errorEl.textContent = '';
            }
        });
    });
});


// Animate skill bars on scroll
const animateSkillBars = () => {
    const skillBars = document.querySelectorAll('.skill-progress');
    skillBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        
        setTimeout(() => {
            bar.style.width = width;
        }, 300);
    });
};

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            if (entry.target.id === 'skills') {
                animateSkillBars();
            }
            
            // Add animation class to section
            entry.target.classList.add('animated');
        }
    });
}, observerOptions);

// Observe sections
document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
});

// Header scroll effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    if (window.scrollY > 100) {
        header.style.padding = '1rem 0';
        header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.1)';
    } else {
        header.style.padding = '2rem 0';
        header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    }
});

// Current year in footer
document.addEventListener('DOMContentLoaded', () => {
    const yearElement = document.querySelector('.copyright');
    if (yearElement) {
        const currentYear = new Date().getFullYear();
        yearElement.textContent = yearElement.textContent.replace('2024', currentYear);
    }
});