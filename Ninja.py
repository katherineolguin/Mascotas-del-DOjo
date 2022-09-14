class Ninja:

    def __init__(self, nombre, apellido, mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota   #se asocia con la linea 6 de main
        self.premio = premio
        self.comida_mascota = comida_mascota


    def caminar(self):
        if   self.mascota.jugar :
            print (f"{self.nombre}:Es hora de pasear con mi gato")
        else:
            print(f"{self.nombre}: El gato no quiere salir")



    def alimentar(self):
        if self.mascota.comer:
            print (f"{self.nombre}:El gato quiere comer")

        else:
            print (f"{self.nombre}:El gato no quiere comer")


    def bañar(self): 
        if self.mascota.ruido:
            print (f"{self.nombre}:hay que bañar al gato")


   
# limpia la mascota del ninja invocando el método de mascota sonido()
