document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#get-involved-form');
  const submitBtn = document.querySelector('#submit-btn');
  const messageBox = document.querySelector('#form-message');

  if (!form) return;

  form.addEventListener('submit', (e) => {
      e.preventDefault();

      // Simple form validation
      const name = form.querySelector('input[name="name"]').value.trim();
      const email = form.querySelector('input[name="email"]').value.trim();

      if (!name || !email) {
          messageBox.textContent = "Please fill out all required fields.";
          messageBox.style.color = "red";
          return;
      }

      // Optional: AJAX submission (placeholder)
      messageBox.textContent = "Submitting...";
      messageBox.style.color = "green";

      setTimeout(() => {
          messageBox.textContent = "Thank you for getting involved!";
          form.reset();
      }, 1000);
  });
});
