Dis=float(input("Ingrese la distancia recorrida anual en km "))
Comb=int(input("Ingrese consumo de combustible anual en L "))
Cost=float(input("Ingrese costo promedio anual en $ "))
ConsC=Comb/100
CostTA=Dis*ConsC*Cost
print("El costo anual del consumo de combustible de su vehiculo es $",CostTA)