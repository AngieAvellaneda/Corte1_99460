Num=int(input("Ingrese un numero: "))
i=2
Primo=True
while i < Num:
    if Num%i==0:
        print("No es primo")
        Primo = False
        break
    i += 1
if Primo != False:
  print("Es primo")
print("Los numeros primos son: \n1")
x = 1
Primo = True
while x < Num:
    Primo = True
    i = 2
    while i < x:
        if x%i == 0:
            Primo = False
            break
        i += 1
        if Primo != False:
            print(x)
            break
    x += 1