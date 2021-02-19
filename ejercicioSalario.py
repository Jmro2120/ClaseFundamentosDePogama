# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:12:58 2021

@author: Liliana
"""

var_horas_trabajadas=int(input("ingrese la cantidad de horas trabajadas :"));
var_precio_porhora=int(input("ingrese el precio por hora trabajada :"));
salario_neto = var_horas_trabajadas * var_precio_porhora;

if(salario_neto > 300):
    var_salario=salario_neto-(salario_neto*0.02);
    print("su salario es",var_salario);
else:
    var_salario=salario_neto;
    print("su salario es",var_salario);