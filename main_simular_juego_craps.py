from estado_juego import EstadoJuego
from constantes_funciones import *


resultado_primer_lanzamiento = tirar_dados()
print(f'PUNTO EN EL PRIMER LANZAMIENTO: {resultado_primer_lanzamiento}')
estado_juego: EstadoJuego

estado_juego = estado_juego_primer_lanzamiento(resultado_primer_lanzamiento)
print(estado_juego)

resultado_juego(estado_juego, resultado_primer_lanzamiento)
