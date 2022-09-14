

class Mascota: 


    def __init__(self,nombre ,tipo , energía, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.energía = energía
        self.salud = salud

    
    def jugar(self):

        if self.energía > 50:
            self.salud += 5
            self.energía -= 5

            # print(f"La salud de {self.nombre} aumento a: {self.salud} y su energia dismuyo: {self.energía}")
    
            print(f"{self.nombre}: Es hora de perseguir aves!")
            
        else:
            print(f"{self.nombre}: No quiero salir")
           



    def dormir(self):
        if self.energía < 50:
            self.energía += 25
            self.salud += 5
            print(f"{self.nombre}: A dormir!")

            # print(f"La salud de {self.nombre} aumento a: {self.salud} y su energia aumento: {self.energía}")

        else:
            print(f"{self.nombre}: Quiero atencion!")




    def comer(self):
        if self.energía > 50:
            self.energía += 5
            self.salud += 10

            print(f"{self.nombre}: Tengo hambre")

            # print(f"La salud de {self.nombre} aumento a: {self.salud} y su energia aumento: {self.energía}")
        else:
            print(f"{self.nombre}: Quiero atencion")


    def ruido(self): 
        if self.salud > 100:
            print(f"{self.nombre}: Miaaaaaaauuu")

    # - imprime el sonido que produce la mascota
    def estado_mascota(self):
        
        print(f"Energia de {self.nombre} es de: {self.energía}")
        print(f"Salud de {self.nombre} es de: {self.salud}")