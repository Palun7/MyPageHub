document.getElementById('sub_categoria_form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
        const response = await fetch('/pagehub/cargar_sub_categoria/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });

        if (!response.ok) throw new Error(`Error: ${response.status}`);

        const data = await response.json();
        Toastify({
            text: `${data.success}`,
            duration: 2000,
            gravity: 'top',
            position: 'center',
            style: {
                background: "rgb(75, 222, 255)",
                color: "rgb(0,0,0)"
            },
        }).showToast();
        setTimeout(() => {
            window.location.href = '/pagehub/cargar_page/';
        }, 2000);
    } catch (error) {
        Toastify({
            text: `Hubo un error al cargar.`,
            duration: 2000,
            gravity: 'top',
            position: 'center',
            style: {
                background: "linear-gradient(to right,rgb(255, 0, 0),rgb(251, 66, 66))",
                color: "rgb(221,221,221)",
            },
        }).showToast();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    fetch('/pagehub/cargar_page/?json=true')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const categoriaSelect = document.getElementById('categoria_principal');

            // Cargar categorías
            data.categorias.forEach(categoria => {
                const option = document.createElement('option');
                option.value = categoria[0];
                option.textContent = categoria[1];
                categoriaSelect.appendChild(option);
                console.log(categoria[0], categoria[1]);
            });

        })
        .catch(error => console.error("Error cargando datos:", error));
});