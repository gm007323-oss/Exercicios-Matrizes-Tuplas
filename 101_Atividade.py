
matriz = []

# Solicitar os valores da matriz
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Calculo
a = matriz[0][0]
b = matriz[0][1]
c = matriz[0][2]

d = matriz[1][0]
e = matriz[1][1]
f = matriz[1][2]

g = matriz[2][0]
h = matriz[2][1]
i = matriz[2][2]

det = a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h

# resultado
print("\nO determinante da matriz é:", det)
