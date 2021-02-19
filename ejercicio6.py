# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:38:48 2021

@author: Liliana
"""

var_Distancia=int(input("Ingrese la distancia en Km :"));
var_Tiempo=int(input("Ingrese el tiempo en minutos"));
TiempoHoras=var_Tiempo/60;
velocidad=var_Distancia/TiempoHoras;
print("La velocidad necesaria es :",velocidad , "Km/h")