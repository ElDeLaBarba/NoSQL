import DatosPersona

class Domicilio:
    def __init__(self, id, datos_Persona, direccion):
        self.id = id
        self.datos_Persona = datos_Persona
        self.direccion = direccion
        
    def __str__(self) -> str:
        return f"{self.datos_Persona}\n\nDirección: \n {self.direccion}"