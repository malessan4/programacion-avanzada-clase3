"""
Ejercicio 4
Desarrolla una clase Canción con los siguientes atributos:
.titulo: una variable String que guarda el titulo de una cancion
.autor: una variable String que guarda el autor de una cancion
Con los siguientes metodos
.Cancion(String, String): Constructor que recibe como parametros el titulo y el autor
de la cancion (por este orden)
.get_titulo(): devuelve el titulo de la cancion
.get_autor(): devuelve el autor de la cancion
.set_titulo(String): Establece el titulo de la cancion
.set_autor(String): Establece el autor de la cancion

    
"""

class Persona():
    def __init__(self, nombre):
        self.__nombre = nombre


    def __str__(self):
        return self.__nombre
    
class Cancion ():
    
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        
        if not isinstance(autor, Persona):
                
                raise ValueError("El autor debe ser una instancia de la clase Persona.")
        
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor
        
autor1 = Persona ("Robert Plant")       
cancion = Cancion ("21 palms", autor1)

print (cancion.get_autor ())
print (cancion.get_titulo())
    
    
