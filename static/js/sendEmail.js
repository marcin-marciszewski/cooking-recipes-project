function sendMail(contactForm) {
    emailjs.send("gmail", "cooking", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("Message successfuly sent", response);
        },
        function(error) {
            console.log("FAILED", error);
        });
}

