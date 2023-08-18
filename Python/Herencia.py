"""
Herencia
la herencia nos permite definir una clase que hereda todos
los metodos y propiedades de la otra clase
### La clase Pricipal###
es la clase encargada de heredar, tambien llamada calse base
cualquier clase puede ser una clase principlal
"""

class persona:
    nombre=""
    apellido=""
    edada=0
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def __str__(self):
        return f"el nombre es: {self.nombre} el apellido es {self.apellido} y la edad es {self.edad}"
persona1=persona("juan","perez",23)
print(persona1)

class estudiante(persona):
    pass
estudiante1=estudiante()

class profesor(persona):
    salario=0
    cod_profesor=0
    cod_materia=0
    telefono=0
    def __init__(self, nombre, apellido, edad, salario,cod_profesor,cod_materia,telefono):
        super().__init__(nombre, apellido, edad)
        self.salario = salario
        self.cod_materia = cod_materia
        self.telefono = telefono
        self.cod_profesor

    def Mostrar(self):
        print("El profesor con codigo", self.cod_profesor)
        print("El nombre es ", self.nombre)
        print("El apellido es", self.apellido )
        print("La Edad es", self.edad)
        print("El codigo de la materia es",   )
        print("El salario es ", )
        print("El telefono", )
        print("El ",  )

