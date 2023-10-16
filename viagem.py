distancia=float(input("distancia da viagem em km: "))
if distancia <= 200:
    print(f"valor da viagem: R${distancia*0.50:.2f}")
else:
    print(f"valor da viagem: R${distancia*0.45:.2f}")