##BD 
#pip install pymongo
import pymongo
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_TIMEOUT = 10000
#MONGO_URI = "mongodb://{}:{}/".format(MONGO_HOST, MONGO_PORT)
MONGO_URI = "mongodb+srv://ElDeLaBarba:4YQSc2HHQvjBj892@cluster0.o1jktdl.mongodb.net/"
MONGO_BD = "NoSQL"
MONGO_COL_DIRECCION = "Direcciones"
MONGO_COL_DOMICILIO = "Domicilios"
MONGO_COL_PERSONA = "Personas"


try:
    client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT)
    client.server_info()
    print("Conection success ")
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTimeout:
    print("Timeout exception")
except pymongo.errors.ConnectionFailure as errorConnecting:
    print("Connection failed")

from DatosPersona import DatosPersona
from Direccion import Direccion
from Domicilio import Domicilio
from HandlerPersona import HandlerPersona
from HandlerDomicilio import HandlerDomicilio

hper = HandlerPersona()
hdom = HandlerDomicilio()


def main():
    exit = False
    print("=============================================")
    print("================¡Bienvenido!=================")
    try:
        while exit == False:
            print("=============================================")
            print("     1-Agregar Persona")
            print("     2-Ver Personas")
            print("     3-Agregar Domicilio")
            print("     4-Ver todos los domicilios")
            print("     5-Consultar Domicilio")
            print("     6-Obtener domicilios por Criterio")
            print("     0-Salir")
            print("=============================================")
            opt = input("Selecione una opción: ")
            print("\n")
            print("=============================================")
            match str(opt):
                case "1":
                    agregarPersona()
                case "2":
                    hper.printPersonas(MONGO_URI, MONGO_BD, MONGO_COL_PERSONA)
                case "3":
                    agregarDomicilio()
                case "4":
                    hdom.printDomicilios()
                case "5":
                    consultarDomicilio()
                case "6":
                    domiciliosPorCriterio()
                case "0": 
                    exit = True
                case _:
                    print("Opción inválida. Reintente.")
    except EOFError as e:
        print(end="")
    


def agregarPersona():
    print("Ingrese los siguientes datos: ")
    #crear persona
    CI = int(input("Cédula: "))
    name = input("Nombre: ")
    surname = input("Apellido: ")
    age = int(input("Edad: "))
    # datosPersona = DatosPersona(CI, name, surname, age)
    datosPersona = {
        "CI": CI,
        "name": name,
        "surname": surname,
        "age": age
    }
    print(str(datosPersona))
    hper.addPersona(datosPersona, MONGO_URI, MONGO_BD, MONGO_COL_PERSONA)

def agregarDomicilio():
    print("Ingrese los siguientes datos: ")
    CI = input("Cédula de la persona: ")
    # persona = hper.findPersona(CI)
    print("Ingrese los siguientes datos de dirección (si no corresponde, ingrese 0): ")
    departamento = input("Departamento: ")
    localidad = input("Localidad: ")
    calle = input("Calle: ")
    nro = input("Nro. de puerta: ")
    apartamento = input("Nro. de apartamento: ")
    padron = input("Padron: ") 
    ruta = input("Ruta: ")
    km = input("Km: ")
    letra = input("Letra: ")
    barrio = input("Barrio: ")
    
    # direccion = Direccion(departamento, localidad, calle, nro, apartamento, padron, ruta, km, letra, barrio)
    # domicilio = Domicilio(hdom.giveDomicilioID(), persona, direccion)
    direccion = {
        "departamento": departamento,
        "localidad": localidad,
        "calle": calle,
        "nro": nro,
        "apartamento": apartamento,
        "padron": padron,
        "ruta": ruta,
        "km": km,
        "letra": letra,
        "barrio": barrio
    }
    hdom.addDomicilio(MONGO_URI, MONGO_BD, MONGO_COL_DOMICILIO, CI, direccion)

def consultarDomicilio():
    CI = input("Ingrese la cédula del usuario: ")
    hdom.consultarDomicilio(MONGO_URI, MONGO_BD, MONGO_COL_DOMICILIO, CI)
    
def domiciliosPorCriterio():
    # opt = 1
    # criterias = ["", "", ""]
    # while opt != 0:
    #     print("Criterios: ")
    #     print("     1-Departamento\n")
    #     print("     2-Localidad\n")
    #     print("     3-Barrio\n")
    #     opt = int(input("¿Por qué campo quiere filtrar (0 si no quiere agregar más filtros)?: "))
    #     if opt > 0 and opt < 4:
    #         criterias[opt-1] = input("Escriba el criterio por el que filtrar: ")
    #     elif opt >= 4:
    #         print("Campo no reconocido. Reintente.")
    print("Ingrese los criterios de interés (0 en caso contrario): ")
    departamento = input("Departamento: ")
    localidad = input("Localidad: ")
    barrio = input("Barrio: ")

    criterias = {
        "direccion.departamento": departamento ,
        "direccion.localidad": localidad ,
        "direccion.barrio": barrio
    }

    if departamento == '0':
        del criterias["direccion.departamento"]
    if localidad == '0':
        del criterias["direccion.localidad"]
    if barrio == '0':
        del criterias["direccion.barrio"]

    hdom.domiciliosPorCriterio(MONGO_URI, MONGO_BD, MONGO_COL_DOMICILIO, criterias)

if __name__ == "__main__":
    main()