
def generar_ruta_caballo(posicion_inicial):
    """Genera la ruta del caballo dentro de un tablero de ajedrez a partir de la posición inicial"""
    x, y = posicion_inicial
    ruta_caballo = [(x, y)]
    
    movimientos_caballo = [
        (2, 1), (1, 2), (-1, 2), (-2, 1), 
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    for _ in range(63):
        movimientos_validos = []
        for dx, dy in movimientos_caballo:
            nueva_x, nueva_y = x + dx, y + dy
            if 0 <= nueva_x < 8 and 0 <= nueva_y < 8 and (nueva_x, nueva_y) not in ruta_caballo:
                movimientos_validos.append((nueva_x, nueva_y))
        if not movimientos_validos:
            break
        x, y = movimientos_validos[0]
        ruta_caballo.append((x, y))
        
    return ruta_caballo


ANCHO_VENTANA = 400
ALTO_VENTANA = 400
TAMANIO_CASILLA = 50
COLOR_FONDO = (255, 255, 255)
COLOR_CASILLA_BLANCA = (255, 255, 204)
COLOR_CASILLA_NEGRA = (51, 153, 255)
COLOR_CAMINO = (255, 0, 0)

def imprimir_tablero(ruta_caballo):
    """Imprime el tablero de ajedrez con la ruta del caballo"""
    tablero = [[0 for _ in range(8)] for _ in range(8)]
    for i, (x, y) in enumerate(ruta_caballo):
        tablero[x][y] = i + 1
        
    print("   0  1  2  3  4  5  6  7 ")
    print(" +------------------------+")
    for i in range(8):
        fila = str(i) + "|"
        for j in range(8):
            fila += f" {tablero[i][j]:2d}"
        fila += " |"
        print(fila)
    print(" +------------------------+")

ruta_caballo = generar_ruta_caballo((0, 0))
imprimir_tablero(ruta_caballo)



ruta = generar_ruta_caballo((0, 0))
print(ruta)
