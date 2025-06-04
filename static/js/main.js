document.addEventListener('DOMContentLoaded', function() {
    // Theme toggle functionality
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = themeToggle.querySelector('i');
    
    // Check for saved theme preference or use default
    const savedTheme = localStorage.getItem('theme') || 'dark';
    body.classList.add(savedTheme + '-theme');
    updateThemeIcon(savedTheme);
    
    // Toggle theme when button is clicked
    themeToggle.addEventListener('click', function() {
        if (body.classList.contains('dark-theme')) {
            body.classList.replace('dark-theme', 'light-theme');
            localStorage.setItem('theme', 'light');
            updateThemeIcon('light');
        } else {
            body.classList.replace('light-theme', 'dark-theme');
            localStorage.setItem('theme', 'dark');
            updateThemeIcon('dark');
        }
    });
    
    function updateThemeIcon(theme) {
        if (theme === 'dark') {
            icon.classList.replace('fa-sun', 'fa-moon');
        } else {
            icon.classList.replace('fa-moon', 'fa-sun');
        }
    }
    
    // Add current year to footer
    const currentYear = new Date().getFullYear();
    document.querySelector('footer p').innerHTML = document.querySelector('footer p').innerHTML.replace('{{ current_year }}', currentYear);
});