# Listas
lista = [2026, "Diciembre", 11, 78.9, "Miercoles"]
print(lista)
print(type(lista))
print("\n")

# Tuplas
tupla = (10, 20, 30, 40)
print(tupla)
print(type(tupla))
print("\n")

# Conjuntos
conjunto = {2000, 2001, 2002, 2003, 2000}
print(conjunto)
print(type(conjunto))
print(f"EL numero 2000 esta en el conjunto: {2000 in conjunto}")
print("\n")

# Diccionarios
diccionario = {
    "nombre": "Cristian",
    "edad": 19,
    "estatura": 1.85,
    "promedio": 9.85
}
print(diccionario)
print(type(diccionario))
print("\n")

# Operaciones en lista
print("//Operacion append()")
print("Agrega un elemento nuevo al final de la lista ya existente:")
lista.append(3)
print(f"lista.append(2000): {lista}")
print("\n")

print("//Operacion insert()")
print("Inserta un nuevo elemento en una posicion\ndeterminada de la lista mediante su indice")
lista.insert(2, 3)
print(f"lista.insert(2, 3): {lista}")
print("\n")

print("//Operacion remove()")
print("Elimina la primera aparicion de un valor determinado:")
lista.remove(3)
print(f"lista.remove(3): {lista}")
print("\n")

print("//Operacion pop()")
print("Elimina el elemento en la posicion indice y retorna su valor:")
print(f"lista.pop(4): {lista.pop(4)} ")
print("\n")

print("//Operacion actualizar")
print("Se debe acceder a la posicion indice y asignar un nuevo valor:")
lista[0] = 2025
print(f"lista[0] = 2025: {lista}")
print("\n")

print("//Operacion sort()")
print("Ordena una lista ya existente, si la lista contiene variables diferentes se debe usar 'key':")
lista.sort(key=lambda x: str(type(x)))
print(f"lista.sort(key=lambda x: str(type(x))): {lista}")
print("\n")

print("//Operacion sorted()")
print("Devuelve una lista nueva ya ordenada, si la lista contiene variables diferentes se debe usar 'key':")
lista_ordenada = sorted(lista, key=lambda x: (isinstance(x, str), str(x)))
print(f"Lista ordenada con sorted(): {lista_ordenada}")
print("\n")

#Operaciones en tuplas

print("//Operacion para insertar")
print("""La tupla no es mutable, entonces los valores se insertan
de manera manual cuando se crea la tupla. Si se desea agregar nuevos valores
se debe crear una nueva tupla.""")
tupla_ej1 = (1,2,3,4,5)
tupla_ej2 = (1,2,3,4,5,6)
print(f"""Tupla con valores del 1 al 5: {tupla_ej1}
Tupla nueva con valores del 1 al 6: {tupla_ej2}""")
print("\n")

print("//Operacion para eliminar")
print("""La tupla no es mutable, entonces los valores se eliminan
de manera manual cuando se crea la tupla. Si se desea eliminar valores
se debe crear una nueva tupla.""")
tupla_ej3 = (1,2,3,4)
print(f"""Tupla con valores del 1 al 5: {tupla_ej1}
Tupla nueva con valores del 1 al 4: {tupla_ej3}""")
print("\n")

print("//Operacion para actualizar")
print("""La tupla no es mutable, entonces los valores se actualizan
de manera manual cuando se crea la tupla. Si se desea actualizar valores
se debe crear una nueva tupla.""")
tupla_ej4 = (1,3,5)
print(f"""Tupla con valores del 1 al 5: {tupla_ej1}
Tupla nueva con valores 1,3 y 5: {tupla_ej4}""")
print("\n")

print("//Operacion sorted()")
print("Devuelve una lista ordenada con los datos de la tupla, si la lista contiene variables diferentes se debe usar 'key':")
tupla_ej5 = (55,44,33,22,11)
tupla_ordenada = sorted(tupla_ej5)
print(f"Tupla (55,44,33,22,11) ordenada con sorted(): {tupla_ordenada}")
print("\n")

# Operaciones en conjuntos
print("//Operacion add()")
print("Agrega un unico elemento al conjunto:")
conjunto.add(2004)
print(f"""Conjunto agregando 2004: {conjunto}""")
print("\n")

print("//Operacion remove()")
print("Elimina un dato determinado del conjunto, si el valor no existe lanza error:")
conjunto.remove(2000)
print(f"Conjunto removiendo 2000: {conjunto}")
print("\n")

print("//Operacion discard()")
print("Elimina un dato determinado del conjunto, si el valor no existe no lanza error:")
conjunto.discard(2006)
print(f"Conjunto removiendo 2006: {conjunto}")
print("\n")

print("//Operacion para actualizar")
print("Se ocupa remove, discard y add para eliminar y agregar nuevos valores.")

print("//Operacion sorted()")
print("Devuelve una lista nueva ya ordenada con los datos del conjunto, si la lista contiene variables diferentes se debe usar 'key':")
conjunto_ej1 = {55,44,33,22,11}
conjunto_ordenado = sorted(conjunto_ej1)
print(f"Conjunto {conjunto_ej1} ordenado con sorted(): {conjunto_ordenado}")
print("\n")

# Operaciones con diccionarios
print("//Operacion para agregar")
print("Se debe crear el diccionario de manera manual siguiendo esta estructura:")
print("diccionario = {'clave1' : 'valor1', 'clave2' : 'valor2'}")

print("//Operacion pop()")
print("Elimina el par clave-valor en la clave indicada y retorna su valor:")
print(f"diccionario.pop('nombre'): {diccionario.pop("nombre")} ")
print("\n")

print("//Operacion del")
print("Elimina un par clave-valor especifico. Tambien puede borrar todo el diccionario:")
del diccionario["promedio"]
print(f"del diccionario['promedio']: {diccionario}")
print("\n")

print("// Operacion para actualizar")
print("""Para actualizar un par clave-valor en el diccionario se debe modificar
manualmente asignandole un valor a un tributo especifico del diccionario, 
igual sirve para agregar nuevas claves.""")
diccionario["nombre"] = "Cristian"
print(f"diccionario['nombre'] = 'Cristian': {diccionario}")
print("\n")

print("//Operacion sorted()")
print("Si se llama directamente a sorted ordena sus claves en una lista:")
claves_diccionario = sorted(diccionario)
print(claves_diccionario)
print("Se usa .items para ordenarlo por claves conservando el diccionario:")
diccionario_ordenado = sorted(diccionario.items())
print(porclaves_diccionario)
print("Se ocupa dict para reconstruir el diccionario ordenado:")
porvalor_diccionario = dict(sorted(diccionario.items()))
print(porvalor_diccionario)
print("\n")

# EJERCICIO EXTRA

def buscar():
    contacto_buscar = input("Ingrese el nombre del contacto a buscar: ")

    for contacto in contactos:
        if contacto["nombre"].lower() == contacto_buscar.lower():
            return contacto

    return None


def registrar_numero():

    while True:
        numero = input("Ingrese el numero telefonico del contacto: ")

        if not numero.isdigit():
            print("El numero debe contener solamente digitos.")
        elif len(numero) > 11:
            print("El numero no debe superar los 11 digitos.")
        else:
            return numero


def agregar():
    nombre = input("Ingrese el nombre del contacto nuevo: ")

    numero = registrar_numero()

    contacto = {
        "nombre": nombre,
        "telefono": numero
    }

    contactos.append(contacto)
    print("Contacto agregado correctamente.")


def modificar():
    contacto_modificar = buscar()

    if contacto_modificar is None:
        print("Contacto inexistente.")
        return

    campo = input("Que clave desea modificar (nombre o telefono): ").lower()

    if campo == "telefono":
        contacto_modificar["telefono"] = registrar_numero()

    elif campo == "nombre":
        contacto_modificar["nombre"] = input("Ingrese el nuevo nombre: ")

    else:
        print("Clave inexistente.")
        return

    print("Contacto modificado correctamente.")


def eliminar():
    contacto_eliminar = buscar()

    if contacto_eliminar is None:
        print("Contacto inexistente.")
        return

    contactos.remove(contacto_eliminar)
    print("Contacto eliminado correctamente.")


def mostrar():
    if not contactos:
        print("La agenda esta vacia.")
        return

    for contacto in contactos:
        print(contacto)


def menu():
    print("1. Buscar contacto")
    print("2. Agregar contacto")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


contactos = []
opcion = 0

while opcion != 5:

    print("\nAGENDA DE CONTACTOS POR TERMINAL")
    menu()

    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Solo se aceptan numeros en las opciones del menu.")
        continue

    match opcion:
        case 1:
            buscado = buscar()

            if buscado is None:
                print("Contacto inexistente.")
            else:
                print(buscado)

        case 2:
            agregar()

        case 3:
            modificar()

        case 4:
            eliminar()

        case 5:
            print("Contactos registrados:")
            mostrar()
            print("Gracias por utilizar el programa.")

        case _:
            print("Opcion no valida.")