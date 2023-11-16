class Direccion: 
    def __init__(self, departamento, localidad, calle, nro, apartamento, padron, ruta, km, letra, barrio):
        self.departamento = departamento
        self.localidad = localidad
        self.calle = calle
        self.nro = nro
        self.apartamento = apartamento
        self.padron = padron
        self.ruta = ruta
        self.km = km 
        self.letra = letra
        self.barrio = barrio
        
    def __str__(self) -> str: 
        text = ""
        if self.departamento != "0": 
            text = "Departamento: " + self.departamento + "\n"
        if self.localidad != "0":
            text = text + "Localidad: " + self.localidad + "\n"
        if self.calle != "0":
            text = text + "Calle: " + self.calle +"\n"
        if self.nro != "0":
            text = text + "Número de puerta: " + self.nro +"\n"
        if self.apartamento != "0":
            text = text + "Número de apartamento: " + self.apartamento +"\n"
        if self.padron != "0":
            text = text + "Padrón: " + self.padron +"\n"
        if self.ruta != "0":
            text = text + "Ruta: " + self.ruta +"\n"
        if self.km != "0":
            text = text + "Km: " + self.km +"\n"
        if self.letra != "0":
            text = text + "Letra: " + self.letra +"\n"
        if self.barrio != "0":
            text = text + "Barrio: " + self.barrio +"\n"
        
        return text