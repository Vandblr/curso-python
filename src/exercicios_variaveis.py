from questionary import text, select
from datetime import date, datetime

def exercicios_dados_produto(): 
    nome = text("Digite o nome do produto:").ask()

    categoria = select(
        "Selecione a categoria do produto:",
        choices=[
            "Esportes",
            "Roupas Esportivas",
            "Calçados",
            "Acessórios",
            "Equipamentos",
            "Suplementos e Nutrição",
            "Marcas",
            "Ofertas e Categorias Especiais",
            "Outros"
        ]
    ).ask()

    quantidade = int(text("Digite a quantidade:").ask())
    preco = float(text("Digite o preço unitário:").ask())
    data_vencimento = text("Digite a data de vencimento (DD/MM/AAAA):").ask()

    try:
        data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y").date()
    except ValueError:
        print("⚠️ Data inválida! Use o formato DD/MM/AAAA.")
        return

    hoje = date.today()

    if data_vencimento < hoje:
        print("\n🛑 Produto vencido! Compra não permitida.")
        print("Nome do produto: " + nome)
        print("Categoria: " + categoria)
        print("Quantidade: " + str(quantidade))
        print("Preço unitário: R$ " + str(preco))
        print("Data de vencimento: " + data_vencimento.strftime("%d/%m/%Y"))
        return

    total = quantidade * preco 

    if categoria.lower() == "esportes":
        percentual = 10
    elif categoria.lower() == "roupas esportivas":
        percentual = 15
    elif categoria.lower() == "calçados":
        percentual = 20
    elif categoria.lower() == "acessórios":
        percentual = 12
    elif categoria.lower() == "equipamentos":
        percentual = 8
    elif categoria.lower() == "suplementos e nutrição":
        percentual = 5
    elif categoria.lower() == "marcas":
        percentual = 7
    elif categoria.lower() == "ofertas e categorias especiais":
        percentual = 25
    else:
        percentual = 0

    valor_desconto_categoria = total * (percentual / 100.0)

    desconto_extra = 0.0
    motivo_extra = "Nenhum"

    if data_vencimento == hoje:
        desconto_extra = 0.70 * valor_desconto_categoria
        motivo_extra = "Vence hoje: +70% sobre o desconto da categoria"
    elif data_vencimento.month == hoje.month and data_vencimento.year == hoje.year:
        desconto_extra = 20.00
        motivo_extra = "Vence neste mês: -R$ 20,00 fixo"

    total_descontos = valor_desconto_categoria + desconto_extra
    total_com_desconto = total - total_descontos

    cupom = select(
        "Selecione o cupom promocional (ou escolha 'Nenhum'):",
        choices=["Nenhum", "SUPER10", "PRIME20", "CLIENTEVIP", "FRETEGRATIS"]
    ).ask()

    desconto_cupom = 0.0
    frete_gratis_cupom = False

    if cupom == "Nenhum":
        pass
    elif cupom == "SUPER10":
        desconto_cupom = total_com_desconto * 0.10
    elif cupom == "PRIME20":
        desconto_cupom = total_com_desconto * 0.20
    elif cupom == "CLIENTEVIP":
        desconto_cupom = total_com_desconto * 0.25
    elif cupom == "FRETEGRATIS":
        frete_gratis_cupom = True

    total_com_desconto_final = total_com_desconto - desconto_cupom

    regiao = select(
        "Selecione a região de entrega:",
        choices=["Sul", "Sudeste", "Centro-Oeste", "Norte", "Nordeste"]
    ).ask()

    if regiao.lower() == "sul":
        frete = 25.00
    elif regiao.lower() == "sudeste":
        frete = 35.00
    elif regiao.lower() == "centro-oeste":
        frete = 45.00
    elif regiao.lower() == "norte":
        frete = 55.00
    elif regiao.lower() == "nordeste":
        frete = 50.00
    else:
        frete = 50.00

    if total_com_desconto_final > 500 or frete_gratis_cupom:
        frete = 0.00

    total_final = total_com_desconto_final + frete

    print("\n🧾 RESUMO DO PEDIDO")
    print("------------------------------------")
    print("Produto: " + nome)
    print("Categoria: " + categoria)
    print("Quantidade: " + str(quantidade))
    print("Preço Unitário: R$ " + "{:.2f}".format(preco))
    print("Total Bruto: R$ " + "{:.2f}".format(total))
    print("Desconto Categoria (" + str(percentual) + "%): R$ " + "{:.2f}".format(valor_desconto_categoria))
    print("Desconto Cupom: R$ " + "{:.2f}".format(desconto_cupom))
    print("Desconto Extra: R$ " + "{:.2f}".format(desconto_extra))
    print("Frete: R$ " + "{:.2f}".format(frete))
    print("------------------------------------")
    print("💰 Total a Pagar: R$ " + "{:.2f}".format(total_final))
    print("📅 Vencimento: " + data_vencimento.strftime("%d/%m/%Y"))
    print("📦 Região: " + regiao)
    print("------------------------------------")
    print("Obrigado por comprar conosco! 😄")
