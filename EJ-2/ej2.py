import random
class ejercicio2():
    def __init__(self):#constructor
        tareas = []
        for i in range(int(input("Escriba el numero de tareas que va a relizar:"))):
             tarea = 't' + (str(i+1)) #t1 t2 t3....tn
             tareas.append(tarea)
        random.shuffle(tareas) #metodo que sirve para barajear las tareas 
        print(tareas)
        orden=[]
        self.tareas=tareas
        self.orden=orden
    def ordenacion(self,n,t):
        if len(self.tareas)>0:
            if 't' + str(n)==self.tareas[t]:
                print("ha realizado la tarea",n)
                self.orden.append(self.tareas[t])
                del self.tareas[t] #eliminamos self.tareas hasta q la len sea igual a 0
                self.ordenacion(n+1,0)
            else:
                print("esa tarea no es la q toca,realice la tarea",n)
        else:
            print(self.orden) 




        