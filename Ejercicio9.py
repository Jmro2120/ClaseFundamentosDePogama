# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:11:31 2021

@author: Liliana
"""

var_Masa=float(input("Ingrese masa del cuerpo en Kg : "));
var_CoeficienteRozamiento=float(input("Ingese el coeficiente de rozamiento en m/s2 :"));
fuerzaNormal=var_Masa*9.8;
fuerzaRozamiento=var_CoeficienteRozamiento*fuerzaNormal;
print("La fuerza a aplicar es de :", fuerzaRozamiento);