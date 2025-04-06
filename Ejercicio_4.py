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
        self._nombre = nombre
    
    def __str__(self):
        return self.nombre
    
