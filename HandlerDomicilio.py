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
                print("\n")
                
                
    def domiciliosPorCriterio(self, criterio):
        domSorteados = []
        for domicilio in self.domicilios: 
            match str(criterio).upper():
                case "DEPARTAMENTO":
                    if domicilio.direccion.departamento == criterio:
                        domSorteados.append(domicilio)
                case "LOCALIDAD":
                    if domicilio.direccion.localidad == criterio:
                        print(str(domicilio.direccion))
                case "CALLE":
                    if domicilio.direccion.calle == criterio:
                        print(str(domicilio.direccion))
                case "NRO":
                    if domicilio.direccion.nro == criterio:
                        print(str(domicilio.direccion))
                case "APARTAMENTO":
                    if domicilio.direccion.apartamento == criterio:
                        print(str(domicilio.direccion))
                case "PADRON":
                    if domicilio.direccion.padron == criterio:
                        print(str(domicilio.direccion))
                case "RUTA":
                    if domicilio.direccion.ruta == criterio:
                        print(str(domicilio.direccion))
                case "KM":
                    if domicilio.direccion.km == criterio:
                        print(str(domicilio.direccion))
                case "LETRA":
                    if domicilio.direccion.letra == criterio:
                        print(str(domicilio.direccion))
                case "BARRIO":
                    if domicilio.direccion.barrio == criterio:
                        print(str(domicilio.direccion))
                case _:
                    print("Caso no válido")
        
        if len(domSorteados) != 0:
            for domicilio in domSorteados:
                print(str(domicilio))
        else: 
            print("No hay domicilios con el criterio establecido.\n")
        