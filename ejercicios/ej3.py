import random as rd
from itertools import islice


copia_seguridad=[]
tabla=[]

def crear_dividir_tabla():
    n=15
    for i in range(1,n):
        tabla.append(rd.randint(0,100))

    divisiones = [2, 4, 3, 6]

    # Usando islice
    Output = [list(islice(iter(tabla), elem)) for elem in divisiones]
    
    print("List after splitting", Output)    
    return tabla

def esta_explorando():

    return