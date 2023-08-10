/*Ejercicio 1
Crear una función mkDate que reciba los parámetros day, month, year y retorne un objeto con dicha información.
Agregarle además un método printDate que imprima por consola la fecha en formato dia/mes/año. */

function mkDate(day, month, year) {
    return {
      day: day,
      month: month,
      year: year,
      printDate: function() {
        console.log(`${this.day}/${this.month}/${this.year}`);
      }
    };
  }
  
  const fecha = mkDate(10, 8, 2023);
  fecha.printDate(); 

/* Ejercicio 2
Modificar el objeto que retorna la función y agregar el método isValid. isValid debe validar que los tres campos estén seteados y que 1 <= day <= 31, 1 <= month <= 12, 1970 <= year < 3000. printDate deberá imprimir fecha inválida si la fecha no es válida. */  
function createDate(day, month, year) {
function printDate() {
        if (isValid()) {
            console.log(`Fecha: ${day}/${month}/${year}`);
        } else {
            console.log("Fecha inválida");
        }
    }

    function isValid() {
        if (!(1 <= day && day <= 31 && 1 <= month && month <= 12 && 1970 <= year && year < 3000)) {
            return false;
        }
        return true;
    }

    return {
        day,
        month,
        year,
        printDate,
        isValid
    };
}

// Ejemplo de uso:
const date = createDate(15, 8, 2023);
date.printDate();  // Imprimirá "Fecha: 15/8/2023"
console.log(date.isValid());  // Imprimirá true

const invalidDate = createDate(40, 13, 2025);
invalidDate.printDate();  // Imprimirá "Fecha inválida"
console.log(invalidDate.isValid());  // Imprimirá false

/*Ejercicio 3
Seguir modificando el objeto... agregar los métodos isBefore e isAfter que reciban otro objeto date como parámetro y retornen un boolean indicando si la fecha pasada como parámetro es anterior y posterior respectivamente. */

function createDate(day, month, year) {
    function printDate() {
        if (isValid()) {
            console.log(`Fecha: ${day}/${month}/${year}`);
        } else {
            console.log("Fecha inválida");
        }
    }

    function isValid() {
        return 1 <= day && day <= 31 && 1 <= month && month <= 12 && 1970 <= year && year < 3000;
    }

    function isBefore(otherDate) {
        return (
            year < otherDate.year ||
            (year === otherDate.year && month < otherDate.month) ||
            (year === otherDate.year && month === otherDate.month && day < otherDate.day)
        );
    }

    function isAfter(otherDate) {
        return (
            year > otherDate.year ||
            (year === otherDate.year && month > otherDate.month) ||
            (year === otherDate.year && month === otherDate.month && day > otherDate.day)
        );
    }

    return {
        day,
        month,
        year,
        printDate,
        isValid,
        isBefore,
        isAfter
    };
}

// Ejemplo de uso:
const date1 = createDate(15, 8, 2023);
const date2 = createDate(20, 8, 2023);

date1.printDate();  // Imprimirá "Fecha: 15/8/2023"
console.log(date1.isBefore(date2));  // Imprimirá true
console.log(date1.isAfter(date2));   // Imprimirá false

console.log(date2.isBefore(date1));  // Imprimirá false
console.log(date2.isAfter(date1));   // Imprimirá true


/* Ejercicio 5
Crea un array para albergar al menos 10 números enteros cualquiera , luego rellena el array (o crealo ya con los valores). El ejercicio trata de crear a partir de este array otros dos uno con los números pares y otro con los impares. No debes usar bucles, usa el método del array qe creas más apropiado.
No debes usar bucles, mira el método más apropiado para crear un array a partir de otro.
Un número es par si al dividirlo por 2 el resto es 0 (num%2 es 0) */

const numeros = [10, 23, 44, 57, 68, 71, 82, 95, 106, 119];

const numerosPares = numeros.filter(num => num % 2 === 0);
const numerosImpares = numeros.filter(num => num % 2 !== 0);

console.log("Números originales:", numeros);
console.log("Números pares:", numerosPares);
console.log("Números impares:", numerosImpares);


/*Ejercicio 6
Crea un array de al menos 10 elementos para guardar números enteros. Usa un método para obtener la suma de los números pares y la de los números impares.
Se trata de reducir el array a un número obtenido como suma de los pares en un caso y delos impares en el otro. */

const numeros1 = [10, 23, 44, 57, 68, 71, 82, 95, 106, 119];

const sumaPares = numeros1.reduce((acumulador, num) => {
    if (num % 2 === 0) {
        return acumulador + num;
    }
    return acumulador;
}, 0);

const sumaImpares = numeros1.reduce((acumulador, num) => {
    if (num % 2 !== 0) {
        return acumulador + num;
    }
    return acumulador;
}, 0);

console.log("Números originales:", numeros);
console.log("Suma de números pares:", sumaPares);
console.log("Suma de números impares:", sumaImpares);



/*Ejercicio 7
Vamos a crear un objeto sencillo que se usa para guardar información sobre las calificaciones de un alumno. El curso contiene tres materias: Ingles, programación y HTM, y el objeto contendrá el nombre del alumno y la calificación en cada una de ellas. El script imprimirá el nombre y la media de sus calificaciones
Por ejemplo, guardar las calificaciones de un alumno de nombre Juan, Inglés: 9, programacion: 8, HTML: 7. Sacará Nota media de Juan 8 */



/*Ejercicio 8
Define un objeto, mediante una expresión, que tenga dos propiedades: precio y descuento y un método neto. El método calculará el precio con el descuento aplicado. Los valores se pedirán por teclado
Por ejemplo objeto vestido, precio 400 y descuento 10. El método devolverá como resultado 360 (400 - 10*400/100). */

/*Ejercicio 10
Realiza un ejercicio en js que pida una cadena de texto y la muestre poniendo el signo – entre cada carácter sin usar el método replace. */

/*Ejercicio 11
Pedimos una cadena de texto que sabemos que puede contener paréntesis. Realiza un script que extraiga la cadena que se encuentra entre los paréntesis.
Ej: Si escribimoe el texto “Hola (que) tal” se mostrará “que”. Si no existe el signo “(“ mostrará una cadena vacía y si existe el signo “(“pero no el signo “)” mostrará desde el primer paréntesis hasta el final. */

/*Ejercicio 12
Realiza un script que pida una cadena de texto y la devuelva al revés.
Ej: si tecleo “hola que tal” deberá mostrar “lat euq aloh”. */

/*Ejercicio 13
Realiza un script que pida un texto e indique si es un palíndromo.
Ejemplo de palíndromo: “Dabale arroz a la zorra el abad”.
Palíndromo, 1. m. Palabra o frase que se lee igual de izquierda a derecha, que de derecha a izquierda; p. ej., anilina; dábale arroz a la zorra el abad. */

/*Ejercicio 14
Realizar acciones de carrusel con eventos */
