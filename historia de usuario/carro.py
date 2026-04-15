class Carro:
    def __init__(self,placa,modelo,color,fecha_s,fecha_l):
        self.placa = placa
        self.modelo = modelo
        self.color = color
        self.fecha_s = fecha_s
        self.fecha_l = fecha_l
    
    def get_placa(self):
        return self.placa
    
    def get_modelo(self):
        return self.modelo
    
    def get_color(self):
        return self.color
    
    def get_fecha_s(self):
        return self.fecha_s
    
    def get_fecha_l(self):
        return self.fecha_l
    
    def __str__(self):
        return f"Placa : {self.placa} - Modelo : {self.modelo} - Color : {self.color} - Fecha de salida: {self.fecha_s} - Fecha limite {self.fecha_l}"