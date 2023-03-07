Num=int(input("Ingrese un numero "))
if Num > 0:
    i=1
    fact=Num
    while fact>1:
        i*=fact
        fact-=1
    print("El factorial de",Num,"es: ",i)
else:
    print("No es posible calcular el factorial")
    