const password = document.getElementById("password");
const toggleButton = document.getElementById("togglePassword");

toggleButton.addEventListener("click", function () {

    if (password.type === "password") {

        password.type = "text";
        toggleButton.textContent = "Hide";

    } else {

        password.type = "password";
        toggleButton.textContent = "Show";

    }

});

const confirmPassword = document.getElementById("confirmPassword");
const toggleConfirmButton = document.getElementById("toggleConfirmPassword");

toggleConfirmButton.addEventListener("click", function () {

    if (confirmPassword.type === "password") {

        confirmPassword.type = "text";
        toggleConfirmButton.textContent = "Hide";

    } else {

        confirmPassword.type = "password";
        toggleConfirmButton.textContent = "Show";

    }

});

const strengthMessage = document.getElementById("strengthMessage");

password.addEventListener("input", function () {

    let userPassword = password.value;
    const hasUpperCase = /[A-Z]/.test(userPassword);
    const hasLowerCase = /[a-z]/.test(userPassword);
    const hasNumber = /[0-9]/.test(userPassword);
    const hasSpecialCharacter = /[!@#$%^&*(),.?":{}|<>]/.test(userPassword);

    if (userPassword.length < 6) {

        strengthMessage.textContent = "🔴 Weak Password";
        strengthMessage.style.color = "red";

    }

    else if (
        userPassword.length >= 10 &&
        hasUpperCase &&
        hasLowerCase &&
        hasNumber &&
        hasSpecialCharacter
    ) {

        strengthMessage.textContent = "🟢 Strong Password";
        strengthMessage.style.color = "green";

    }

    else {

        strengthMessage.textContent = "🟡 Medium Password";
        strengthMessage.style.color = "orange";

    }


});

const matchMessage = document.getElementById("matchMessage");

confirmPassword.addEventListener("input", function () {

    if (
        password.value.length === 0 ||
        confirmPassword.value.length === 0
    ) {

        matchMessage.textContent = "";
        return;
    }

    

    if (password.value === confirmPassword.value) {

        matchMessage.textContent = "✅ Passwords Match";
        matchMessage.style.color = "green";

    }
    else {

        matchMessage.textContent = "❌ Passwords Do Not Match";
        matchMessage.style.color = "red";

    }

});