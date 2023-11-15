class DatosPersona: 
    def __init__(self, CI, name, surname, age):
        self.CI = CI
        self.name = name
        self.surname = surname
        self.age = age
        
    def __str__(self) -> str:
        return f"Cédula: {self.CI} \nNombre: {self.name} \nApellido: {self.surname} \nEdad: {self.age}"