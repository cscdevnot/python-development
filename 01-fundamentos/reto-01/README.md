# Reto #01 — Operadores y Estructuras de Control en Python

## Descripción

Este reto tiene como objetivo comprender y aplicar los operadores y las estructuras de control fundamentales del lenguaje Python.

Se desarrollaron ejemplos prácticos para representar las diferentes operaciones disponibles en Python, así como mecanismos para controlar el flujo de ejecución de un programa.

## Objetivos

- Identificar y utilizar los diferentes tipos de operadores de Python.
- Comprender el funcionamiento de las estructuras condicionales.
- Implementar estructuras iterativas.
- Controlar el flujo de ejecución mediante instrucciones específicas.
- Comprender el manejo de excepciones.
- Aplicar los conocimientos adquiridos mediante ejercicios prácticos.

## 1. Operadores

Se implementaron ejemplos de las siguientes categorías:

| Categoría | Operadores |
|---|---|
| Aritméticos | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparación | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Lógicos | `and`, `or`, `not` |
| Asignación | `=`, `+=`, `-=`, `*=`, `/=`, `**=` |
| Identidad | `is`, `is not` |
| Pertenencia | `in`, `not in` |
| Bit a bit | `&`, `|`, `^`, `~`, `<<`, `>>` |

Los ejemplos permiten observar cómo funcionan los operadores y cómo pueden utilizarse para realizar operaciones matemáticas, comparar valores y evaluar condiciones.

## 2. Estructuras de control

### 2.1 Condicionales

Se utilizaron las estructuras:

- `if`: evalúa una condición.
- `elif`: permite evaluar condiciones adicionales.
- `else`: ejecuta instrucciones cuando ninguna de las condiciones anteriores se cumple.

Se implementó un sistema de evaluación de calificaciones para clasificar el rendimiento académico.

### 2.2 Selección por patrones: Match / Case

Se utilizó `match/case` para evaluar diferentes valores de una variable y ejecutar instrucciones dependiendo del caso correspondiente.

Se implementaron diferentes resultados según la opción seleccionada y un caso predeterminado mediante `case _`.

**Nota:** Esta estructura está disponible desde Python 3.10.

### 2.3 Estructuras iterativas

**For**

Permite recorrer una secuencia o repetir instrucciones un número determinado de veces.

Se implementó un ciclo que recorre los números del 1 al 10 y determina si cada número es par o impar.

**While**

Permite repetir instrucciones mientras una condición sea verdadera.

Se implementó un contador que disminuye progresivamente hasta alcanzar el valor de cero.

### 2.4 Control de iteraciones

Se trabajó con las siguientes instrucciones:

| Instrucción | Descripción |
|---|---|
| `break` | Finaliza inmediatamente un ciclo. |
| `continue` | Omite la iteración actual y continúa con la siguiente. |
| `pass` | No realiza ninguna operación; funciona como una instrucción vacía. |

Se realizaron ejemplos independientes para comprender el comportamiento de cada instrucción.

### 2.5 Manejo de excepciones

Se utilizó la estructura `try/except/else/finally` para comprender cómo Python permite controlar errores durante la ejecución.

- `try`: contiene el código que puede generar una excepción.
- `except`: permite capturar y gestionar excepciones.
- `else`: se ejecuta cuando no ocurre ninguna excepción.
- `finally`: se ejecuta independientemente de si ocurrió una excepción.

También se identificó `raise` como una instrucción que permite generar excepciones intencionalmente.

## 3. Ejercicio extra

Se desarrolló un ciclo `for` que recorre los números del 10 al 55 y utiliza condiciones para filtrar los valores.

Se aplicaron las siguientes reglas:

1. Se omite el número 16.
2. Se omiten los múltiplos de 3.
3. Se omiten los números impares.
4. Se imprimen los números restantes.

Este ejercicio permitió combinar estructuras condicionales e iterativas con la instrucción `continue`.

## 4. Conceptos aprendidos

- Diferenciación y aplicación de los operadores de Python.
- Evaluación de condiciones mediante expresiones lógicas.
- Selección de instrucciones mediante estructuras condicionales.
- Repetición de instrucciones utilizando ciclos.
- Control del flujo de ejecución mediante `break`, `continue` y `pass`.
- Manejo de excepciones y control de errores.
- Combinación de diferentes estructuras para resolver problemas.

## 5. Ejecución

Para ejecutar el programa desde la terminal, utiliza:
python main.py

## 6. Tecnologías utilizadas

- Lenguaje: Python
- Editor: Visual Studio Code / editor de preferencia
- Control de versiones: Git
- Repositorio: GitHub

## Estado
**Completado**

**Ruta de aprendizaje:** Fundamentos de Python → Reto #01.

**Repositorio de referencia:** [MoureDev - Retos de programación](https://github.com/mouredev/roadmap-retos-programacion)