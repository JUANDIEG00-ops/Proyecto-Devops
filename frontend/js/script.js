document.getElementById('btn-conectar').addEventListener('click', () => {
    // Llamamos al backend en el puerto 5000 que configuraremos en Docker
    fetch('http://localhost:5000/api/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('respuesta').innerText = data.mensaje;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('respuesta').innerText = 'No se pudo conectar con el backend.';
        });
});