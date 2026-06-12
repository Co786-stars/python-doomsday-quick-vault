<script>
// Simple --> check  running or not
console.log("✅ JS file is attached and running!");
alert("✅ JS file is attached and running!");


// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission

    // Get form values
    const fullname = document.getElementById("fullname").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const gender = document.querySelector('input[name="gender"]:checked');
    const interests = document.querySelectorAll('input[name="interests"]:checked');
    const country = document.getElementById("country").value;
    const message = document.getElementById("message").value.trim();

    // Validation checks
    if (fullname.length < 3) {
      alert("Full Name must be at least 3 characters long.");
      return;
    }

    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!email.match(emailPattern)) {
      alert("Please enter a valid email address.");
      return;
    }

    if (password.length < 6) {
      alert("Password must be at least 6 characters long.");
      return;
    }

    if (!gender) {
      alert("Please select your gender.");
      return;
    }

    if (interests.length === 0) {
      alert("Please select at least one interest.");
      return;
    }

    if (country === "") {
      alert("Please select your country.");
      return;
    }

    // If everything is valid
    alert("Form submitted successfully!\n\n" +
          "Name: " + fullname + "\n" +
          "Email: " + email + "\n" +
          "Gender: " + gender.value + "\n" +
          "Interests: " + Array.from(interests).map(i => i.value).join(", ") + "\n" +
          "Country: " + country + "\n" +
          "Message: " + message);

    // You can send data to server here using fetch/AJAX
    // Example:
    // fetch("/submit", {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    //   body: JSON.stringify({ fullname, email, password, gender: gender.value, interests: Array.from(interests).map(i => i.value), country, message })
    // }).then(res => res.json()).then(data => console.log(data));
  });
});
</script>
