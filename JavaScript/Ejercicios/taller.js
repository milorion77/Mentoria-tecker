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

