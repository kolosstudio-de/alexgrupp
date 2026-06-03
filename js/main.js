document.addEventListener('DOMContentLoaded', () => {
    /* ==========================================================================
       Theme Switcher Interaction Logic for Split Screen
       ========================================================================== */
    const switcher = document.getElementById('themeSwitcher');
    const autoSide = document.getElementById('autoSide');
    const bauSide = document.getElementById('bauSide');

    // On hover of the switcher, optionally preview the state
    if (switcher) {
        switcher.addEventListener('click', (e) => {
            e.stopPropagation();
            switcher.classList.toggle('is-bau');

            if (switcher.classList.contains('is-bau')) {
                bauSide.style.flex = '1.5';
                autoSide.style.flex = '1';
                autoSide.style.opacity = '0.5';
                bauSide.style.opacity = '1';
            } else {
                autoSide.style.flex = '1.5';
                bauSide.style.flex = '1';
                autoSide.style.opacity = '0.5';
                autoSide.style.opacity = '1';
            }
        });
    }

});
