document.addEventListener('DOMContentLoaded', () => {
  const reportCards = document.querySelectorAll('.report-card');

  reportCards.forEach(card => {
      card.addEventListener('click', () => {
          const details = card.querySelector('.report-details');
          if (details) {
              details.classList.toggle('visible');
              if (details.classList.contains('visible')) {
                  details.style.maxHeight = details.scrollHeight + "px";
              } else {
                  details.style.maxHeight = "0";
              }
          }
      });
  });
});
