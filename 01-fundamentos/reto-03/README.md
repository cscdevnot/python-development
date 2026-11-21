# Reto #03 — Estructuras de datos en Python

## Descripción

En este reto se estudian las principales estructuras de datos integradas de Python: listas, tuplas, conjuntos y diccionarios.

El objetivo es comprender cómo se crean, cuáles son sus características y qué operaciones se pueden realizar con cada una de ellas. También se desarrolla un ejercicio práctico que consiste en crear una agenda de contactos mediante la terminal.

## Objetivos

- Comprender las diferencias entre listas, tuplas, conjuntos y diccionarios.
- Identificar cuándo utilizar cada estructura de datos.
- Practicar operaciones de inserción, eliminación y actualización.
- Utilizar métodos para ordenar y consultar información.
- Aplicar funciones para organizar el código.
- Implementar validaciones y manejo de excepciones.
- Desarrollar un programa interactivo mediante la terminal.

## 1. Estructuras de datos

### Listas (`list`)

Son estructuras ordenadas y mutables que permiten almacenar diferentes tipos de datos y elementos duplicados.

En el ejercicio se realizan las siguientes operaciones:

| Operación | Descripción |
| `append()` | Agrega un elemento al final de la lista. |
| `insert()` | Inserta un elemento en una posición determinada. |
| `remove()` | Elimina la primera aparición de un valor. |
| `pop()` | Elimina un elemento mediante su índice y devuelve su valor. |
| Actualización | Modifica un elemento mediante su índice. |
| `sort()` | Ordena la lista original. |
| `sorted()` | Devuelve una nueva lista ordenada. |

También se utiliza el parámetro `key` para establecer criterios personalizados de ordenamiento.

### Tuplas (`tuple`)

Son estructuras ordenadas e inmutables que permiten almacenar diferentes tipos de datos y elementos duplicados.

Debido a su inmutabilidad, no es posible agregar, eliminar o modificar directamente sus elementos. Para representar estos cambios se crean nuevas tuplas.

Se utiliza `sorted()` para obtener una lista ordenada a partir de los elementos de una tupla.

### Conjuntos (`set`)

Son estructuras que almacenan elementos únicos y permiten realizar operaciones de inserción y eliminación.

En el ejercicio se utilizan:

| Operación | Descripción |
| `add()` | Agrega un elemento al conjunto. |
| `remove()` | Elimina un elemento; genera un error si no existe. |
| `discard()` | Elimina un elemento sin generar un error si no existe. |
| Actualización | Se combinan operaciones de eliminación e inserción. |
| `sorted()` | Devuelve una lista ordenada con los elementos del conjunto. |

También se comprueba la pertenencia de un elemento mediante el operador `in`.

### Diccionarios (`dict`)

Son estructuras que almacenan información mediante pares de clave y valor. Cada clave debe ser única y permite acceder directamente al valor asociado.

En el ejercicio se realizan las siguientes operaciones:

| Operación | Descripción |
| Inserción | Se agrega una nueva clave y su valor mediante asignación. |
| `pop()` | Elimina una clave y devuelve su valor asociado. |
| `del` | Elimina un par clave-valor específico. |
| Actualización | Se asigna un nuevo valor a una clave existente. |
| `sorted()` | Ordena las claves del diccionario. |
| `items()` | Permite obtener los pares clave-valor para ordenarlos. |
| `dict()` | Permite construir un nuevo diccionario a partir de los pares ordenados. |

## 2. Ejercicio extra: Agenda de contactos

Se desarrolla una agenda de contactos interactiva que funciona desde la terminal.

Para almacenar la información se utiliza una lista de diccionarios. Cada contacto contiene dos atributos:

- `nombre`: nombre del contacto.
- `telefono`: número telefónico almacenado como cadena de texto (`str`).

### Funcionalidades

El programa presenta un menú con cinco opciones:

1. Buscar contacto.
2. Agregar contacto.
3. Modificar contacto.
4. Eliminar contacto.
5. Salir.

### Validaciones implementadas

- Se comprueba que el teléfono contenga únicamente dígitos.
- Se establece un máximo de 11 dígitos para el número telefónico.
- Se verifica que un contacto exista antes de modificarlo o eliminarlo.
- Se controlan las entradas no numéricas al seleccionar una opción del menú.
- Se permite buscar nombres sin distinguir entre mayúsculas y minúsculas.

### Funciones utilizadas

| Función | Responsabilidad |
| `buscar()` | Busca un contacto por su nombre. |
| `registrar_numero()` | Solicita y valida un número telefónico. |
| `agregar()` | Registra un contacto nuevo. |
| `modificar()` | Actualiza el nombre o teléfono de un contacto. |
| `eliminar()` | Elimina un contacto de la agenda. |
| `mostrar()` | Muestra los contactos registrados. |
| `menu()` | Presenta las opciones disponibles. |

## 3. Conceptos de Python practicados

Durante el desarrollo del reto se aplicaron los siguientes conceptos:

- Variables y tipos de datos.
- Listas, tuplas, conjuntos y diccionarios.
- Métodos y operaciones de estructuras de datos.
- Funciones y parámetros.
- Ciclos `for` y `while`.
- Condicionales `if`, `elif` y `else`.
- Estructura `match-case`.
- Manejo de excepciones mediante `try` y `except`.
- Retorno de valores mediante `return`.
- Comprensión de referencias a objetos.
- Validación de cadenas de texto.
- Ordenamiento mediante `sort()` y `sorted()`.
- Funciones lambda como criterios de ordenamiento.

## 4. Ejecución del programa

Para ejecutar el reto desde la terminal, utiliza:

main.py

El programa ejecutará primero los ejemplos de las cuatro estructuras de datos y posteriormente iniciará la agenda de contactos interactiva.

**Reto #03 completado.**