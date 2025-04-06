"""

Ejercicio 3

Define una clase Linea con dos atributos: _punto_a y _punto_b. Son dos puntos
por los que pasa la linea en un espacio de dos dimensiones.

La clase dispondra de los siguientes métodos:
.Linea (Punto, Punto) Constructor que recibe como parámetros dos objetos
de la clase  Punto, que son utilizados para inicializar los atributos
.mueve_derecha(float) Desplaza la línea a ña derecha la distancia que se
indique.
.mueve_izquierda(float) Desplaza la linea a la izquierda la distancia que se
indique.
.mueve_arriba(float) Desplaza la linea hacia arriba la distancia que se indique
.mueve_abajo(float) Desplaza la linea hacia abajo la distancia que se indique


"""
from Ejercicio_2 import Punto
from Ejercicio_2 import punto1, punto2

class Linea():
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def __str__(self):
        return f"Linea: ({self._punto_a}, {self._punto_b})"

    def get_punto_a(self):
        return self._punto_a
    
    def get_punto_b(self):
        return self._punto_b
        
    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia

    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia

    def mueve_abajo(self, distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia

linea1 = Linea(punto1,punto2)
print(linea1)


