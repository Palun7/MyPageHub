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
                option.value = categoria.id;
                option.textContent = categoria.nombre;
                categoriaSelect.appendChild(option);
                option.addEventListener('select', ()=> {
                    // Cargar subcategorías
                    data.sub_categorias.forEach(subCategoria => {
                        const option = document.createElement('option');
                        option.value = subCategoria.id;
                        option.textContent = subCategoria.sub_categoria;
                        subCategoriaSelect.appendChild(option);
                    });
                })
            });

        })
        .catch(error => console.error("Error cargando datos:", error));
});

document.getElementById('pagehub_form').addEventListener('submit', async (e) => {
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
            window.location.href = '/pagehub/';
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

document.addEventListener("DOMContentLoaded", function () {
    const categoriaSelect = document.getElementById("categoria");
    const subCategoriaSelect = document.getElementById("sub_categoria");

    categoriaSelect.addEventListener("change", function () {
        const categoriaId = this.value;
        // Vaciar subcategorías anteriores
        subCategoriaSelect.innerHTML = '<option class="option">Sub Categoría</option>';

        if (categoriaId) {
            fetch(`/pagehub/subcategorias/${encodeURIComponent(categoriaId)}/`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(sub => {
                        const option = document.createElement("option");
                        option.value = sub.id;
                        option.textContent = sub.nombre;
                        subCategoriaSelect.appendChild(option);
                    });
                });
        }
    });
});