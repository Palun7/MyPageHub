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
            text: `${data.error}`,
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