import pymongo
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
        
    def addPersona(self, datosPersona, uri, db, col):
        # self.personas.append(datosPersona)
        try: 
            cliente=pymongo.MongoClient(uri, serverSelectionTimeoutMS=1000)
            database = cliente[db]
            colection = database[col]
            # idPersona = colection.insertOne(datosPersona)
            idPersona = colection.insert_one(datosPersona)
            print("Agregada persona con id: ", idPersona.inserted_id)
        except Exception as e:
            print(f"Ocurrió una excepción: {e}")
        
    def printPersonas(self):
        for persona in self.personas:
            print(persona)
            print("\n")
            
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
