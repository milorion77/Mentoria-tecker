// CONST => es una palabra clave que se utiliza para declarar una variable cuyo valor no se espera que cambie después de haber sido inicializado.

const targetElement = document.getElementById('ejem');
// target element => es el elemento que es el objetivo o el destinatario de una acción en un contexto dado.
// document. => se refiere al objeto global Document, que representa el documento HTML cargado en una ventana del navegador.
//getElementById  => es un método proporcionado por el objeto global document
//Este método se utiliza para seleccionar y recuperar un elemento del DOM por su atributo id en este caso es id 'ejem'


targetElement.addEventListener('click', () => {
  //addEventListener ==> es como decirle a tu página web: "Parcero, escucha si algo sucede en este elemento y cuando tin, haz que suceda el tan".
  const currentWidth = parseInt(getComputedStyle(targetElement).width);
  // ParseInt ==>> utiliza para convertir una cadena de texto en un número entero (entero).
  // getComputedStyle ==>  es como preguntar al navegador cómo se ven realmente las cosas en la pantalla después de aplicar todos los estilos

  const newWidth = currentWidth + 10; // Incrementa el tamaño en 10 píxeles

  targetElement.style.width = newWidth + 'px';
  targetElement.style.height = newWidth + 'px';
  
  console.log("Haciendo un solo click para cambiar el tamaño");
});


// Evento mouseover cambia el color a verde cuando el cursor esta encima 
targetElement.addEventListener('mouseover', () => {
  targetElement.style.backgroundColor = 'green';
  console.log("cursor paso encima de la figura y cambia a verde")
});

// Evento: mouseout
targetElement.addEventListener('mouseout', () => {
  targetElement.style.backgroundColor = 'purple';
  console.log("cursor salió de la figura y cambia a morado")
});

// Evento: mousedown
targetElement.addEventListener('mousedown', () => {
  targetElement.style.backgroundColor = 'red';
  console.log("Sostengo el click y cambia a rojo")
});

// Evento: mouseup
targetElement.addEventListener('mouseup', () => {
  targetElement.style.backgroundColor = 'blue';
  console.log("suelto click y pasa a color azul oscuro")
});

// Ejemplo Click
const button = document.getElementById('myButton');
button.addEventListener('click', () => {
  alert('¡Botón clickeado!');
});


// Ejemplo Teclas
const input = document.getElementById('myInput');
input.addEventListener('keydown', (event) => {
  if (event.key === 'a') {
    alert('Tecla "A" presionada');
  } else if (event.key === 's') {
    alert('Tecla "S" presionada');
  }
});

// Ejemplo Submit
const form = document.getElementById('myForm');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  alert('Formulario enviado');
});

// Ejemplo Focus y Blur
const focusInput = document.getElementById('focusInput');
focusInput.addEventListener('focus', () => {
  focusInput.style.backgroundColor = 'yellow';
});
focusInput.addEventListener('blur', () => {
  focusInput.style.backgroundColor = 'white';
});