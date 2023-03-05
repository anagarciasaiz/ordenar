link: https://github.com/anagarciasaiz/ordenar  
GRUPO: Iñigo Aguirre, Ana García, Angel Martínez, Lidia Velicia  
# ENTRGA ORDENAR

## Ejercicio 1: Ordenación por inserción dicotómica
Sea t una tabla de una sola línea donde los componentes son de tipo T --> COMPARABLE.  

1. Escribir primero las especificaciones del algoritmo que no usa la ayuda de otra tabla para calcular su resultado. Así, los elementos de t están «ordenados en su lugar». Cuidar especialmente la precondición y la postcondición; no son fáciles de obtener, pero proporcionan una guía útil para la construcción del algoritmo.
  
2. Desarrollar el análisis completo de la solución retenida. En la segunda estrategia de resolución, se define primero una tabla r inicialmente vacía con el mismo cardinal que t. Esta vez se inserta una copia de cada componente t «en su lugar» en r, buscando su posición, como en la primera estrategia que hemos visto antes.

3. Desarrollar este algoritmo nuevo.


## Ejercicio 2: Ordenación topológica
Una restricción se expresa mediante un par (i,j) de números enteros comprendidos entre 1 y n, que indica que la tarea ti va antes que la tarea tj. Es decir, la tarea ti debe estar terminada antes de empezar la tarea tj. La relación binaria «... precede ...» así definida en el conjunto de las n tareas es una relación de orden parcial: algunas tareas no son comparables.

Hacer un algoritmo que calcule una ordenación de la n tareas cumpliendo las restricciones. Está claro que no se pueden cumplir todas las restricciones. En este caso, no hay ordenación de las tareas. El algoritmo deberá tratar este caso correctamente.


## Ejercicio 3: Especificación de está_explorado
Escribir las especificaciones del predicado está_explorado. Las especificaciones se expresan usando la definición de un segmento de tabla. Es una serie de componentes que empieza por el máximo de la serie.

Definición: Se llama segmento en una tabla t de componentes de tipo T que deriva de COMPARABLE a la serie de componentes consecutivos más grande cuyo valor máximo es el primero de la serie.

La figura siguiente representa una tabla y sus segmentos.  
![08_07](https://user-images.githubusercontent.com/114655698/222982856-17e9c8a9-bd89-407d-946a-86d34f3da0af.png)


La parte t[inicio .. fin] contiene dos segmentos. El primero en t[5 .. 9] tiene por componente máximo 18 en la celda t[5]. El segundo en t[10 .. 11] tiene por componente máximo 21 en t[10].

La tabla t[inicio .. fin] contiene k segmentos S1, S2, …, Sk. Cada segmento Si tiene un primer componente de número di y un último componente de número fi que verifican:

           (1 ≤ i ≤ k ) (Si = t[di .. fi]) 
            max 1 ≤ i ≤ k(Si) = t[di] 
            max 1 ≤ i ≤ k(Si) ≤ t[fi + 1] 
Para cada segmento Si, explorar consiste en:

Hacer copia de seguridad del max del segmento: mi <-- t[di];
Desplazar los elementos de t[di+1 .. fi] una celda hacia la izquierda;

Colocar el elemento más grande del segmento «en lo alto»: t[fi] <-- mi.
