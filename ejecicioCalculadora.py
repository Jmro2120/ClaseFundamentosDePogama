# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:00:40 2021

@author: Liliana
"""

print("Ingrese el valor según la acción que desee realizar");
var_tipoOperacion=int(input("1:Suma , 2:Resta , 3:Multiplicación , 4:División , 5:Potenciación : "));
if(var_tipoOperacion == 1):
    var_n1=int(input("Ingrese el primer numero :"));
    var_n2=int(input("Ingrese el segundo numero :"));
    suma=var_n1+var_n2;
    print("El valor de la suma es :" , suma);
elif(var_tipoOperacion == 2):
    var_n1=int(input("Ingrese el primer numero :"));
    var_n2=int(input("Ingrese el segundo numero :"));
    resta=var_n1-var_n2;
    print("El valor de la resta es :" , resta);
elif(var_tipoOperacion == 3):
    var_n1=int(input("Ingrese el primer numero :"));
    var_n2=int(input("Ingrese el segundo numero :"));
    multiplicacion=var_n1*var_n2;
    print("El valor de la multiplicación es :" , multiplicacion);
elif(var_tipoOperacion == 4):
    var_n1=int(input("Ingrese el primer numero :"));
    var_n2=int(input("Ingrese el segundo numero :"));
    Division=var_n1/var_n2;
    print("El valor de la división es :" , Division);
elif(var_tipoOperacion == 5):
    var_n1=int(input("Ingrese el valor a potenciar :"));
    var_n2=int(input("Ingrese el valor al que desea potenciar :"));
    Potenciacion=pow(var_n1,var_n2);
    print("El valor de la potenciación es :" , Potenciacion);
else:
    print("Valor incorrecto");