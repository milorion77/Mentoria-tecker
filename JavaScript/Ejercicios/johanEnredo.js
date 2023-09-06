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