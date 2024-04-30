document.getElementById('predictBtn').addEventListener('click', function() {
    // Obtendo os valores de entrada do usuário
    const temperature = parseFloat(document.getElementById('temperature').value);
    const humidity = parseFloat(document.getElementById('humidity').value);
    const pollutants = parseFloat(document.getElementById('pollutants').value);

    // Enviando os valores para o backend (substitua 'predict' pela rota do seu backend)
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            temperature,
            humidity,
            pollutants
        })
    })
    .then(response => response.json())
    .then(data => {
        // Exibindo o resultado da previsão
        document.getElementById('predictionResult').innerText = `Predicted Air Quality: ${data.prediction}`;
    })
    .catch(error => console.error('Error:', error));
});