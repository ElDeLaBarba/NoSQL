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
            
    def findPersona(self, CI) -> DatosPersona:
        encontrada = None
        for persona in self.personas: 
            if persona.CI == CI:
                encontrada = persona
        return encontrada                
