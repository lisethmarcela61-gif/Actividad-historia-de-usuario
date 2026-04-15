class Chofer :
    def __init__(self,nombre,documento,licencia):
        self.nombre = nombre
        self.documento = documento 
        self.licencia = licencia
    
    def get_nombre(self):
        return self.nombre
    
    def get_documento(self):
        return self.documento
    
    def get_licencia(self):
        return self.licencia

    def __str__(self):
        return f"Nombre : {self.nombre} - Documento : {self.documento} - Licencia : {self.licencia}"