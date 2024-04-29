document.addEventListener("DOMContentLoaded", function() {
    const registerForm = document.getElementById("registerForm");
    const passwordField = document.getElementById("passwordfield");
    const showPasswordLink = document.getElementById("showPassword");

    registerForm.addEventListener("submit", function(event) {
        const usernameField = document.getElementById("usernamefield");
        const emailField = document.getElementById("emailfield");

        // Username validation
        const usernameRegex = /^[a-zA-Z0-9]+$/;
        if (!usernameRegex.test(usernameField.value)) {
            alert("Username can only contain alphanumeric characters.");
            event.preventDefault();
            return;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailField.value)) {
            alert("Please enter a valid email address.");
            event.preventDefault();
            return;
        }
    });

    // Show password functionality
    showPasswordLink.addEventListener("click", function(event) {
        event.preventDefault();
        if (passwordField.type === "password") {
            passwordField.type = "text";
            showPasswordLink.textContent = "Hide";
        } else {
            passwordField.type = "password";
            showPasswordLink.textContent = "Show";
        }
    });

    document.getElementById("registrationForm").addEventListener("submit", function(event) {
        const passwordField = document.getElementById("password");
        if (passwordField.value.length < 6) {
            alert("Password must be at least 6 characters long.");
            event.preventDefault();
        }
    });
    
   


});
if (alert_message) 
alert("{{ alert_message }}");
endif 

