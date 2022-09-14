from Mascota import Mascota


class Golosina(Mascota): #Estamos diciendo que la clase a heredar es Mascota

    lista_golosinas =[]

    def __init__(self, nombre ,tipo, energía, salud): #Golosina
        super().__init__(nombre ,tipo , energía, salud)    #Mascota #Super() --> para heredar de Golosina
        Golosina.lista_golosinas.append(self)

    @classmethod
    def total_golosinas_dia(cls):
            print("Tu mascota a comido:", len(cls.lista_golosinas), "golosinas")

            for golosina in cls.lista_golosinas:
                print(golosina.nombre)

    def estadonutricional_golosina(self):
        if self.salud == "buena":
            print(f"Le diste {self.nombre} tipo {self.tipo} y le hace bien a tu gato")
        else:
            print(f"ALERTA!!!!!! Le diste {self.nombre} tipo {self.tipo} y es peligroso para tu gato")
