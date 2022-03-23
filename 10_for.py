#la sentencia for permite iterar un numero especifico de veces 
#una sentencia o conjunto de sentencias 

n = int(input("cuantos numeros desas sumar?"))
suma=0 
for i in range(n):
    numero = float (input("introduce un numero: "))
    suma= suma + numero 


print("la suma de los numeros introducidos es: ", suma)
