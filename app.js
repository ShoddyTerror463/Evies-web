const buyButtons = document.querySelectorAll('.buy-button');
const modal = document.getElementById('myModal');
const span = document.getElementsByClassName('close')[0];
const form = document.querySelector('form');

buyButtons.forEach(button => {
  button.addEventListener('click', () => {
    modal.style.display = 'block';
    button.classList.add('rotate');
  });
});

span.addEventListener('click', () => {
  modal.style.display = 'none';
});

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  alert(`Thank you ${name} for your purchase! We'll send your confirmation to ${email}.`);
  modal.style.display = 'none';
});
