import random as rd
from itertools import islice


copia_seguridad=[]
tabla=[]
output=[]

def crear_dividir_tabla():
    n=15
    for i in range(1,n):
        tabla.append(rd.randint(0,100))

    divisiones = [2, 4, 3, 6]

    # Usando islice
    output = [list(islice(iter(tabla), elem)) for elem in divisiones]
    
    print("Lista despues de dividirla:", output)    
    return output

crear_dividir_tabla()

l2 =[]
#hacemos lo mismo del código anterior
def sacar(lista,lista2):
     for l1 in range(len(lista)):
          if type(lista[l1]) is list:
               #aqyi la recursividad 
               sacar(lista[l1],l2)
          else:
               lista2.append(lista[l1])

sacar(output, l2)
print("Elementos sacados:", l2)


def esta_explorando(output):
    for i in output:
        n=1
        copia_seguridad.append(max(output(n)))
        n=+1

    print(copia_seguridad)
    return

def desplazar_elementos():
    
    primer_elemento = tabla.pop(0)
    tabla.append(primer_elemento)
    print(tabla)

desplazar_elementos()



