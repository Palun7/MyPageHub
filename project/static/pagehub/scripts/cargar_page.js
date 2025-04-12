document.addEventListener('DOMContentLoaded', () => {
    fetch('/pagehub/cargar_page/?json=true')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const categoriaSelect = document.getElementById('categoria');
            const subCategoriaSelect = document.getElementById('sub_categoria');

            // Cargar categorías
            data.categorias.forEach(categoria => {
                const option = document.createElement('option');
                option.value = categoria[0];
                option.textContent = categoria[1];
                categoriaSelect.appendChild(option);
            });

            // Cargar subcategorías
            data.sub_categorias.forEach(subCategoria => {
                const option = document.createElement('option');
                option.value = subCategoria.id;
                option.textContent = subCategoria.sub_categoria;
                subCategoriaSelect.appendChild(option);
            });

        })
        .catch(error => console.error("Error cargando datos:", error));
});

document.getElementById('pagehub-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
        const response = await fetch('/pagehub/cargar_page/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });

        if (!response.ok) throw new Error(`Error: ${response.status}`);

        const data = await response.json();
        alert(data.message);
        e.target.reset();  // Limpia el formulario después de cargar
    } catch (error) {
        console.error("Error al enviar:", error);
        alert("Hubo un error al cargar la página.");
    }
});