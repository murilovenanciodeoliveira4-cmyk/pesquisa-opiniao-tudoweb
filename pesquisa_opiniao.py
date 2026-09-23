"""Pesquisa de opiniao sobre o atendimento da TudoWeb."""

TOTAL_ENTREVISTADOS = 50


def pedir_idade():
    while True:
        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("Digite uma idade valida.")
            continue

        if idade > 0:
            return idade

        print("A idade deve ser maior que zero.")


def pedir_opiniao():
    while True:
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")

        try:
            opiniao = int(input("Digite a opcao: "))
        except ValueError:
            print("Digite 1, 2 ou 3.")
            continue

        if opiniao in (1, 2, 3):
            return opiniao

        print("Opcao invalida. Digite 1, 2 ou 3.")


def main():
    excelente = 0
    ruim = 0

    print("PESQUISA DE OPINIAO - TUDOWEB")
    print(f"A pesquisa sera realizada com {TOTAL_ENTREVISTADOS} entrevistados.")

    for numero in range(1, TOTAL_ENTREVISTADOS + 1):
        print(f"\n--- Entrevistado {numero} ---")

        nome = input("Nome: ").strip()

        while not nome:
            print("O nome nao pode ficar vazio.")
            nome = input("Nome: ").strip()

        pedir_idade()
        opiniao = pedir_opiniao()

        if opiniao == 1:
            excelente += 1
        elif opiniao == 3:
            ruim += 1

    print("\n===== RESULTADO DA PESQUISA =====")
    print(f"Quantidade de respostas EXCELENTE: {excelente}")
    print(f"Quantidade de respostas RUIM: {ruim}")


if __name__ == "__main__":
    main()
