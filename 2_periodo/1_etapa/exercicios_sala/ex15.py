def soma_imposto(taxa, valor):
    custo = valor * (taxa/100)
    return custo + valor


taxa = float(input("\nInforme o valor da taxa em %: "))
preco = float(input("Digite o valor do produto em R$: "))
print(f"\nPreço: R${preco}\nTaxa:{taxa}%\nPreço final:{soma_imposto(taxa, preco)}")