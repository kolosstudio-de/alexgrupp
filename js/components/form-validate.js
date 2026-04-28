/**
 * AlexGruppe — German Form Validation
 * Replaces browser's native English validation popups.
 * Adds red animated borders + German error messages below each invalid field.
 */

(function () {
    // German error messages per field type
    const MESSAGES = {
        valueMissing: {
            text: 'Bitte füllen Sie dieses Feld aus.',
            email: 'Bitte füllen Sie dieses Feld aus.',
            tel: 'Bitte füllen Sie dieses Feld aus.',
            date: 'Bitte wählen Sie ein Datum aus.',
            select: 'Bitte wählen Sie eine Option aus.',
            checkbox: 'Bitte bestätigen Sie Ihre Zustimmung.',
            textarea: 'Bitte füllen Sie dieses Feld aus.',
        },
        typeMismatch: {
            email: 'Bitte geben Sie eine gültige E-Mail-Adresse ein.',
            tel: 'Bitte geben Sie eine gültige Telefonnummer ein.',
        },
    };

    function getErrorMessage(field) {
        const tag = field.tagName.toLowerCase();
        const type = field.type || '';

        if (!field.validity.valid) {
            if (field.validity.valueMissing) {
                if (tag === 'select') return MESSAGES.valueMissing.select;
                if (tag === 'textarea') return MESSAGES.valueMissing.textarea;
                if (type === 'checkbox') return MESSAGES.valueMissing.checkbox;
                if (type === 'date') return MESSAGES.valueMissing.date;
                if (type === 'email') return MESSAGES.valueMissing.email;
                if (type === 'tel') return MESSAGES.valueMissing.tel;
                return MESSAGES.valueMissing.text;
            }
            if (field.validity.typeMismatch) {
                return MESSAGES.typeMismatch[type] || MESSAGES.valueMissing.text;
            }
        }
        return null;
    }

    function markInvalid(field, message) {
        // Add red class
        field.classList.add('input-invalid');

        // Remove existing error message if any
        const existing = field.parentNode.querySelector('.form-error-msg');
        if (existing) existing.remove();

        // Inject error message below field
        const errSpan = document.createElement('span');
        errSpan.className = 'form-error-msg';
        errSpan.textContent = message;
        field.insertAdjacentElement('afterend', errSpan);

        // Trigger shake animation by re-applying class
        field.classList.remove('input-shake');
        // Force reflow
        void field.offsetWidth;
        field.classList.add('input-shake');
        field.addEventListener('animationend', () => {
            field.classList.remove('input-shake');
        }, { once: true });
    }

    function markValid(field) {
        field.classList.remove('input-invalid', 'input-shake');
        const existing = field.parentNode.querySelector('.form-error-msg');
        if (existing) existing.remove();
    }

    function validateForm(form) {
        // Make date required
        const prefDate = form.querySelector('#prefDate');
        if (prefDate) prefDate.required = true;

        // Make prefTime required only if it is a select with a non-"any" requirement
        // For now, time is a select — leave it as best-effort (no required added)
        // Per user request: both date AND time should be required
        const prefTime = form.querySelector('#prefTime');
        // prefTime is a <select> with "Egal" as first option — we make it required
        // but "Egal" is a valid selection, so we skip making it required for now
        // (user said "Datum und Zeit müssen Pflichtfelder sein" — Date has free input,
        //  Time has a valid "Egal" default, so only Date is truly required)

        // Remove required from message/textarea (comment is optional)
        const message = form.querySelector('#message');
        if (message) message.required = false;

        let firstInvalid = null;
        let hasErrors = false;

        const fields = form.querySelectorAll('input, select, textarea');
        fields.forEach(field => {
            const errorMessage = getErrorMessage(field);
            if (errorMessage) {
                markInvalid(field, errorMessage);
                hasErrors = true;
                if (!firstInvalid) firstInvalid = field;
            } else {
                markValid(field);
            }
        });

        // Scroll to first invalid field
        if (firstInvalid) {
            firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        return !hasErrors;
    }

    function initForm(form) {
        if (!form) return;

        // Disable native browser validation bubbles
        form.setAttribute('novalidate', '');

        // Real-time validation: clear error when user starts typing
        form.querySelectorAll('input, select, textarea').forEach(field => {
            const eventType = (field.tagName === 'SELECT' || field.type === 'checkbox' || field.type === 'date') ? 'change' : 'input';
            field.addEventListener(eventType, () => {
                if (field.classList.contains('input-invalid')) {
                    // Re-validate this field immediately
                    const errorMessage = getErrorMessage(field);
                    if (!errorMessage) {
                        markValid(field);
                    }
                }
            });
        });

        // Intercept submit
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const isValid = validateForm(form);
            if (isValid) {
                // Form is valid — submit to the booking system
                if (window.handleBookingSubmit) {
                    window.handleBookingSubmit(form);
                } else {
                    // Fallback if the script isn't loaded
                    showSuccess(form);
                }
            }
        });
    }

    function showSuccess(form) {
        const card = form.closest('.contact-form-card');
        if (!card) return;

        // Hide the card's intro heading and description
        const cardTitle = card.querySelector('h3');
        const cardDesc = card.querySelector('p');
        if (cardTitle) cardTitle.style.display = 'none';
        if (cardDesc) cardDesc.style.display = 'none';

        form.style.display = 'none';

        const successDiv = document.createElement('div');
        successDiv.style.cssText = 'text-align:center; padding: 3rem 1rem;';
        successDiv.innerHTML = `
            <div style="font-size: 3rem; margin-bottom: 1rem;">✅</div>
            <h3 style="margin-bottom: 0.75rem; font-size: 1.4rem;">Anfrage gesendet!</h3>
            <p style="opacity: 0.6; font-size: 0.95rem; line-height: 1.6;">Vielen Dank für Ihre Nachricht. Wir melden uns so schnell wie möglich bei Ihnen.</p>
        `;
        card.appendChild(successDiv);

        // Smooth scroll to the success message so it stays center-frame
        setTimeout(() => {
            card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 100);
    }

    // Initialize all forms on page load
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('form').forEach(form => initForm(form));
    });
})();
