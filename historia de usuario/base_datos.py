class Base_datos:
    def __init__(self):
        self.base_datos = []

    def guardar_carros(self,base_dato):
        self.base_datos.append(base_dato)

    def guardar_chofer(self,obj_chofer):
        info = [obj_chofer.get_nombre(),obj_chofer.get_documento(),obj_chofer.get_licencia()]
        self.base_datos.append(info)
    
    def ver_datos(self):
        if not self.base_datos:
            print (f"No hay datos")
        else:
            for info in self.base_datos:
                print(info)