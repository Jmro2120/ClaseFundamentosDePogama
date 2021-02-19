# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:04:14 2021

@author: Liliana
"""

var_valorNeto=int(input("Ingrese el valor neto de la compra :"));
var_Iva=var_valorNeto*0.19;
valorMasIva=(var_valorNeto+var_Iva);
valorTotal=valorMasIva-(valorMasIva*0.05);
print("El precio de la compra es :",valorTotal);