import DatosPersona


class HandlerPersona:
    personas = []
    _instance = None
    
    def __new__(cls):
        if cls._instance is None: 
            print("Creando HandlerPersona")
            cls._instance = super(HandlerPersona, cls).__new__(cls)
            cls.personas = []
        return cls._instance
        
    def addPersona(self, datosPersona):
        self.personas.append(datosPersona)
        
    def printPersonas(self):
        for persona in self.personas:
            print(persona)
            print("\n")
            
    def findPersona(self, CI) -> DatosPersona:
        encontrada = None
        for persona in self.personas: 
            if CI in persona == CI:
                encontrada = persona
        return encontrada                
