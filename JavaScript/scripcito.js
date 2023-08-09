const targetElement = document.getElementById('ejem');

// Evento: click que me cambia el color a naranjado
targetElement.addEventListener('click', () => {
  targetElement.style.backgroundColor = 'orange';
  console.log("haciendo un solo clic")
});

// Evento: mouseover
targetElement.addEventListener('mouseover', () => {
  targetElement.style.backgroundColor = 'green';
  console
});

// Evento: mouseout
targetElement.addEventListener('mouseout', () => {
  targetElement.style.backgroundColor = 'lightblue';
});

// Evento: mousedown
targetElement.addEventListener('mousedown', () => {
  targetElement.style.backgroundColor = 'red';
});

// Evento: mouseup
targetElement.addEventListener('mouseup', () => {
  targetElement.style.backgroundColor = 'blue';
});
