// Your existing JavaScript code remains here

const addCustomerForm = document.getElementById('addCustomerForm');
const openFormBtn = document.getElementById('openFormBtn');
const closeFormBtn = document.getElementById('closeForm');
const customerForm = document.getElementById('customerForm');

openFormBtn.addEventListener('click', () => {
  addCustomerForm.style.display = 'block';
});

closeFormBtn.addEventListener('click', () => {
  addCustomerForm.style.display = 'none';
});

customerForm.addEventListener('submit', (e) => {
  e.preventDefault();
  // Get customer details from the form
  const customerName = document.getElementById('customerName').value;
  const customerEmail = document.getElementById('customerEmail').value;
  const customerPhone = document.getElementById('customerPhone').value;

  // Perform validation and save customer logic here

  // For demonstration purposes, just log the customer details
  console.log('Customer Name:', customerName);
  console.log('Customer Email:', customerEmail);
  console.log('Customer Phone:', customerPhone);

  // Close the form after saving
  addCustomerForm.style.display = 'none';
});