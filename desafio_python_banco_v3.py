from datetime import datetime

# ------------------- DECORADOR -------------------
def log_transacao(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Executando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# ------------------- FUNÇÕES DO SISTEMA -------------------
def menu():
    return """
=========== MENU ===========
[1] Depositar em conta
[2] Sacar de conta
[3] Extrato de conta
[4] Criar Usuário
[5] Criar Conta
[6] Listar Contas
[7] Relatório de Transações
[8] Sair
============================
Escolha uma opção: """


@log_transacao
def depositar(conta, valor, /):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta['numero']}.")
    else:
        print("Valor inválido para depósito.")
    return conta


@log_transacao
def sacar(*, conta, valor, limite, numero_saques, limite_saques):
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("O valor excede o limite por saque.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques atingido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {conta['numero']}.")
    else:
        print("Valor inválido para saque.")
    return conta, numero_saques


@log_transacao
def exibir_extrato(conta, /):
    print(f"\n=========== EXTRATO CONTA {conta['numero']} ===========")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for item in conta["extrato"]:
            print(item)
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("================================")


# ------------------- USUÁRIOS E CONTAS -------------------
@log_transacao
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u["cpf"] == cpf), None)


@log_transacao
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero": numero_conta, "usuario": usuario, "saldo": 0, "extrato": []}
    else:
        print("Usuário não encontrado. Conta não criada.")
        return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""
Agência: {conta["agencia"]}
Conta: {conta["numero"]}
Titular: {conta["usuario"]["nome"]}
Saldo: R$ {conta["saldo"]:.2f}
------------------------------"""
        print(linha)


def buscar_conta(contas, numero):
    return next((c for c in contas if c["numero"] == numero), None)


# ------------------- GERADOR DE RELATÓRIOS -------------------
def gerador_transacoes(transacoes, tipo=None):
    for transacao in transacoes:
        if tipo is None or tipo.lower() in transacao.lower():
            yield transacao


# ------------------- PROGRAMA PRINCIPAL -------------------
usuarios = []
contas = []
AGENCIA = "0001"
LIMITE_SAQUES = 3
limite = 500

while True:
    opcao = input(menu())

    if opcao == "1":
        if not contas:
            print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
        else:
            numero = int(input("Número da conta: "))
            conta = buscar_conta(contas, numero)
            if conta:
                valor = float(input("Valor do depósito: "))
                depositar(conta, valor)
            else:
                print("Conta não encontrada.")

    elif opcao == "2":
        if not contas:
            print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
        else:
            numero = int(input("Número da conta: "))
            conta = buscar_conta(contas, numero)
            if conta:
                valor = float(input("Valor do saque: "))
                numero_saques = len([t for t in conta["extrato"] if "Saque" in t])
                conta, numero_saques = sacar(
                    conta=conta,
                    valor=valor,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )
            else:
                print("Conta não encontrada.")

    elif opcao == "3":
        if not contas:
            print("Nenhuma conta cadastrada. Crie uma conta primeiro.")
        else:
            numero = int(input("Número da conta: "))
            conta = buscar_conta(contas, numero)
            if conta:
                exibir_extrato(conta)
            else:
                print("Conta não encontrada.")

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "7":
        if not contas:
            print("Nenhuma conta para gerar relatório.")
        else:
            numero = int(input("Número da conta: "))
            conta = buscar_conta(contas, numero)
            if conta and conta["extrato"]:
                tipo_filtro = input("Deseja filtrar por [Depósito/Saque] ou deixar vazio para todas? ")
                for t in gerador_transacoes(conta["extrato"], tipo_filtro if tipo_filtro else None):
                    print(t)
            else:
                print("Conta não encontrada ou sem transações.")

    elif opcao == "8":
        print("Saindo... Obrigado por usar nosso sistema!")
        break

    else:
        print("Opção inválida. Tente novamente.")
