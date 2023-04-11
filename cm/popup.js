function fetchMessage() {
    fetch('http://localhost:5000/message')
        .then(response => response.text())
        .then(text => {
            document.getElementById('message').textContent = text;
        });
}

document.addEventListener('DOMContentLoaded', fetchMessage);

