#apartado 1
t=[3,2,1,5,0,2]
for i in range (len(t)):
    for j in range(len(t)):
        if t[i]<t[j]:
            ay=t[i]
            t[i]=t[j]
            t[j]=ay
print(t)
#apartado 2
t=[3,2,1,5,0,2]
r=[]
for i in range(len(t)):
    r.append(min(t))
    t.remove(min(t))
print(r)
#apartado 3
def ordenar(t):
    a,b,corte=1,2,len(t)
    while a<corte:
        if t[a-1]<=t[a]:
            a,b=b,b+1
        else:
            t[a-1],t[a]=t[a],t[a-1]
            a-=1
            if a==0:
                a,b=b,b+1
    return t

t=[3,2,1,5,0,2]
print(ordenar(t))  