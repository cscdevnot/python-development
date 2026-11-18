# Funcion sin parametros y sin valor a retornar
def funcion_vacia():
    saludo = "Hola"
    print(saludo)

funcion_vacia()

# Funcion con parametro y sin valor a retornar
def funcion_saludo(nombre):
    print(nombre)

funcion_saludo("Cristian")

# Funcion con parametros y valor a retornar
def funcion_suma(x, y):
    return x + y

suma = funcion_suma(10, 50)
print(suma)

# Funciones anidadas
def operaciones():

    def suma(a, b):
        return a + b

    def multiplicar(a, b):
        return a * b

    print(f"La suma de 14 + 16 es igual a {suma(14, 16)}")
    print(f"La multiplicacion de 24 y 6 es igual a {multiplicar(24, 6)}")

operaciones()

# Funciones propias del lenguaje
lenguaje = "Python"
numeros = [10, 4, 67, 54, 23, 11, 36, 88]
promedio = (sum(numeros)) / (len(numeros))

print(f"Cadena: {lenguaje}")
print(f"Enteros: {numeros}")
print(f"Promedio Enteros: {promedio}")

print(f"Funcion len() con Cadena = {len(lenguaje)}")
print(f"Funcion type() con Cadena = {type(lenguaje)}")
print(f"Funcion max() con Enteros = {max(numeros)}")
print(f"Funcion min() con Enteros = {min(numeros)}")
print(f"Funcion sum() con Enteros = {sum(numeros)}")
print(f"Funcion round() con Promedio = {round(promedio, 2)}")

# Variables locales
def mostrar_numero():
    numero = 25
    print(numero)

mostrar_numero()
#print(numero)

# Variables globales
contador = 10
def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
incrementar()

print(contador)

# Alcance de variables en funciones anidadas
def funcion_exterior():
    mensaje = "Hello"
    
    def funcion_interior():
        print(mensaje)

    funcion_interior()

funcion_exterior()

# Ejercicio extra
def ejercicio_extra(w, z):
    contador = 0
    for i in range(1, 101):
        if ((i % 3) == 0) and ((i % 5) == 0):
            print(f"{w}{z}")
        elif (i % 3) == 0:
            print(w)
        elif (i % 5) == 0:
            print(z)
        else:
            print(i)
            contador += 1
    
    return contador

ejercicio = ejercicio_extra("Fizz", "Buzz")
print(f"Numero de veces que no se imprimio el texto: {ejercicio}")