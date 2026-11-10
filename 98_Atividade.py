matriz1 = []
matriz2 = []
matriz3 = []

print("Digite os valores da primeira matriz:")

for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz1.append(linha)

print("\nDigite os valores da segunda matriz:")

for i in range(4):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz2.append(linha)

# Soma
for i in range(4):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(linha)

# Resultado
print("\nMatriz resultante da soma:")

for i in range(4):
    for j in range(3):
        print(f"{matriz3[i][j]:5}", end="")
    print()