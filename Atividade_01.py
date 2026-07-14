

id_venda = input("Digite o ID da Venda: ")
data = input("Digite a Data: ")
vendedor = input("Diigikpoite o nome do Vendedor: ")
cliente = input("Digite o nome do Cliente: ")
produto = input("Digitie o nome do Produto: ")
categoria = input("Digiite a Categoria: ")

quantidade = int(input("Digite a Quantidade: "))


if quantidade >= 100:
    print("\nNão temos essa quantidade em estoque!")
else:
    preco_unitario = float(input("Digite o Preço Unitário: R$ "))

  
    valor_total = quantidade * preco_unitario

    # Forma de pagamento
    pagamento = input("Forma de pagamento ( À Vista -5% ou A Prazo +5% ): ")

    if pagamento == "à vista" or pagamento == "avista" or pagamento == "a vista":
        valor_total = valor_total * 0.95  
    elif pagamento == "a prazo":
        valor_total = valor_total * 1.05  
    else:
        print("Forma de pagamento inválida!")

    print("\n" + "=" * 40)
    print("         DADOS DA VENDA")
    print(f"ID da Venda: {id_venda}")
    print(f"Data: {data}")
    print(f"Vendedor: {vendedor}")
    print(f"Cliente: {cliente}")
    print(f"Produto: {produto}")
    print(f"Categoria: {categoria}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço Unitário: R$ {preco_unitario:.2f}")
    print(f"Forma de Pagamento: {pagamento.title()}")
    print(f"Valor Total Atualizado: R$ {valor_total:.2f}")
    print("=" * 40)