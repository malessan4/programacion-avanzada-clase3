# programacion-avanzada-clase3
Clase 3 - Programación avanzda 1er Cuatri 2025

Alumnos:
Maximiliano Vergot DNI: 35862337
Matias Alessandrello DNI: 36726760


Ejercicio 2:
● Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
constructor que recibe ambos valores.
● Definir métodos tales como:
○ eje_x
○ eje_y
○ impresion (método que devuelve en representación de string ambos valores)
○ opuesto (método que devuelve el punto opuesto -es decir con los atributos
negativos-)
○ Cualquier otro método que considere importante

Ejercicio 3:
Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
pasa la línea en un espacio de dos dimensiones.
La clase dispondrá de los siguientes métodos:
● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
Punto, que son utilizados para inicializar los atributos.
● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.

Ejercicio 4:
Desarrolla una clase Cancion con los siguientes atributos:
● titulo: una variable String que guarda el título de la canción.
● autor: una variable String que guarda el autor de la canción.
Con los siguientes métodos:
● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
canción (por este orden).
● get_titulo(): devuelve el título de la canción.
● get_autor(): devuelve el autor de la canción.
● set_titulo(String): establece el título de la canción.
● set_autor(String): establece el autor de la canción

Ejercicio 5:
● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
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
784 páginas
