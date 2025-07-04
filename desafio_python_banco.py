menu = """
=========== MENU ===========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
============================
Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Por favor informe o valor que gostaria de depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação falhou! O valor informado é inválido, tente inserir um valor positivo e inteiro!")

    elif opcao == "2":
        valor = float(input("Por favor informe o valor que deseja sacar: "))

        saldo_insuficiente = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("A operação falhou! Verifique se possui saldo suficiente antes de tentar novamente:")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excede o limite diário de R$500,00.")

        elif excedeu_saques:
            print("A operação falhou! Você atingiu o número máximo de saques diários (3).")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("A operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print("Encerrando o sistema. Obrigado!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
