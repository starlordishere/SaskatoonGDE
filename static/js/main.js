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

    // Phone number validation and formatting
    try {
        const phoneInput = document.getElementById('phone');
        if (phoneInput) {
            phoneInput.addEventListener('input', function(e) {
                // Strip all non-digit characters
                let value = e.target.value.replace(/\D/g, '');
                
                // Truncate to 10 digits if longer
                if (value.length > 10) {
                    value = value.substring(0, 10);
                }
                
                // Format the number as (XXX) XXX-XXXX
                if (value.length > 0) {
                    let formatted = '';
                    if (value.length > 0) formatted += '(' + value.substring(0, Math.min(3, value.length));
                    if (value.length > 3) formatted += ') ' + value.substring(3, Math.min(6, value.length));
                    if (value.length > 6) formatted += '-' + value.substring(6, Math.min(10, value.length));
                    e.target.value = formatted;
                }

                // Set validation state
                if (value.length === 10) {
                    this.setCustomValidity('');
                } else {
                    this.setCustomValidity('Please enter exactly 10 digits');
                }
            });

            // Add blur event to enforce format
            phoneInput.addEventListener('blur', function() {
                const digits = this.value.replace(/\D/g, '');
                if (digits.length !== 10) {
                    this.classList.add('is-invalid');
                } else {
                    this.classList.remove('is-invalid');
                }
            });

            console.log('Phone input validation initialized');
        }
    } catch (error) {
        console.warn('Error setting up phone validation:', error);
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
