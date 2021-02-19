# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:49:36 2021

@author: Liliana
"""

var_Nempleados=int(input("Ingrese la cantidad de empleados que realizaran la tarea :"));
var_Tiempo=int(input("Ingrese la cantidad de horas que demoran los trabajadores en realizar la tarea :"));
print("Teniendo en cuenta lo anterior");
var_NempleadosNuevos=int(input("Ingrese la nueva cantidad de empleados que realizara la misma tarea :"));
tiempoNuevo=(var_Tiempo*var_Nempleados)/var_NempleadosNuevos;
print("el tiempo que demoraran los nuevos empleados sera de :",tiempoNuevo,"horas")