from Ninja import Ninja
from Mascota import Mascota
from Golosina import Golosina


Blanquita = Mascota ("Blanquita" , "Gato" , 54, 89)
Cristobal = Ninja ("Cristobal", "ceballos", Blanquita, "premio", "Atun")

print("-----------------")
print(f"Ninja {Cristobal.nombre} tiene un {Cristobal.mascota.tipo} que se llama {Blanquita.nombre}")

print("-----------------")

Blanquita.estado_mascota()

print("-----------------")

Cristobal.caminar()
Blanquita.jugar()

Blanquita.estado_mascota()

print("-----------------")

Blanquita.jugar()

Blanquita.dormir()

Blanquita.estado_mascota()
print("-----------------")


Blanquita.comer()
Cristobal.alimentar()

Blanquita.estado_mascota()
print("-----------------")


Blanquita.ruido()
Cristobal.bañar()
Blanquita.estado_mascota()

print("-----------------")
Snack = Golosina ("felix" ,"bajo en sodio", "alta", "buena")
Pouch = Golosina ("Master Cat" ,"normal", "alta", "mala")
Golosina.total_golosinas_dia()

Pouch.estadonutricional_golosina()
Snack.estadonutricional_golosina()







