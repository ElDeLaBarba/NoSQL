import pymongo
from HandlerPersona import HandlerPersona
from Direccion import Direccion
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
            if exist_persona != None:
                domicilio = {
                    "CI": CI,
                    "direccion": direcc
                }
                id_domicilio = colection.insert_one(domicilio)
                print("Agregado Domicilio con id: ", id_domicilio.inserted_id)
                return json.dumps({'message': 'Domicilio agregado correctamente'}), 200
            else:
                print("Error 402: No existe una persona con la cédula aportada.")
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
        
        
    def printDomicilios(self, uri, db, col):
        try:
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            results = list(colection.find())
            for result in results: 
                domicilio_info = result["direccion"]
                CI = result["CI"]
                    
                dom = self.bdToDom(domicilio_info)
                    
                print("=============================================\n")
                print(f"Domicilio: \n\n{dom}")
                print(f"CI de la persona asociada: {CI}")
                print("=============================================")
        except:
            print("error intentando imprimir domicilios")



            
    def consultarDomicilio(self, uri, db, col, CI):
        # for domicilio in self.domicilios:
        #     if domicilio.datos_Persona.CI == CI:
        #         print(str(domicilio.direccion))
        #         print("\n")
        try: 
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            
            pers = database["Personas"]
        
            
            filter_criteria = {"CI": CI}
            filter_criteria_pers = {"CI": int(CI)}
            
            persona = pers.find_one(filter_criteria_pers)
            
            
            if persona != None:
                results = colection.find(filter_criteria)
                for result in results:
                    if "direccion" in result:
                        domicilio_info = result["direccion"]
                        
                        dir = self.bdToDom(domicilio_info)
                            
                        print("=============================================\n")
                        print(f"Domicilio para CI {CI}: \n{str(dir)}")
                        print("=============================================")
                    else:
                        print(f"No se encontró información de domicilio para CI {CI}")
            else: 
                print("Error 402: No existe una persona con la cédula aportada.")
                return json.dumps({'error': 'No existe una persona con la cédula proporcionada'}), 402
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
                    CI = result["CI"]
                    
                    dom = self.bdToDom(domicilio_info)
                    
                    print("=============================================\n")
                    print(f"Domicilio: \n\n{dom}")
                    print(f"CI de la persona asociada: {CI}")
                    print("=============================================")
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
        

    def bdToDom(self, domicilio_info) -> Direccion: 
        departamento = str(domicilio_info).split("'departamento': '")[1].split("', 'localidad':")[0]
        localidad = str(domicilio_info).split("'localidad': '")[1].split("', 'calle':")[0]
        calle = str(domicilio_info).split("'calle': '")[1].split("', 'nro':")[0]
        nro = str(domicilio_info).split("'nro': '")[1].split("', 'apartamento':")[0]
        apartamento = str(domicilio_info).split("'apartamento': '")[1].split("', 'padron':")[0]
        padron = str(domicilio_info).split("'padron': '")[1].split("', 'ruta':")[0]
        ruta = str(domicilio_info).split("'ruta': '")[1].split("', 'km':")[0]
        km = str(domicilio_info).split("'km': '")[1].split("', 'letra':")[0]
        letra = str(domicilio_info).split("'letra': '")[1].split("', 'barrio':")[0]
        barrio = str(domicilio_info).split("'barrio': '")[1].split("'}")[0]
                    
                    
        dir = Direccion(departamento, localidad, calle, nro, apartamento, padron, ruta, km, letra, barrio)
        
        return dir