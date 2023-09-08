console.log("============Ejercicio 1 ====================");

// Función para crear un arreglo y llenarlo con múltiplos de un número
function llenarArreglo(tamano, numero) {
  let arreglo = [];
  for (let i = 1; i <= tamano; i++) {
    arreglo.push(i * numero);
  }
  return arreglo;
}

// Función para mostrar los elementos de un arreglo
function mostrarArreglo(arreglo) {
  console.log("Contenido del arreglo:");
  for (let i = 0; i < arreglo.length; i++) {
    console.log(arreglo[i]);
  }
}

// Valores instanciados en variables
const tamanoArreglo = 5;
const numeroMultiplo = 3; // Por ejemplo, para generar múltiplos de 3

// Llenar el arreglo y mostrarlo
const miArreglo = llenarArreglo(tamanoArreglo, numeroMultiplo);
mostrarArreglo(miArreglo);

console.log("============Ejercicio 1.2 ====================");

function calcularNota(notas) {
  let notaMasBaja = notas[0]; // Suponemos que la primera nota es la más baja inicialmente

  for (let i = 1; i < notas.length; i++) {
    if (notas[i] < notaMasBaja) {
      notaMasBaja = notas[i]; // Actualizamos la nota más baja si encontramos una nota más baja
    }
  }

  return notaMasBaja;
}

// Ejemplo de uso
let notas = [20, 15, 12, 11, 8, 4, 1];
let notaBaja = calcularNota(notas);
console.log("La nota más baja es: " + notaBaja);

console.log("============Ejercicio 2 ====================");

const a = [1, 9, 4, 25, 16];

// Crear un objeto iterador
const iterador = a[Symbol.iterator]();

// Iterar manualmente usando next()
let resultado = iterador.next();

while (!resultado.done) {
    console.log(resultado); // Imprimir el resultado completo
    resultado = iterador.next(); // Obtener el siguiente valor
}
console.log(resultado); // Imprimir el resultado final


console.log("============Ejercicio 3 ====================");


const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

//promt
rl.question('Ingresa un número entero: ', (numero) => {
  // Convierte la entrada del usuario a un número entero
  numero = parseInt(numero);

  // Verifica si el número ingresado es un entero válido
  if (!isNaN(numero)) {
    // Itera desde 1 hasta el número ingresado
    for (let asterisco = 1; asterisco <= numero; asterisco++) {
      // Crea una cadena de asteriscos con la longitud actual
      const linea = '*'.repeat(asterisco);
      console.log(linea);
    }
  } else {
    console.log('Debes ingresar un número entero válido.');
  }

  rl.close();
});

console.log("============Ejercicio 3.1 While, for  ====================");


function calcularEdad(año, mes, dia) {
  const hoy = new Date();
  const nacimiento = new Date(año, mes - 1, dia); // Restamos 1 a mes para que sea el índice correcto (enero es 0, febrero es 1, etc.)
  
  // Calculamos la diferencia en milisegundos entre las dos fechas
  const diferenciaEnMilisegundos = hoy - nacimiento;

  // Convertimos la diferencia en milisegundos a años
  const milisegundosEnUnAño = 1000 * 60 * 60 * 24 * 365.25; // Aproximadamente 365.25 días en un año, considerando años bisiestos
  const edad = diferenciaEnMilisegundos / milisegundosEnUnAño;

  console.log(`Usted tiene ${edad.toFixed(1)} años`);
}

// Ejemplo de uso
calcularEdad(1996, 10, 7); // Reemplaza estos valores con tu fecha de nacimiento

function edad(año,mes,dia){
  const hoy = new Date();
  console.log(hoy)
  const nacimiento = new Date(año,mes,dia)
  console.log(nacimiento)
  const edad = (((((((hoy - nacimiento)/100)/60)/60)/24)/30)/12)


console.log(`Usted tiene ${edad} años`)

}

