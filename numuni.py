numeros = []
while True:
    n = int(input("Digite um número: "))
    if n not in numeros:
        numeros.append(n)
    else:
        print("Número Duplicado! Não vou adicionar a lista.")
    resp = input("Quer continuar? [S/N] ").strip().upper()[0]
    if resp == "N":
        break
print("=*" * 30)    
print(f"Os números da lista são: {numeros} ")
