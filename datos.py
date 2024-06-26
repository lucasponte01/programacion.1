lista=[{'pregunta': '¿Cuál es la moneda de México?', 'a': 'Peso', 'b': 'Dolar', 'c':'Euro' ,'correcta': 'a'}, 
       {'pregunta': '¿De qué colores es la bandera de Japón?', 'a': 'Azul y Amarilla','b': 'Blanca y roja', 'c':'Celeste y Blanca' ,'correcta': 'b'}, 
       {'pregunta': '¿Cuántos elementos forman la Tabla Periódica?', 'a': '118', 'b': '123', 'c':'125' ,'correcta': 'a'},
       {'pregunta': '¿Quién pintó la Mona Lisa?', 'a': 'Dali', 'b': 'Miguel Angel', 'c':'Leonardo da Vinci' ,'correcta': 'c'},
       {'pregunta': '¿Qué elemento de la tabla periódica tiene como símbolo He?', 'a': 'Hielo', 'b': 'Helio', 'c':'Litio' ,'correcta': 'b'},
       {'pregunta': '¿Qué planeta es el que se encuentra más cerca del Sol?', 'a': 'Mercurio', 'b': 'Marte', 'c':'Jupiter' ,'correcta': 'a'},
       {'pregunta': '¿A cuántos kilómetros equivale una milla?', 'a': '3.6 km.', 'b': '2.6 km.', 'c':'1.6 km.' ,'correcta': 'c'},
       {'pregunta': '¿De dónde es originario el mojito?', 'a': 'Cuba', 'b': 'Puerto Rico', 'c':'El Salvador' ,'correcta': 'a'},
       {'pregunta': '¿Cuántos lados tiene un heptadecágono?', 'a': 'Dieciseis', 'b': 'Diecisete', 'c':'Quince' ,'correcta': 'b'},
       {'pregunta': '¿De dónde sale el aceite de oliva?', 'a': 'aceitunas', 'b': 'girasol', 'c':'maiz' ,'correcta': 'a'},
       {'pregunta': '¿Dónde nació la pizza?', 'a': 'Roma', 'b': 'Venecia', 'c':'Napoles' ,'correcta': 'c'},
       {'pregunta': '¿Cuál es la capital de Kenia?', 'a': 'Luanda', 'b': 'Nairobi', 'c':'El Cairo' ,'correcta': 'b'},
       {'pregunta': '¿Cuántos colores tiene el cubo Rubik?', 'a': '6', 'b': '9', 'c':'4' ,'correcta': 'a'},
       {'pregunta': '¿A qué país pertenece la Isla de Pascua?', 'a': 'Argentina', 'b': 'Chile', 'c':'Brasil' ,'correcta': 'b'},
       {'pregunta': '¿Cuál es el país más grande del mundo?', 'a': 'China', 'b': 'Canada', 'c':'Rusia' ,'correcta': 'c'},
       {'pregunta': '¿Cuál es el lugar más frío de la tierra?', 'a': 'Rusia', 'b': 'Antartida', 'c':'Groenlandia' ,'correcta': 'b'},
       {'pregunta': '¿Cuál es el río más largo del planeta?', 'a': 'Amazonas', 'b': 'Nilo', 'c':'Misisipi' ,'correcta': 'a'}
      ]

# from datos import lista
# import pygame
# import random
# from pygame.locals import *

# pygame.init()
# # Pantalla
# config_pantalla = [1000, 700]
# screen = pygame.display.set_mode(config_pantalla)

# # Botón
# ubicacionrect = [400, 100]
# tamaño_rect = [200, 50]
# color_rect = (251, 255, 0)
# boton1 = pygame.Rect(ubicacionrect[0], ubicacionrect[1], tamaño_rect[0], tamaño_rect[1])

# # Textos
# font = pygame.font.SysFont("Arial Narrow", 50)
# txt_pregunta = font.render("Pregunta", True, (255, 0, 0))
# txt_reiniciar = font.render("Reiniciar", True, (255, 0, 0))

# # Score
# score = 0
# txt_score = font.render(f"Score: {score}", True, (255, 0, 0))

# # Variables para preguntas
# indice_pregunta = 0
# pregunta_actual = font.render(lista[indice_pregunta]["pregunta"], True, (0, 0, 0))
# opciones_actuales = [font.render(opcion, True, (0, 0, 0)) for opcion in lista[indice_pregunta]["pregunta"]]

# pygame.display.set_caption("Preguntados")
# running = True
# while running:
#     # Se verifica si el usuario cerró la ventana
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if boton1.collidepoint(event.pos):
#                 indice_pregunta = (indice_pregunta + 1) % len(lista)
#                 pregunta_actual = font.render(lista[indice_pregunta]["pregunta"], True, (0, 0, 0))
#                 opciones_actuales = [font.render(opcion, True, (0, 0, 0)) for opcion in lista[indice_pregunta]["pregunta"]]
    
#     screen.fill((18, 225, 232))
    
#     pygame.draw.rect(screen, color_rect, boton1, border_radius=10)
#     screen.blit(txt_pregunta, (437, 110))
    
#     # Dibujar pregunta y opciones
#     screen.blit(pregunta_actual, (50, 300))
#     for i, opcion in enumerate(opciones_actuales):
#         screen.blit(opcion, (50, 400 + i * 60))
    
#     pygame.display.flip()

# pygame.quit()