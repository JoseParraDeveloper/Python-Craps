from estado_juego import EstadoJuego
from constantes_funciones import *


iteraciones = 100000
numero = 0
contador_ganar = 0
while (numero <= iteraciones):
    resultado_primer_lanzamiento = tirar_dados()
    estado_juego: EstadoJuego
    estado_juego = estado_juego_primer_lanzamiento(
        resultado_primer_lanzamiento)

    resultado = resultado_juego(
        estado_juego, resultado_primer_lanzamiento)
    if(resultado == EstadoJuego.GANO):
        contador_ganar += 1
    numero += 1

print(f'LA PROBABILIDAD DE GANAR ESTIMADA ES: {contador_ganar/iteraciones}')
