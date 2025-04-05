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
    
    def eje_x (self):
        return self.x
    
    def eje_y (self):
        return self.y
    
    def impresion (self):
        print(f'({self.x}, {self.y})')

        
punto = Punto(3,4)

punto.impresion()
