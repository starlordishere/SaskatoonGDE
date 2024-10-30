// Wait for document to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Feather icons if available
    try {
        if (typeof feather !== 'undefined') {
            feather.replace();
        }
    } catch (error) {
        console.warn('Error initializing Feather icons:', error);
    }

    // Form validation
    try {
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
    } catch (error) {
        console.warn('Error setting up form validation:', error);
    }

    // Phone number formatting
    try {
        const phoneInput = document.getElementById('phone');
        if (phoneInput) {
            phoneInput.addEventListener('input', function(e) {
                let x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
                e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
            });
        }
    } catch (error) {
        console.warn('Error setting up phone formatting:', error);
    }

    // Initialize Bootstrap tooltips if available
    try {
        if (typeof bootstrap !== 'undefined') {
            const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
            tooltipTriggerList.forEach(tooltipTriggerEl => {
                new bootstrap.Tooltip(tooltipTriggerEl);
            });
        }
    } catch (error) {
        console.warn('Error initializing tooltips:', error);
    }
});
