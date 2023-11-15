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
        if self.domicilios.count() == 0:
            return 0
        else:
            return self.domicilios[-1].id+1
        
    