document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contact-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        const csrftoken = getCookie('csrftoken');
        const name = document.getElementById("name").value;
        const phone = document.getElementById("phone").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        // Send form data to server
        fetch("/api/contact/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken // Include the CSRF token in the request
            },
            body: JSON.stringify({ name, phone, email, message })
        })
        .then(response => {
            if (response.ok) {
                alert("הטופס נשלח בהצלחה! תודה על הפנייה.");
                document.getElementById("contact-form").reset(); // Clear the form
            } else {
                alert("אירעה שגיאה בשליחת הטופס. אנא נסו שוב.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("אירעה שגיאה בשליחת הטופס. אנא נסו שוב.");
        });
    });

    // Function to get the CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
