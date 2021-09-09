n=int(input("ingrese un numero: "))
for i in range(10+1):
    multi= n*i
    print(i,"*",n, "=",multi)

n=int(input("ingrese un numero: "))
multi=1
for i in range(1,n+1):
    multi*=i
print(multi)

n= int(input("ingrese un numero: "))
m= int(input("ingrese un numero: "))
multi=1
for i in range(1,m+1):
    multi*=n
print(multi)

cant=int(input("ingrese la cant de numeros que quiere ingresar: "))
sum=0
for i in range(1,cant+1):
    nota=float(input("ingrese la nota: "))
    sum+=nota
promedio= sum/cant
print(promedio)
