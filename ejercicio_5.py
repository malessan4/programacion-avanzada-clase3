
"""● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
servicios: getters y setters, método para leer la información y método para mostrar la
información.
● Este último método mostrará la información del libro con este formato:
Título: Introduction to Java Programming 3a. edición
Autor: Liang, Y. Daniel
ISBN: 0-13-031997-X
Prentice-Hall, New Jersey (USA)
viernes 16 de noviembre de 2001
784 páginas"""

from Ejercicio_4 import Persona

class Libro () :

    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, lugar, fecha_de_edicion ):
        self.__titulo = titulo
        self.__autor = autor
        self.__ISBN = ISBN
        self.__paginas = paginas
        self.__edicion= edicion 
        self.__editorial = editorial
        self.__lugar = lugar
        self.__fecha_de_edicion = fecha_de_edicion 
        
        if not isinstance(autor, Persona):
            
            raise ValueError("El autor debe ser una instancia de la clase Persona.")
             
    
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ISBN(self):
        return self.__ISBN

    def get_paginas(self):
        return self.__paginas

    def get_edicion(self):
        return self.__edicion

    def get_editorial(self):
        return self.__editorial

    def get_lugar(self):
        return self.__lugar

    def get_fecha_de_edicion(self):
        return self.__fecha_de_edicion

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def set_paginas(self, paginas):
        self.__paginas = paginas

    def set_edicion(self, edicion):
        self.__edicion = edicion

    def set_editorial(self, editorial):
        self.__editorial = editorial

    def set_lugar(self, lugar):
        self.__lugar = lugar

    def set_fecha_de_edicion(self, fecha_de_edicion):
        self.__fecha_de_edicion = fecha_de_edicion
        
    def mostrar_informacion (self) :
        return f"Título: {self.__titulo}\n" \
               f"Autor: {self.__autor}\n" \
               f"ISBN: {self.__ISBN}\n" \
               f"{self.__editorial}, {self.__lugar}\n" \
               f"{self.__fecha_de_edicion}\n" \
               f"{self.__paginas} páginas"
               

autor = Persona("Mary Shelley") 
libro = Libro("Frankenstein", autor, "978-0-14-143947-1", 280, 1, "Editorial Valdemar", "Madrid, España", "1818")

print(libro.mostrar_informacion())