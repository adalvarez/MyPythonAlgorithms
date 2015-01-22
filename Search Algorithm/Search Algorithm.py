# -*- coding: utf-8 -*-

# 2015 @chapitro shares

'''
Algoritmo de búsqueda:
La utilización de diversas estructuras de datos en programación en variada
pero sin duda las listas (eventualmente vectores o matrices) son de las principales
en cuanto a uso. Este algoritmo de búsqueda satisface esa necesidad a una escala
más grande que simplemente hacer comparaciones entre dos elementos entre listas.
Por el contrario, gracias a la ayuda de una librería llamada textblob se puede
responder a la necesidad de buscar una o más palabras dentro de un texto, todo basado
en la estructura de datos mencionada (listas).
Aquí puede entrar el ingenio del programador para satisfacer otras necesidades
por ejemplo el utilizar un directorio y si este contiene archivos en texto plano
poder hacer búsqueda a partir de una o más palabras (también números, siglas, entre otros).

'''


from textblob import TextBlob

def process():
     tagSearch = input("Busqueda:  > ").decode("latin-1")# Elementos por buscar.

     listTagSearch = TextBlob(tagSearch.lower()).words

     #__ Parte opcional para rellenar la base de información a la cual se recurrirá al proceso de búsqueda.

     baseInformacion = []

     bandera = True
     while bandera :
          info = input("Ingrese informacion base para busqueda o 'end' para salir. > ").decode("latin-1")
          if info == 'end':
               bandera = False
          else:
               baseInformacion += [ [info, TextBlob(info.lower()).words] ]

     #__
               
     for index, valor in enumerate(baseInformacion):
          count = 0
          for j in valor[1]:
               if j in listTagSearch:
                    count += 1
          baseInformacion[index] += [count]

     listSeleccionText = []

     for i in baseInformacion:
          if i[-1] > 0:
               listSeleccionText += [i]
     
     # Ordenamiento:
     valores = []
     count = 0
     listSORT = []

     while listSeleccionText != []:

          for i in listSeleccionText:
               valores += [ i[-1] ]
               
          if max(valores) == listSeleccionText [count] [-1] :
               listSORT += [ listSeleccionText[count][0] ]
               listSeleccionText = listSeleccionText[:count] + listSeleccionText [count+1:]
               count = 0
               valores = []
          else:
               count +=1

     print "Proceso terminado, a continuacion se presenta las coincidencias con orden prioritario: "

     for h, i in enumerate(listSORT):
          print str(h+1) + ' ___'
          print i



##########

# TextBlob tiene muchos usos, en este caso utiliza un texto y lo descompone en partes ya sea palabras, numeros, etc. Omite espacios, comas, puntos, y otros caracteres, es una libería que nos
#  ayuda a descomponer un texto de manera sencilla ya que si se desarrollara manualmente el algoritmo se debería tener muchas consideraciones según el lenguaje.


# Demostrción de funcionamiento:

'''

>>> process()
Busqueda:  > "Minecraft un juego comercial"

Ingrese informacion base para busqueda o 'end' para salir. > "El jugador es libre de desplazarse por el terreno, conformado por distintos biomas, entre los que se encuentran desiertos, sabanas, selvas,
océanos, llanuras, tundras, etc."

Ingrese informacion base para busqueda o 'end' para salir. > "En su lanzamiento comercial el juego tenía dos modos principales: supervivencia, en el que los jugadores deben adquirir recursos para
mantener su salud y hambre; y creativo, donde los jugadores tienen acceso ilimitado a los recursos del juego, la habilidad de volar y no requieren mantener su salud y hambre."

Ingrese informacion base para busqueda o 'end' para salir. > "En Minecraft los jugadores pueden realizar construcciones mediante cubos con texturas tridimensionales, igualmente pueden explorar
el entorno, recolectar recursos y crear objetos con distintas utilidades, combatir criaturas (llamadas mobs en inglés) u otros jugadores, etc."

Ingrese informacion base para busqueda o 'end' para salir. > 'end'

Proceso terminado, a continuacion se presenta las coincidencias con orden prioritario: 
1 ___
En su lanzamiento comercial el juego tenía dos modos principales: supervivencia, en el que los jugadores deben adquirir recursos para mantener su salud y hambre; y creativo, donde los jugadores
tienen acceso ilimitado a los recursos del juego, la habilidad de volar y no requieren mantener su salud y hambre.
2 ___
En Minecraft los jugadores pueden realizar construcciones mediante cubos con texturas tridimensionales, igualmente pueden explorar el entorno, recolectar recursos y crear objetos con distintas
utilidades, combatir criaturas (llamadas mobs en inglés) u otros jugadores, etc.

'''
# Aclarar nada más el proceso interno:  El primer texto ingresado tiene 0 coincidencias, segundo texto tiene 2 coincidencias, y el tercer texto tiene 1 coincidencia,
# por tanto el orden es: segundo texto, tercer texto. Sólo aparece los textos con coincidencias.


# GNU GPL v3
