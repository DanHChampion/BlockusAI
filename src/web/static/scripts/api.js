function handleSubmit() {
  const form = document.getElementById('form');
  const formData = new FormData(form);
  const data = Object.fromEntries(formData);
  const url = '/move';
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  };

  fetch(url, options)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });
}