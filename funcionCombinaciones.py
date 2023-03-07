def facto(Num):
    i=1
    fact=Num
    while fact>1:
        i*=fact
        fact-=1
    return i

Num1 = float(input("Ingrese un primer numero: "));
Num2 = float(input("ingrese un segundo numero: "));
numerador = facto(Num1);
denominador = facto(Num2)*facto(Num1-Num2);
Comb = numerador/denominador;
print("la contidad de combinaciones son: ",Comb);
