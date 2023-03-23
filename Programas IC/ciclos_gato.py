import random

# Definimos la función para imprimir el tablero
def imprimir_tablero(tablero):
    print(tablero[0] + '|' + tablero[1] + '|' + tablero[2])
    print('-+-+-')
    print(tablero[3] + '|' + tablero[4] + '|' + tablero[5])
    print('-+-+-')
    print(tablero[6] + '|' + tablero[7] + '|' + tablero[8])

# Definimos la función para verificar si alguien ha ganado
def alguien_gano(tablero, jugador):
    if (
        (tablero[0] == jugador and tablero[1] == jugador and tablero[2] == jugador) or
        (tablero[3] == jugador and tablero[4] == jugador and tablero[5] == jugador) or
        (tablero[6] == jugador and tablero[7] == jugador and tablero[8] == jugador) or
        (tablero[0] == jugador and tablero[3] == jugador and tablero[6] == jugador) or
        (tablero[1] == jugador and tablero[4] == jugador and tablero[7] == jugador) or
        (tablero[2] == jugador and tablero[5] == jugador and tablero[8] == jugador) or
        (tablero[0] == jugador and tablero[4] == jugador and tablero[8] == jugador) or
        (tablero[2] == jugador and tablero[4] == jugador and tablero[6] == jugador)
    ):
        return True
    else:
        return False

# Definimos la función para que la computadora elija una posición aleatoria en el tablero
def elegir_posicion_computadora(tablero):
    posicion = random.randint(0, 8)
    while tablero[posicion] != ' ':
        posicion = random.randint(0, 8)
    return posicion

# Definimos la función principal del juego
def jugar_gato():
    # Creamos el tablero
    tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    # Definimos los jugadores
    jugador1 = 'X'
    jugador2 = 'O'

    # Definimos el jugador que inicia
    turno = jugador1

    # Imprimimos el tablero vacío
    imprimir_tablero(tablero)

    # Iniciamos el juego
    while True:
        if turno == jugador1:
            # Pedimos la posición al jugador 1
            posicion = int(input('Jugador ' + turno + ', elige una posición (1-9): ')) - 1

            # Verificamos si la posición está disponible
            if tablero[posicion] == ' ':
                tablero[posicion] = turno
            else:
                print('Esa posición ya está ocupada. Elige otra.')
                continue

        else:
            # La computadora elige una posición aleatoria
            print('Turno de la computadora...')
            posicion = elegir_posicion_computadora(tablero)
            tablero[posicion] = turno
            print('La computadora ha elegido la posición', posicion)

# Imprimimos el tablero actualizado
        imprimir_tablero(tablero)

        # Verificamos si alguien ganó
        if alguien_gano(tablero, turno):
            print('¡El jugador ' + turno + ' ha ganado!')
            break

        # Verificamos si el tablero está lleno (empate)
        if ' ' not in tablero:
            print('¡Empate!')
            break
        # Cambiamos de turno
        if turno == jugador1:
            turno = jugador2
        else:
            turno = jugador1
            
# Ejecutamos la función principal
jugar_gato()
