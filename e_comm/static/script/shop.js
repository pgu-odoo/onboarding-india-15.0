document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('button').forEach(button => {  // get all elements with button tag, or class
        button.onclick = () => {
            const request = new XMLHttpRequest();  // exchange data with a web server
            request.open('POST', `/${button.id}`);  // open(method, url, async)
            request.onload = () => {  // onload event occurs when an object has been loaded
                const response = request.responseText;  // returns the text received from a server following a request being sent.
                // console.log("response", response)
                document.getElementById('count').innerHTML = response;
            }; 
            request.send();  // Sends the request to the server
        };
    });
});

document.getElementById('clc').addEventListener('click', () => {
    window.open('/homepage', '_self')
});

