// Wait for DOM to be fully loaded before initializing features
function initializeFeatures() {
    // Initialize Feather icons if available
    try {
        if (typeof feather !== 'undefined') {
            feather.replace();
            console.log('Feather icons initialized successfully');
        } else {
            console.warn('Feather icons not loaded');
        }
    } catch (error) {
        console.warn('Error initializing Feather icons:', error);
    }

    // Form validation
    try {
        const forms = document.querySelectorAll('.needs-validation');
        if (forms && forms.length > 0) {
            forms.forEach(form => {
                if (form) {
                    form.addEventListener('submit', event => {
                        if (!form.checkValidity()) {
                            event.preventDefault();
                            event.stopPropagation();
                        }
                        form.classList.add('was-validated');
                    }, false);
                }
            });
            console.log('Form validation initialized');
        }
    } catch (error) {
        console.warn('Error setting up form validation:', error);
    }

    // Phone number formatting
    try {
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
            console.log('Phone input formatting initialized');
        }
    } catch (error) {
        console.warn('Error setting up phone formatting:', error);
    }

    // Initialize Bootstrap tooltips if available
    try {
        if (typeof bootstrap !== 'undefined') {
            const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
            if (tooltipTriggerList.length > 0) {
                tooltipTriggerList.forEach(tooltipTriggerEl => {
                    if (tooltipTriggerEl) {
                        new bootstrap.Tooltip(tooltipTriggerEl);
                    }
                });
                console.log('Bootstrap tooltips initialized');
            }
        } else {
            console.warn('Bootstrap not loaded');
        }
    } catch (error) {
        console.warn('Error initializing tooltips:', error);
    }
}

// Add event listener after declaring the function
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeFeatures);
} else {
    initializeFeatures();
}
