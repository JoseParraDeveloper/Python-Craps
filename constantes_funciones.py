import random as rd
from estado_juego import EstadoJuego

# CONSTANTES QUE REPRESENTAN RESULTADOS IMPORTANTES EN LOS LANZAMIENTOS DE DADOS.
DOS_UNOS = 2
TRES = 3
SIETE = 7
ONCE = 11
DOCE = 12


def tirar_dados():
    dado1 = rd.randint(1, 6)
    dado2 = rd.randint(1, 6)
    resultado = dado1+dado2
    return resultado


def estado_juego_primer_lanzamiento(punto: int):
    estado_juego: EstadoJuego
    if ((punto == SIETE) or (punto == ONCE)):
        estado_juego = EstadoJuego.GANO
    elif ((punto == DOS_UNOS) or (punto == TRES) or (punto == DOCE)):
        estado_juego = EstadoJuego.PERDIO
    else:
        estado_juego = EstadoJuego.CONTINUA
    return estado_juego


def resultado_juego(estado: EstadoJuego, punto: int):
    if(estado == EstadoJuego.GANO):
        print('EL JUGADOR GANO EN EL PRIMER LANZAMIENTO!!')
    elif (estado == EstadoJuego.PERDIO):
        print('EL JUGADOR PERDIO EN EL PRIMER INTENTO....SIGUE INTENTANDOLO!!')
    else:
        while(estado == EstadoJuego.CONTINUA):
            resultado_lanzamiento_posterior = tirar_dados()
            if(resultado_lanzamiento_posterior == punto):
                estado = EstadoJuego.GANO
                print('EL JUGADOR GANO!!')
                print(
                    f'PUNTO EN EL ULTIMO LANZAMIENTO: {resultado_lanzamiento_posterior}')
            elif(resultado_lanzamiento_posterior == SIETE):
                estado = EstadoJuego.PERDIO
                print('EL JUGADOR PERDIO!!')
                print(
                    f'PUNTO EN EL ULTIMO LANZAMIENTO: {resultado_lanzamiento_posterior}')
    return estado
