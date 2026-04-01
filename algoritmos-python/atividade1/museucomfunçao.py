COMBINACOES = {
    "frente": {"lanterna", "chave"},
    "servico": {"chave", "corda"},
    "telhado": {"lanterna", "corda"}
}

ITENS_VALIDOS = ["lanterna", "chave", "corda"]


def escolher_entrada():
    while True:
        entrada = input("Escolha a entrada (frente/servico/telhado): ").strip().lower()
        if entrada in COMBINACOES:
            return entrada
        print("Opção inválida!")


def desafio_frente():
    dados = input("Digite três valores (ex: 7 42 6.0): ").split()
    if len(dados) != 3:
        return False
    try:
        a = int(dados[0])
        b = int(dados[1])
        c = float(dados[2].replace(",", "."))
        return 294 % a == 0 and 294 // a == b and b / a == c
    except:
        return False


def desafio_servico():
    dados = input("Digite dois números inteiros: ").split()
    if len(dados) != 2:
        return False
    try:
        x = int(dados[0])
        y = int(dados[1])
        return x % y == 0 and y % 2 != 0 and x + y > 50
    except:
        return False


def desafio_telhado():
    dados = input("Digite três lados do triângulo: ").split()
    if len(dados) != 3:
        return False
    try:
        x, y, z = map(lambda v: float(v.replace(",", ".")), dados)
        return (x + y > z and x + z > y and y + z > x) and not (x == y == z)
    except:
        return False


def resolver_desafio(entrada):

    tentativas = 3

    while tentativas > 0:

        if entrada == "frente":
            resolvido = desafio_frente()

        elif entrada == "servico":
            resolvido = desafio_servico()

        else:
            resolvido = desafio_telhado()

        if resolvido:
            return tentativas

        tentativas -= 1
        print("Errado! Restam", tentativas, "tentativas.")

    return 0


def escolher_itens():

    while True:

        texto = input("Escolha DOIS itens: ").strip().lower()

        texto = texto.replace(" e ", " ")
        texto = texto.replace(",", " ")

        itens = texto.split()

        if len(itens) == 2 and itens[0] in ITENS_VALIDOS and itens[1] in ITENS_VALIDOS and itens[0] != itens[1]:
            return set(itens)

        print("Escolha inválida!")


def calcular_final(itens, entrada, tentativas):

    if itens != COMBINACOES[entrada]:
        print("Final: ruim")

    elif tentativas == 3:
        print("Final: supremo")

    elif tentativas == 2:
        print("Final: bom")

    else:
        print("Final: neutro")


# -------- PROGRAMA PRINCIPAL --------

while True:

    entrada = escolher_entrada()

    tentativas = resolver_desafio(entrada)

    if tentativas == 0:
        print("Você está fora!")

    else:
        print("\nVocê encontrou o depósito.")
        itens = escolher_itens()
        calcular_final(itens, entrada, tentativas)

    jogar = input("\nJogar novamente? (sim/nao): ").strip().lower()

    if jogar != "sim":
        break