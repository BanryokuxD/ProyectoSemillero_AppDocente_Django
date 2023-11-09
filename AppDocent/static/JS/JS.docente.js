// Función para ocultar todos los detalles de las tarjetas
function hideAllDetails() {
    const detailsElements = document.querySelectorAll('.details');
    detailsElements.forEach(function(details) {
        details.style.display = 'none';
    });
}

// Función para mostrar los detalles de la tarjeta seleccionada
function toggleDetails(detailsId) {
    hideAllDetails(); // Oculta todos los detalles primero
    const details = document.getElementById(detailsId);
    details.style.display = 'block'; // Muestra solo los detalles de la tarjeta clicada
}

// Ocultar todos los detalles al cargar la página
window.addEventListener('load', hideAllDetails);
