import pymongo
from HandlerPersona import HandlerPersona
import json

hper = HandlerPersona()

class HandlerDomicilio: 
    domicilios = []
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creando HnadlerDomicilio")
            cls._instance = super(HandlerDomicilio, cls).__new__(cls)
            cls.domicilios = []
        return cls._instance
    
    
    def addDomicilio(self, uri, db, col, CI, direcc):
        # self.domicilios.append(domicilio)
        print("\nIngresando domicilio\n")
        try: 
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            exist_persona = hper.findPersona(CI)
            print("existe persona: ", exist_persona)
            if exist_persona:
                domicilio = {
                    "CI": CI,
                    "direccion": direcc
                }
                id_domicilio = colection.insert_one(domicilio)
                print("Agregado Domicilio con id: ", id_domicilio.inserted_id)
                return json.dumps({'message': 'Domicilio agregado correctamente'}), 200
            else:
                return json.dumps({'error': 'No existe una persona con la cédula proporcionada'}), 402
        except pymongo.errors.ServerSelectionTimeoutError:
            return json.dumps({'error': 'Error de conexión con la base de datos'}), 500
        except Exception as e:
            return json.dumps({'error': str(e)}), 500
        
        
    def giveDomicilioID(self) -> int:
        if len(self.domicilios) == 0:
            return 0
        else:
            return self.domicilios[-1].id+1
        
        
    def printDomicilios(self):
        for domicilio in self.domicilios: 
            print(str(domicilio.datos_Persona) + "\n\nDirección: \n\n" + str(domicilio.direccion))

            
    def consultarDomicilio(self, uri, db, col, CI):
        # for domicilio in self.domicilios:
        #     if domicilio.datos_Persona.CI == CI:
        #         print(str(domicilio.direccion))
        #         print("\n")
        try: 
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            filter_criteria = {"CI": CI}
            results = colection.find(filter_criteria)
            for result in results:
                if "direccion" in result:
                    domicilio_info = result["direccion"]
                    print(f"Domicilio para CI {CI}: {domicilio_info}")
                else:
                    print(f"No se encontró información de domicilio para CI {CI}")
        except:
            print("error intentando imprimir domicilios")
                
                
    def domiciliosPorCriterio(self, uri, db, col, criterias):
        try: 
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            print("criterias", criterias)
            results = colection.find(criterias)
            for result in results:
                if result:
                    domicilio_info = result["direccion"]
                    print(f"Domicilio: {domicilio_info}")
                else:
                    print(f"No se encontró información de domicilio para los criterios", criterias)
        except:
            print("error intentando imprimir domicilios")

        # domSorteados = self.domicilios.copy()
        # for domicilio in self.domicilios: 
        #     if criterio[0] != "":
        #         if domicilio.direccion.departamento != criterio[0]:
        #             domSorteados.remove(domicilio)
            
        #     if criterio[1] != "" and domicilio in domSorteados:
        #         if domicilio.direccion.localidad != criterio[1]:
        #             domSorteados.remove(domicilio)
                    
        #     if criterio[2] != "":
        #         if domicilio.direccion.barrio != criterio[2] and domicilio in domSorteados:
        #             domSorteados.remove(domicilio)
        
        # if len(domSorteados) != 0:
        #     for domicilio in domSorteados:
        #         print(str(domicilio))
        # else: 
        #     print("No hay domicilios con el criterio establecido.\n")
        