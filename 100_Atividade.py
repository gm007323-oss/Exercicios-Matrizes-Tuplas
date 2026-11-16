
matriz = []

# Solicitar os valores da matriz 3x3
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

identidade = True

for i in range(3):
    for j in range(3):
        if i == j:
            if matriz[i][j] != 1:
                identidade = False
        else:
            if matriz[i][j] != 0:
                identidade = False

# resultado
if identidade:
    print("\nA matriz informada é uma matriz identidade!")
else:
    print("\nA matriz informada NÃO é uma matriz identidade!")
