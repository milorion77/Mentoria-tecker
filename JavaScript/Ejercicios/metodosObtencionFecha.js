
//METODOS DE OBTENCION DE FECHA! 😎😎😎😎

const FechaDioy = new Date();
const nuevaFecha = new Date();

console.log("obtener el año")
console.log(FechaDioy.getFullYear()); // 2023

// 
console.log("Obtener el mes")
console.log(FechaDioy.getMonth() + 1); // 9

// 
console.log("Obtener el día")
console.log(FechaDioy.getDate()); // 4

// Obtener la hora
console.log("Obtener la hora")
console.log(FechaDioy.getHours()); // 12

// 
console.log("Obtener los minutos")
console.log(FechaDioy.getMinutes()); // 00

// 
console.log("Obtener los segundos")
console.log(FechaDioy.getSeconds()); // 00

// Obtener los milisegundos
console.log("Obtener los milisegundos")
console.log(FechaDioy.getMilliseconds()); // 000

// 
console.log("Obtener el día de la semana")
console.log(FechaDioy.getDay()); // 0

// Obtener el día del año
console.log("Obtener el día del año")
console.log(FechaDioy.getDate()); // 244

// Obtener la semana del año
console.log("Obtener la semana del año")
function getWeek(date) {
  const FechaDioycopia = new Date(date);
  FechaDioycopia.setHours(0, 0, 0, 0);
  FechaDioycopia.setDate(FechaDioycopia.getDate() + 4 - (FechaDioycopia.getDay() || 7));
  const PrincipioYear = new Date(FechaDioycopia.getFullYear(), 0, 1);
  return Math.ceil(((FechaDioycopia - PrincipioYear) / 86400000 + 1) / 7); // milisegundos  86400000
}
console.log(getWeek(FechaDioy)); // 36

// Obtener el mes del año
console.log("Obtener el mes del año")
console.log(FechaDioy.getMonth()); // 8

// 
console.log("Obtener el año bisiesto")
function isLeapYear(año) {
  return (año % 4 === 0 && año % 100 !== 0) || (año % 400 === 0);
}
console.log(isLeapYear(FechaDioy.getFullYear())); // false

// Obtener la hora local
console.log("Obtener la hora local")
console.log(FechaDioy.toLocaleTimeString()); // 12:00:00

// Obtener la fecha local
console.log("Obtener la fecha local")
console.log(FechaDioy.toLocaleDateString()); // 04/09/2023

// Obtener la fecha en formato UTC
console.log("Obtener la fecha en formato UTC")
console.log(FechaDioy.toUTCString()); // Sun, 04 Sep 2023 12:00:00 GMT

// Obtener la fecha en formato ISO 8601
console.log("Obtener la fecha en formato ISO 860")
console.log(FechaDioy.toISOString()); // 2023-09-04T12:00:00.000Z

// 
console.log("Obtener la diferencia entre dos fechas")
const date1 = new Date("2023-09-03");
const date2 = new Date("2023-09-04");
console.log(date2 - date1); // 86400000

// 
console.log("Agregar un número de días a una fecha")
const dateAdd = new Date("2023-09-03");
dateAdd.setDate(dateAdd.getDate() + 1);
console.log(dateAdd); // 2023-09-04

// 
console.log("Restar un número de días a una fecha")
const dateSubtract = new Date("2023-09-04");
dateSubtract.setDate(dateSubtract.getDate() - 1);
console.log(dateSubtract); // 2023-09-03
