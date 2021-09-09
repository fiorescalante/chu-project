print("chu te amooo")
n= int(input("ingrese la cant de terminos: "))
cont=0
i=1
sum=0
while cont<n:

    if i % 2!=0:
        cont+=1
        print(cont, sum)
        if cont%2==0:

            sum-=1/i
            print("resta", sum)





#1/0! + 1/2! + 1/3!