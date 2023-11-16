class HandlerDomicilio: 
    domicilios = []
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creando HnadlerDomicilio")
            cls._instance = super(HandlerDomicilio, cls).__new__(cls)
            cls.domicilios = []
        return cls._instance
    
    def addDomicilio(self, domicilio):
        self.domicilios.append(domicilio)
        
    def giveDomicilioID(self) -> int:
        if len(self.domicilios) == 0:
            return 0
        else:
            return self.domicilios[-1].id+1
        
    def printDomicilios(self):
        for domicilio in self.domicilios: 
            #print(domicilio.datos_persona)
            print(str(domicilio.datos_persona) + "\n\nDirección: \n\n" + str(domicilio.direccion))
            
    def consultarDomicilio(self, CI):
        for domicilio in self.domicilios:
            if domicilio.datos_persona.ci == CI:
                print(str(domicilio.direccion))
                
                

        