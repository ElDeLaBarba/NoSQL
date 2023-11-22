import pymongo
from DatosPersona import DatosPersona

class HandlerPersona:
    personas = []
    _instance = None
    
    def __new__(cls):
        if cls._instance is None: 
            print("Creando HandlerPersona")
            cls._instance = super(HandlerPersona, cls).__new__(cls)
            cls.personas = []
        return cls._instance
        
    def addPersona(self, datosPersona, uri, db, col):
        # self.personas.append(datosPersona)
        try: 
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            # idPersona = colection.insertOne(datosPersona)
            filter_criteria_pers = {"CI": datosPersona['CI']}
            
            existePersona = colection.find_one(filter_criteria_pers)
            if existePersona == None:
                idPersona = colection.insert_one(datosPersona)
                print("Agregada persona con id: ", idPersona.inserted_id)
            else:
                print("Error 401: La persona ya existe.")
        except Exception as e:
            print(f"Ocurrió una excepción: {e}")
        
    def printPersonas(self, uri, db, col):
        #for persona in self.personas:
         #   print(persona)
          #  print("\n")
        try:
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            CI = 0
            name = ''
            surname = ''
            age = 0
        
            personasBD = list(colection.find({}))
            
            for persona in personasBD: 
                CI = str(persona).split("'CI': ")[1].split(", 'name':")[0]
                name = str(persona).split("'name': '")[1].split("', 'surname':")[0]
                surname = str(persona).split("'surname': '")[1].split("', 'age':")[0]
                age = str(persona).split("'age': ")[1].split("}")[0]
                
                datosPersona = DatosPersona(CI, name, surname, age)
                print(datosPersona)
                
        except Exception as e:
            print(f"Ocurrió una excepción: {e}")
            
    # def findPersona(self, CI) -> DatosPersona:
    def findPersona(self, CI):
            cliente=pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1000)
            database = cliente["NoSQL"]
            colection = database["Personas"]
            criterio_busqueda = {"CI": int(CI)}
            print("ci: ", CI)
            documento = colection.find_one(criterio_busqueda)
            if documento:
                print("\nUsuario "+CI+" encontrado\n")
                return True
