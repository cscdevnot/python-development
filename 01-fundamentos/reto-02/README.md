# Reto #02 — Funciones y alcance

## Descripción

Segundo reto del roadmap de programación de MoureDev. El objetivo es comprender el funcionamiento de las funciones en Python, sus diferentes formas de utilización y el alcance de las variables.

Se desarrollan ejemplos prácticos para comprender cómo declarar funciones, utilizar parámetros, devolver valores, crear funciones anidadas y trabajar con variables locales y globales.

## Objetivos

- Crear funciones con y sin parámetros.
- Comprender la diferencia entre `print()` y `return`.
- Implementar funciones anidadas.
- Utilizar funciones integradas de Python (*built-in functions*).
- Comprender el alcance de las variables locales y globales.
- Aplicar estructuras condicionales y ciclos mediante el ejercicio adicional FizzBuzz.

## Conceptos aplicados

| Concepto | Descripción |
|---|---|
| `def` | Permite declarar funciones. |
| Parámetros y argumentos | Permiten proporcionar información a las funciones. |
| `return` | Devuelve un resultado desde una función. |
| Funciones anidadas | Permiten declarar funciones dentro de otras funciones. |
| Built-in functions | Funciones integradas de Python, como `len()`, `type()`, `max()`, `min()`, `sum()` y `round()`. |
| Variables locales | Variables cuyo alcance está limitado a una función. |
| Variables globales | Variables declaradas fuera de las funciones. |
| `global` | Permite modificar una variable global desde una función. |
| Scope | Determina dónde pueden utilizarse las variables. |
| Condicionales | Permiten ejecutar instrucciones dependiendo de determinadas condiciones. |
| Ciclos | Permiten repetir instrucciones mediante `for`. |
| Operador módulo `%` | Permite obtener el residuo de una división. |

## Ejercicio adicional: FizzBuzz

Se implementa una función que recibe dos cadenas de texto y recorre los números del 1 al 100.

Las condiciones son:

1. Si el número es múltiplo de 3 y 5, imprime ambas cadenas.
2. Si es múltiplo de 3, imprime la primera cadena.
3. Si es múltiplo de 5, imprime la segunda cadena.
4. Si no cumple ninguna condición, imprime el número.

Se utiliza el operador módulo (`%`) para comprobar la divisibilidad y una estructura `if`, `elif` y `else` para evitar ejecutar varias condiciones para un mismo número.

La variable local `contador` registra cuántas veces se imprime un número en lugar de los textos. Finalmente, la función devuelve ese resultado mediante `return`.

### Resultado esperado

- Iteraciones: 100.
- Múltiplos de 3 o 5: 47.
- Números impresos directamente: 53.

Por lo tanto, el resultado final de la función es:

```text
Numero de veces que no se imprimio el texto: 53
```

## Aprendizajes y conclusiones

Durante este reto se comprendió que las funciones permiten organizar el código en bloques reutilizables y separar responsabilidades.

Se identificó la diferencia entre imprimir información mediante `print()` y devolver resultados mediante `return`, así como la importancia de utilizar parámetros para evitar dependencias innecesarias de variables externas.

También se estudió el alcance de las variables, comprendiendo las diferencias entre los ámbitos local, enclosing y global, además de la utilización de `global` para modificar variables globales.

Finalmente, mediante FizzBuzz se integraron funciones, parámetros, valores de retorno, ciclos, condicionales y operadores aritméticos en un mismo ejercicio.

## Estado

**Completado.**