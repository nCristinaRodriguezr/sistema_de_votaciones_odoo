// static/src/js/voting_page.js

// Función que actualiza la lista de candidatos según el proceso de votación seleccionado
function updateCandidates() {
    var votacionId = document.getElementById('votacion').value;
    var candidatoSelect = document.getElementById('candidato');
    var photoContainer = document.getElementById('candidate-photo-container');
    var photoImg = document.getElementById('candidate-photo');

    // Ocultar la foto del candidato cuando se cambia el proceso de votación
    photoContainer.style.display = 'none';
    photoImg.src = '';

    // Limpiar las opciones anteriores y añadir un placeholder en el campo de candidatos
    candidatoSelect.innerHTML = ''; 
    let placeholderOption = document.createElement('option');
    placeholderOption.textContent = 'Elige un candidato';
    placeholderOption.disabled = true;
    placeholderOption.selected = true;
    candidatoSelect.appendChild(placeholderOption);

    // Realizar la solicitud al servidor para obtener los candidatos del proceso de votación seleccionado
    fetch(`/get_candidates?votacion_id=${votacionId}`)
        .then(response => response.json())
        .then(data => {
            // Recorrer y agregar cada candidato a la lista desplegable
            data.forEach(candidato => {
                let option = document.createElement('option');
                option.value = candidato.id;
                option.setAttribute('data-photo', `data:image/png;base64,${candidato.image}`);
                option.textContent = candidato.name;
                candidatoSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error al obtener candidatos:', error));
}


// Mostrar la foto del candidato seleccionado
function showCandidatePhoto() {
    var candidatoSelect = document.getElementById('candidato');
    var photoContainer = document.getElementById('candidate-photo-container');
    var photoImg = document.getElementById('candidate-photo');

    var selectedOption = candidatoSelect.options[candidatoSelect.selectedIndex];
    var photoUrl = selectedOption.getAttribute('data-photo');

    // Mostrar la foto si está disponible
    if (photoUrl) {
        photoImg.src = photoUrl;
        photoContainer.style.display = 'block';
    } else {
        photoContainer.style.display = 'none';
    }
}
