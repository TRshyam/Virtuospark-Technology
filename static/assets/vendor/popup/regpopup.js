function showPopupMessage(message, type = 'success') {
    // console.log(message+"_____________________");
    var popupMessage = document.querySelector('.popup-message');
    // console.log(popupMessage+"class")
    // console.log(popupMessage+"class")
    // console.log(popupMessage+"class")
    // console.log(popupMessage+"class")
    
    popupMessage.innerHTML = message;
    popupMessage.className = 'popup-message alert-' + type;
    popupMessage.style.display = 'block';

    // Hide the pop-up message after 5 seconds
    setTimeout(function () {
        popupMessage.style.display = 'none';
    }, 3000);
}





function handleSubmit(event, endpoint) {
    event.preventDefault();

    // Fetch data from the form
    var formData = new FormData(event.target);
    // console.log(formData);

    // Make a POST request to the specified endpoint
    fetch(endpoint, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(data => {
        // Log the data in the console if it's not None
        if (data.trim() !== 'None') {
            // console.log(data);
            // console.log(data);
            // console.log(data);
            // console.log(data+"this is data");
            // Display the data in a pop-up message
            // console.log(data,'success');
            // console.log(data,'success');
            // console.log(data,'success');
            // console.log(data,'success');
            // console.log(data,'success');
            showPopupMessage(data, 'success');
        }
    })
    .catch(error => {
        // console.error('Error:', error);
        showPopupMessage('An error occurred during form submission.', 'danger');
    });
}
