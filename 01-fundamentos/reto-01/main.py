a = 19
b = 13

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

edad = 19
tiene_identificacion = True

print ((edad >= 18) and tiene_identificacion)
print ((edad < 18) or (not tiene_identificacion))
print (not tiene_identificacion)
print ((edad >= 18) and (not tiene_identificacion))

numero = 20

numero += 5
print(numero)
numero -= 8
print(numero)
numero *= 3
print(numero)
numero /= 2
print(numero)
numero **= 2
print(numero)

d = [1, 2, 3]
e = [1, 2, 3]
f = d

print(d == e)
print(d is e)
print(d is f)
print(d is not f)

lenguajes = ["Python", "C", "Java", "JavaScript"]
mensaje = "Estoy aprendiendo Python"

print("Python" in lenguajes)
print("Rust" not in lenguajes)
print("Java" in mensaje)
print("C++" not in mensaje)

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)

print("Estructura if, elif, else")
calificacion = 95

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Aceptable")
else:
    print("Reprobado")

print("Estructura match/case")
opcion = 1

match opcion:
    case 1:
        print("Aprobado")
    case 2:
        print("Reprobado")
    case _:
        print("No tiene")

print("Ciclo for")
for numero in range(1,11):
    if (numero % 2) == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

print("Bucle while")
contador = 10

while contador > 0:
    print(contador)
    contador -= 1
    if contador == 0:
        print("El contador llego a 0.")

print("Control de iteraciones break")
for numero in range(1, 11):
    print(numero)
    if numero == 5:
        break

print("Control de iteraciones continue")
for numero in range(1,11):
    if (numero % 2) == 0:
        continue
    print(numero)

print("Control de iteraciones pass")
for numero in range(1,11):
    if (numero % 2) == 0:
        pass
    else:
        print("Es impar")

print("Excepciones")
x = 23
y = 11

try:
    division = x / y
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("Error")
else:
    print("El valor de la division es", division)
finally:
    print("Operacion finalizada")

print("EXTRA")

for numero in range(10, 56):
    if numero == 16:
        continue
    elif (numero % 3) == 0:
        continue
    elif (numero % 2) == 1:
        continue
    else:
        print(numero)