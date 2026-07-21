# Exemplo simples de vetor em Python (lista)

vetor = [10, 20, 30, 40, 50]

# Exibindo o vetor
print("Vetor:", vetor)

# Acessando um elemento específico (posição 2)
print("\nElemento na posição 2:", vetor[2])

# Percorrendo o vetor
print("\nElementos do vetor:")
for i, valor in enumerate(vetor):
    print(f"Posição {i}: {valor}")

# Somando todos os elementos
soma = 0
for valor in vetor:
    soma += valor

print("\nSoma de todos os elementos:", soma)

# Encontrando o maior e o menor valor
print("Maior valor:", max(vetor))
print("Menor valor:", min(vetor))
