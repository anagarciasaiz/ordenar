import random
class ejercicio2():
    def __init__(self):#constructor
        tareas = []
        for i in range(int(input("Escriba el numero de tareas que va a relizar:"))):
             tarea = 't' + (str(i+1)) #t1 t2 t3....tn
             tareas.append(tarea)
        random.shuffle(tareas) #metodo que sirve para barajar las tareas 
        print(tareas)
        orden=[]
        self.tareas=tareas
        self.orden=orden

        