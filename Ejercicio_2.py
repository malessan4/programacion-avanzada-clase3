"""

Ejercicio 2
Crear la clase Punto con dos atributos x e y (ambos numéricos),
con el correspondiente constructor que recibe ambos valores

-Definir metodos tales como:
eje_x
eje_Y

-impresión (método que devuelve en representacion de string ambos valores)
-opuesto (método que devuelve el punto opuesto -es decir con los atributos negativos-)
-cualquier otro método que considere importante


"""


class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'

    def eje_x (self):
        return self.x

    def eje_y (self):
        return self.y

    def impresion (self):
        print(f"({self.x}, {self.y})")

    def opuesto (self):
        return Punto(-self.x, -self.y)

def ingresar_punto():
    x = int(input("Ingrese un numero para la coordenada x: "))
    y = int(input("Ingrese un número para la coordenada y: "))
    return Punto(x,y)





punto1 = Punto(3,5)
punto1.impresion()
punto1.opuesto().impresion()

punto2 = ingresar_punto()
punto2.impresion()
punto2.opuesto().impresion()