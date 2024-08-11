document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navUl = document.querySelector('nav ul');

    menuToggle.addEventListener('click', function() {
        navUl.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });

    document.addEventListener('click', function(event) {
        const isClickInside = navUl.contains(event.target) || menuToggle.contains(event.target);
        if (!isClickInside) {
            navUl.classList.remove('active');
            menuToggle.classList.remove('active');
        }
    });
});
