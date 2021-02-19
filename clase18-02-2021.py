# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:02:32 2021

@author: Liliana
"""

print("ingrese 3 numeros enteros diferenetes") # Mensaje De petición al usuario
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor")) # Petición al ususario de ingresar 1 o 2 según desee dependiendo del orden. la opción digitada queda guardada en la variable e
a = int(input("ingrese el numero a")) # valor 1 digitado por el ususario.queda guardado en la variable a
b = int(input("ingrese el numero b")) # valor 2 digitado por el ususario.queda guardado en la variable b
c = int(input("ingrese el numero c"))# valor 3 digitado por el ususario.queda guardado en la variable c

if (e == 1): # comparación del valor guardado en la variable e.según el orden a mostrar de los numeros 
    if (a > b): # comparación de valor a mayor que b
        if (a > c): # comparación de valor a mayor que c , en este punto a es mayor que ambos numeros
            if(b > c): # comparación de valor b mayor que c , teniendo encuenta que a es mayor que ambos
               print(a, b, c) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
            else: # negación de la comparación de valor b mayor que c 
               print(a, c, b)  # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
    if (c > a):# comparación de valor c mayor que a
        if (c > b): # comparación de valor c mayor que b , en este punto c es mayor que ambos numeros
            if(b > a): # comparación de valor b mayor que a , teniendo encuenta que c es mayor que ambos
               print(c, b, a) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
            else: # negación de la comparación de valor b mayor que a 
               print(c, a, b) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
    if (b > a): # comparación de valor b mayor que a
        if (b > c): # comparación de valor b mayor que c , en este punto b es mayor que ambos numeros
            if(a > c): # comparación de valor a mayor que c , teniendo encuenta que b es mayor que ambos
               print(b, a, c) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
            else: # negación de la comparación de valor a mayor que c 
               print(b, c, a) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente


if (e == 2): # comparación del valor guardado en la variable e.según el orden a mostrar de los numeros , teniendo en cuenta que el valor ingresado no fue 1 ya que el programa llego a este comparador
    if (a < b): # comparación de valor a menor que b
        if (a < c): # comparación de valor a menor que c , en este punto a es menor que ambos numeros
            if(b < c):# comparación de valor b menor que c , teniendo encuenta que a es menor que ambos
               print(a, b, c) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
            else: # negación de la comparación de valor b menor que c
               print(a, c, b) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
    if (c < a): # comparación de valor c menor que a
        if (c < b): # comparación de valor c menor que b , en este punto c es menor que ambos numeros
            if(b < a): # comparación de valor b menor que a , teniendo encuenta que c es menor que ambos
               print(c, b, a)  # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
            else: # negación de la comparación de valor b menor que a
               print(c, a, b)  # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
    if (b < a): # comparación de valor b menor que a
        if (b < c): # comparación de valor b menor que c , en este punto b es menor que ambos numeros
            if(a < c): # comparación de valor a menor que c , teniendo encuenta que b es menor que ambos
               print(b, a, c) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente
            else: # negación de la comparación de valor a menor que c
               print(b, c, a) # Impresión de los valores de acuerdo a las comparaciones hechas anteriormente

if (a == b): # comparación si el valor a es igual que el valor b
    print("b y a son iguales") # como la condición se cumple, el programa muestra el siguiente mensaje
    if (a == c): # comparación si el valor a es igual que el valor c
        print("a y c son iguales") # como la condición se cumple, el programa muestra el siguiente mensaje
        if(b == c): # comparación si el valor b es igual que el valor c
           print(" b y c con iguales") # como la condición se cumple, el programa muestra el siguiente mensaje
           if(a == b == c): # comparación si el valor a es igual que el valor b e igual que el valo c , es decir los trea valores son iguales
              print("todos son iguales") # como la condición se cumple, el programa muestra el siguiente mensaje