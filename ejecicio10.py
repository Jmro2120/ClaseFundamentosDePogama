# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:39:41 2021

@author: Liliana
"""

var_gradosCelsius=float(input("Ingrese grados celcius : "));
gradosKelvin=var_gradosCelsius + 273.15;
gadosFarenheit= 1.8 * (gradosKelvin - 273.15) + 32;
print("Grados kelvin : ", gradosKelvin);
print("Grados farenheit : ", gadosFarenheit);