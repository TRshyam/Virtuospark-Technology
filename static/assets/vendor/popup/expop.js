function showPopup(message) {
    // Create a container for the popup
    var popupContainer = $('<div/>', {
        class: 'popup-container'
    });

    // Create the actual popup with the message
    var popup = $('<div/>', {
        text: message,
        class: 'popup'
    });

    // Append the popup to the container
    popupContainer.append(popup);

    // Append the container to the body
    $('body').append(popupContainer);

    // Adjust the position of the popup container to the right-down side
    var windowHeight = $(window).height();
    var windowWidth = $(window).width();
    var popupHeight = popupContainer.outerHeight();
    var popupWidth = popupContainer.outerWidth();

    popupContainer.css({
        'bottom': '10px', // Adjust this value as needed
        'right': '10px',  // Adjust this value as needed
        'position': 'fixed',
        'background': 'linear-gradient(to bottom, rgba(255,255,255,0.9) 0%, rgba(255,255,255,0.7) 50%, rgba(255,255,255,0.9) 100%)',  // Gradient background
        'border': '1px solid #ccc',  // Border color
        'border-radius': '15px',  // Rounded corners
        '-webkit-box-shadow': '0px 3px 8px rgba(0, 0, 0, 0.47)',   // Drop shadow on Chrome
        'padding': '50px',  // Padding
        'font-size': '18px',  // Font size
        'color': '#333',  // Text color
        'z-index': '9999',
        'box-shadow': '0 0 10px rgba(0, 0, 0, 0.2)'  // Box shadow for a glassy effect
    });

    // Remove the popup container after a few seconds (e.g., 5 seconds)
    setTimeout(function () {
        popupContainer.remove();
    }, 5000);
}



        // Submit form using AJAX to handle the response
        $('#statusMessage').submit(function (event) {
            event.preventDefault();
            
            // Use AJAX to submit the form data
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function (response) {
                    // Assuming 'response' contains the response from your server
                    if (response === 'OK') {
                        // Show the popup with the success message
                        showPopup('Successfully Registered');
                    }
                    else {
                        showPopup('Invalid or Already Registered');
                    }
                }
            });
        });

