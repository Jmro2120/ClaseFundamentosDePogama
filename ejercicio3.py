# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:29:08 2021

@author: Liliana
"""

var_Estatura=float(input("Ingrese su estatura en cm :"));
var_Peso=float(input("Ingrese su peso en Kg :"));
EstaturaMetros=var_Estatura*0.01;
Imc=var_Peso/(pow(EstaturaMetros,2));
print("Imc :",Imc);