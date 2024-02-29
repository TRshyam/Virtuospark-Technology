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
        'background-color': '#e03a3c',
        'border': '1px solid #e03a3c',  // Border color
        'border-radius': '15px',  // Rounded corners
        'padding': '40px',  // Padding
        'font-size': '18px',  // Font size
        'color': '#333',  // Text color
        'z-index': '9999',
    });

    // Remove the popup container after a few seconds (e.g., 5 seconds)
    setTimeout(function () {
        popupContainer.remove();
    }, 5000);
}



        // Submit form using AJAX to handle the response
        $('#subscribeForm').submit(function (event) {
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
                        showPopup('Successfully subscribed');
                    }
                    else {
                        showPopup('Already  subscribed');
                    }
                }
            });
        });

