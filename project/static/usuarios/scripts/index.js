async function sendUserData(action, data) {
    try {
        const response = await fetch('/usuarios/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({ action, ...data })
        });

        const result = await response.json();
        if (response.ok) {
            Toastify({
                text: `${result.success}`,
                duration: 2000,
                gravity: 'top',
                position: 'center',
                style: {
                    background: "linear-gradient(to right,rgb(228, 10, 232),rgb(255, 191, 0))",
                    color: "rgb(0,0,0)"
                },
            }).showToast();
            setTimeout(() => {
                window.location.href = `../../`;
            }, 2000);
        } else {
            Toastify({
                text: `${result.error}`,
                duration: 2000,
                gravity: 'top',
                position: 'center',
                style: {
                    background: "linear-gradient(to right,rgb(255, 0, 0),rgb(251, 66, 66))",
                    color: "rgb(221,221,221)",
                },
            }).showToast();
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function sendUserDataFormData(formData) {
    try {
        const response = await fetch('/usuarios/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken()
            },
            body: formData
        });

        const result = await response.json();
        if (response.ok) {
            Toastify({
                text: `${result.success}`,
                duration: 2000,
                gravity: 'top',
                position: 'center',
                style: {
                    background: "linear-gradient(to right,rgb(173, 0, 176),rgb(255, 191, 0))",
                },
            }).showToast();
        } else {
            Toastify({
                text: `${result.error}`,
                duration: 2000,
                gravity: 'top',
                position: 'center',
            }).showToast();
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function getCsrfToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}

document.getElementById('register_form').addEventListener('submit', function (e) {
    e.preventDefault();

    const password = this.password.value;
    const password2 = this.password2.value;

    if (password !== password2) {
        Toastify({
            text: `Las contraseñas deben ser iguales`,
            duration: 2000,
            gravity: 'top',
            position: 'center',
        }).showToast();
        return;
    }

    const formData = new FormData(this);
    formData.append('action', 'register');

    sendUserDataFormData(formData);
});

// Inicio de sesión
document.getElementById('login_form').addEventListener('submit', function (e) {
    e.preventDefault();
    const data = {
        username: this.username.value,
        password: this.password.value
    };
    sendUserData('login', data);
});