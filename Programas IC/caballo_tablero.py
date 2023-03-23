import tkinter as tk 


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

LADO_CASILLA = 80
LADO_TABLERO = 8 * LADO_CASILLA

def crear_tablero(canvas):
    """Crea el tablero de ajedrez en el canvas"""
    for i in range(8):
        for j in range(8):
            x0, y0 = j * LADO_CASILLA, i * LADO_CASILLA
            x1, y1 = x0 + LADO_CASILLA, y0 + LADO_CASILLA
            if (i + j) % 2 == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#EEEED2", outline="")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#000000", outline="")
    
def crear_ruta(canvas, ruta_caballo):
    """Crea la ruta del caballo en el canvas"""
    for i, (x, y) in enumerate(ruta_caballo):
        x0, y0 = y * LADO_CASILLA, x * LADO_CASILLA
        x1, y1 = x0 + LADO_CASILLA, y0 + LADO_CASILLA
        canvas.create_text(x0 + LADO_CASILLA // 2, y0 + LADO_CASILLA // 2, text=str(i+1), font=("Arial", 24))
        canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill="#007FFF", outline="")

ruta_caballo = generar_ruta_caballo((0, 0))

root = tk.Tk()
root.title("Ruta del Caballo")

canvas = tk.Canvas(root, width=LADO_TABLERO, height=LADO_TABLERO)
canvas.pack()

crear_tablero(canvas)
crear_ruta(canvas, ruta_caballo)

root.mainloop()

ruta = generar_ruta_caballo((0, 0))
print(ruta)
