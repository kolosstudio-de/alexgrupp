function initModals() {
    const modalTriggers = document.querySelectorAll('[data-modal]');
    const overlays = document.querySelectorAll('.ag-modal-overlay');
    const closeBtns = document.querySelectorAll('.ag-modal-close');

    // Helper: animate closing a modal overlay
    function closeModal(overlay) {
        if (!overlay || !overlay.classList.contains('active')) return;
        overlay.classList.add('closing');
        overlay.classList.remove('active');
        // Wait for CSS transition to finish before fully hiding
        const content = overlay.querySelector('.ag-modal-content');
        const transitionDuration = content ? 500 : 350;
        setTimeout(() => {
            overlay.classList.remove('closing');
            document.body.style.overflow = '';
        }, transitionDuration);
    }

    if (modalTriggers.length > 0) {
        modalTriggers.forEach(trigger => {
            trigger.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                const modalId = this.getAttribute('data-modal');
                const targetModal = document.getElementById(modalId);
                if (targetModal) {
                    targetModal.classList.remove('closing');
                    targetModal.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }
            });
        });

        closeBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                overlays.forEach(overlay => closeModal(overlay));
            });
        });

        overlays.forEach(overlay => {
            overlay.addEventListener('click', (e) => {
                if (e.target === overlay) {
                    closeModal(overlay);
                }
            });
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                overlays.forEach(overlay => closeModal(overlay));
            }
        });
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initModals);
} else {
    initModals();
}
