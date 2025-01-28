document.getElementById('appointment-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const doctor = document.getElementById('doctor').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    const reason = document.getElementById('reason').value;

    // Simple form validation (optional)
    if (name && email && phone && doctor && date && time && reason) {
        alert('Appointment booked successfully!\n\n' +
              `Name: ${name}\n` +
              `Email: ${email}\n` +
              `Phone: ${phone}\n` +
              `Doctor: ${doctor}\n` +
              `Date: ${date}\n` +
              `Time: ${time}\n` +
              `Reason: ${reason}`);
        // Here you would typically send the form data to a server
    } else {
        alert('Please fill in all fields.');
    }
});
