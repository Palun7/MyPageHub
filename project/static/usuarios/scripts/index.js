const resgistrarse = document.getElementById('registrarse');
const login_form = document.getElementById('login_form');
const register_form = document.getElementById('register_form');
const iniciar_sesion = document.getElementById('iniciar_sesion');
const login = document.getElementById('login');
const registrar = document.getElementById('registrar');

function boton_registrarse(boton) {
    boton.addEventListener('click', ()=>{

        login.classList.add('left-500');
        login.classList.add('opacity-0');
        registrar.classList.remove('right500');
        registrar.classList.remove('opacity-0');
        login_form.reset();

    });
}

function boton_login(boton){
    boton.addEventListener('click', ()=>{

        login.classList.remove('left-500');
        login.classList.remove('opacity-0');
        registrar.classList.add('right500');
        registrar.classList.add('opacity-0');
        register_form.reset();

    });
}

document.addEventListener('DOMContentLoaded', ()=>{
    login.classList.remove('opacity-0');
})

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
                    background: "linear-gradient(to right,rgb(147, 33, 254),rgb(178, 95, 255))",
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
                    background: "linear-gradient(to right,rgb(248, 63, 63),rgb(249, 121, 121))",
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
                    background: "linear-gradient(to right,rgb(0, 174, 12), rgba(10, 194, 0, 0.764))",
                    color: "black"
                },
            }).showToast();
            setTimeout(()=>{
                location.reload();
            },2000);
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

boton_registrarse(resgistrarse);

boton_login(iniciar_sesion);

function mostrarPreview() {
  const input = document.getElementById('foto_perfil');
  const preview = document.getElementById('preview');

  if (input.files.length > 0) {
    const file = input.files[0];
    const reader = new FileReader();
    reader.onload = function(e) {
      preview.src = e.target.result;
      preview.classList.remove('opacity-0');
    };
    reader.readAsDataURL(file);
  } else {
    preview.classList.add('opacity-0');
    preview.src = '';
  }
};