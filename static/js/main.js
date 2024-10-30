// Wait for document to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    try {
        // Form validation
        const forms = document.querySelectorAll('.needs-validation');
        
        if (forms && forms.length > 0) {
            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
        }

        // Phone number formatting
        const phoneInput = document.getElementById('phone');
        if (phoneInput) {
            phoneInput.addEventListener('input', function(e) {
                try {
                    let x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
                    e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
                } catch (error) {
                    console.warn('Error formatting phone number:', error);
                }
            });
        }

        // Smooth scrolling for anchor links
        try {
            const anchorLinks = document.querySelectorAll('a[href^="#"]');
            if (anchorLinks && anchorLinks.length > 0) {
                anchorLinks.forEach(anchor => {
                    anchor.addEventListener('click', function(e) {
                        e.preventDefault();
                        const targetId = this.getAttribute('href');
                        if (targetId !== '#') {
                            const target = document.querySelector(targetId);
                            if (target) {
                                target.scrollIntoView({
                                    behavior: 'smooth',
                                    block: 'start'
                                });
                            }
                        }
                    });
                });
            }
        } catch (error) {
            console.warn('Error setting up smooth scroll:', error);
        }

        // Initialize tooltips if Bootstrap is loaded
        try {
            if (typeof bootstrap !== 'undefined') {
                const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
                if (tooltipTriggerList.length > 0) {
                    tooltipTriggerList.map(function(tooltipTriggerEl) {
                        return new bootstrap.Tooltip(tooltipTriggerEl);
                    });
                }
            }
        } catch (error) {
            console.warn('Error initializing tooltips:', error);
        }

        // Initialize Feather icons if available
        try {
            if (typeof feather !== 'undefined') {
                feather.replace();
            }
        } catch (error) {
            console.warn('Error initializing Feather icons:', error);
        }
    } catch (error) {
        console.warn('Error in main.js initialization:', error);
    }
});
