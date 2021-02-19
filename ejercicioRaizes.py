# -*- coding: utf-8 -*-
import math;
"""
Created on Mon Feb 15 15:58:08 2021

@author: Liliana
"""

print("Teniendo en cuenta el trinomio de la forma Ax2+Bx+C");
var_A=int(input("Introdusca valor para A : "));
var_B=int(input("Introdusca valor para B : "));
var_C=int(input("Introdusca valor para B : "));

Raiz=pow(var_B, 2)-(4*var_A*var_C);

if(Raiz < 0):
    print("Posee raizes imaginarias");
elif(Raiz == 0):
    x=-var_B/(2 * var_A)
    print("Posee raizes de doble valor " , x);
else:
    x1=(-var_B)+ math.sqrt(Raiz) / (2 * var_A);
    x2=(-var_B)- math.sqrt(Raiz) / (2 * var_A);
    print("Valor de x1:" , x1);
    print("Valor de x2:" , x2);