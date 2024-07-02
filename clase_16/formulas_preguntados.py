
import pygame
import csv #csv.reader: Permite leer un archivo CSV línea por línea y devuelve cada línea como una lista de cadenas.Básicamente, convierte las filas de un archivo CSV en listas de Python

pygame.init()

def guardar_nombre_y_puntaje(puntaje, nombre):
    """
    Guarda el nombre y puntaje en un archivo CSV.
    """
    with open("clase_16/puntajes.csv", "a", newline='') as archivo:
        archivo.writelines(f"{nombre}, {puntaje}")

def mostrar_puntajes(archivo , pantalla):
    """
    Lee los puntajes desde el archivo CSV y los ordena de mayor a menor.

    """
    puntajes = []
    font = pygame.font.SysFont("Arial Narrow", 50)
    with open(archivo, "r") as file:
        reader = csv.reader(file, lineterminator="\n")
        for i in reader:
            nombres = i[0]
            puntaje = int(i[1])
            puntajes.append((nombres, puntaje))
    # Ordenar puntajes de mayor a menor
    puntajes_ordenados = sorted(puntajes, reverse=True)
    txt_puntos1 = font.render(f"{puntajes_ordenados} " , True , (225,225,225))
    pantalla.blit(txt_puntos1 , (10 , 50))
    return puntajes_ordenados
    

def mostrar_preguntas(lista:list ,indice:int , pantalla):
    """
    utilizando el parametro indice marca las preguntas del parametro lista
    return: opciones1 , opciones2 , opciones3 , pregunta_actual
    """
    font = pygame.font.SysFont("Arial Narrow", 50)
    ubicacionrect_a = [0, 300]
    tamaño_rect_a = [335 , 35]
    color_rect_a =(18, 225, 232)
    boton_a = pygame.Rect(ubicacionrect_a, tamaño_rect_a)
    ubicacionrect_b = [0, 350]
    tamaño_rect_b = [335 , 35]
    color_rect_b =(18, 225, 232)
    boton_b = pygame.Rect(ubicacionrect_b, tamaño_rect_b)
    ubicacionrect_c = [0, 400]
    tamaño_rect_c = [335 , 35]
    color_rect_c =(18, 225, 232)
    boton_c = pygame.Rect(ubicacionrect_c, tamaño_rect_c)
    pregunta_actual = font.render(lista[indice]["pregunta"], True, (0, 0, 0))
    opciones1 = font.render(f"a:{lista[indice]["a"]}",True,(0,0,0))
    opciones2 = font.render(f"b:{lista[indice]["b"]}",True,(0,0,0))
    opciones3 = font.render(f"c:{lista[indice]["c"]}",True,(0,0,0))
    pygame.draw.rect(pantalla, color_rect_a , boton_a , border_radius=0)
    pygame.draw.rect(pantalla , color_rect_b , boton_b , border_radius=0)
    pygame.draw.rect(pantalla , color_rect_c , boton_c , border_radius=0)
    pantalla.blit(pregunta_actual, (-5, 10))
    pantalla.blit(opciones1, (0, 300))
    pantalla.blit(opciones2, (0, 350))
    pantalla.blit(opciones3, (0, 400))