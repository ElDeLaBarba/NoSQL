import pymongo

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
            print(str(domicilio.datos_Persona) + "\n\nDirección: \n\n" + str(domicilio.direccion))

            
    def consultarDomicilio(self, uri, db, col):
        # for domicilio in self.domicilios:
        #     if domicilio.datos_Persona.CI == CI:
        #         print(str(domicilio.direccion))
        #         print("\n")
        try: 
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            for direccion in colection.find():
                print(direccion)
        except:
            print("error intentando imprimir domicilios")
                
                
    def domiciliosPorCriterio(self, criterio):
        domSorteados = self.domicilios.copy()
        for domicilio in self.domicilios: 
            if criterio[0] != "":
                if domicilio.direccion.departamento != criterio[0]:
                    domSorteados.remove(domicilio)
            
            if criterio[1] != "" and domicilio in domSorteados:
                if domicilio.direccion.localidad != criterio[1]:
                    domSorteados.remove(domicilio)
                    
            if criterio[2] != "":
                if domicilio.direccion.barrio != criterio[2] and domicilio in domSorteados:
                    domSorteados.remove(domicilio)
        
        if len(domSorteados) != 0:
            for domicilio in domSorteados:
                print(str(domicilio))
        else: 
            print("No hay domicilios con el criterio establecido.\n")
        