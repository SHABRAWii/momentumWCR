// script.js
document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('liveCamera');

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
                video.srcObject = stream;
            })
            .catch((error) => {
                console.error('Error accessing camera:', error);
            });
    } else {
        console.error('getUserMedia is not supported');
    }

    function appendUARTMessage(message) {
        const uartMessagesDiv = document.getElementById('uartMessages');
        uartMessagesDiv.innerHTML += `<p>${message}</p>`;
    }

    const uartMessage = 'UART Message: Hello, world!';
    appendUARTMessage(uartMessage);
});
