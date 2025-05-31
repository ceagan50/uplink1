// Live Time Update
function updateTime() {
    const now = new Date();
    const options = { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    };
    const liveTimeElement = document.getElementById('liveTime');
    if (liveTimeElement) {
        liveTimeElement.textContent = now.toLocaleDateString('en-US', options);
    }
}

// Update time every second
setInterval(updateTime, 1000);
updateTime(); // Initial call

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form submission handling
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        const submitButton = this.querySelector('button[type="submit"]');
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
        }
    });
});

// Admin login form toggle
function toggleAdminForm(type) {
    const forms = document.querySelectorAll('.admin-form');
    forms.forEach(form => {
        form.style.display = 'none';
    });
    document.getElementById(`${type}-form`).style.display = 'block';
}