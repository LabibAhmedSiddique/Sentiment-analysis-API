document.addEventListener('DOMContentLoaded', function() {
    const analyzeForm = document.getElementById('analyze-form');
    analyzeForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const text = document.getElementById('text').value;
        if (!text) {
            alert('Please enter some text!!!!!!');
            return;
        }
        
        const payload = {
            text: text
        };
        
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            displayResult(data.sentiment);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
    
    function displayResult(sentiment) {
        const resultContainer = document.getElementById('result-container');
        resultContainer.textContent = 'Sentiment: ' + sentiment;
        resultContainer.style.display = 'block';
    }
});