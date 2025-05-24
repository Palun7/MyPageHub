const foto_sub = document.querySelector('.foto-sub-categoria');
const foto_cat = document.querySelector('.foto-categoria-titulo');


foto_cat.addEventListener('click', () => {
    foto_cat.classList.toggle('scale-13');
})

foto_sub.addEventListener('click', () => {
    foto_sub.classList.toggle('scale-13');
})