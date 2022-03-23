num = int(input("Ingresa un numero entero positivo:\n"))

if num < 0:
    print("No se permiten negativos")
else:
    for i in range(1, num+1, 2):
        print(i, end=",")