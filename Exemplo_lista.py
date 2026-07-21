# ===================================================
# CONCEITO: LISTA
# ===================================================
# Uma lista é como uma "caixa organizadora" que guarda
# vários valores, um do lado do outro, numa ordem fixa.
# Cada valor tem uma posição (índice), começando do 0.
#
# Índice:   0        1        2        3
# Lista:  ["maçã", "banana", "uva", "pera"]

frutas = ["maçã", "banana", "uva", "pera"]

# 1. Acessando um item pelo índice
print(frutas[0])   # maçã (primeiro item)
print(frutas[2])   # uva (terceiro item)

# 2. Descobrindo quantos itens a lista tem
print(len(frutas))  # 4

# 3. Adicionando um item no final
frutas.append("laranja")
print(frutas)  # ['maçã', 'banana', 'uva', 'pera', 'laranja']

# 4. Removendo um item
frutas.remove("banana")
print(frutas)  # ['maçã', 'uva', 'pera', 'laranja']

# 5. Alterando um item existente
frutas[0] = "morango"
print(frutas)  # ['morango', 'uva', 'pera', 'laranja']

# 6. Percorrendo (visitando) todos os itens da lista
for fruta in frutas:
    print("Fruta:", fruta)
