def criar_ccr(nconta, agencia):
    while True:
        cpf = input("Digite o CPF à qual deseja atribuir a conta:\n").replace(".", "").replace("-", "")
        if any(user['cpf'] == cpf for user in users):
            conta = {"numero": nconta, "agencia": agencia, "cpf": cpf}
            nconta += 1
            break
        else:
            print(f"Por favor, cadastre um usuário com o CPF: {cpf} ou insira corretamente o valor do mesmo!")      
    return nconta, conta

def show_ccr(contas):
    if not contas:
        print("================== Nenhuma Conta Cadastrada ==================")
    else:
        print("================== Contas Cadastradas ==================")
        for ct in contas:
            print(f"Conta Número: {ct['numero']}, Agência: {ct['agencia']}, CPF: {ct['cpf']}")
        print("=======================================================")

def criar_usu(users):
    while True:
        cpf = input("Digite o seu CPF, sem o uso da pontuação:\n").replace(".", "").replace("-", "")
        if any(user['cpf'] == cpf for user in users):
            print("CPF já cadastrado. Tente novamente.")
        else:
            break
    
    nome = input("Digite o seu nome:\n")
    data_nasc = input("Digite a sua data de nascimento: (ex: 12/34/5678)\n")
    logradouro = input("Digite o nome de sua rua:\n")
    nmr = input("Digite o número de sua residência:\n")
    bairro = input("Digite o nome do seu bairro:\n")
    uf = input("Digite apenas a sigla do estado em que reside:\n").upper()
    
    usuario = {
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "endereco": {
            "logradouro": logradouro,
            "nmr": nmr,
            "bairro": bairro,
            "UF": uf
        }
    }
    
    return usuario

def show_users(users):
    if not users:
        print("================== Nenhum Usuário Cadastrado ==================")
    else:
        print("================== Usuários Cadastrados ==================")
        for i, usuario in enumerate(users, start=1):
            print(f"\nUsuário {i}:")
            print(f"Nome: {usuario['nome']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Endereço: {usuario['endereco']['logradouro']}, {usuario['endereco']['nmr']}, {usuario['endereco']['bairro']}, {usuario['endereco']['UF']}")
        print("=======================================================")

def dep(sld, valor, ext, /):
    if valor > 0:
        sld += valor
        ext += f"Depósito: R${valor:.2f}\n"
    else:
        print("O valor informado é inválido.")
    return sld, ext

def saque(*, sld, valor, ext, limite, nsaques, lsaques):
    esaldo = valor > sld
    elimmite = valor > limite
    esaque = nsaques >= lsaques

    if esaldo:
        print("O valor de saque excedeu o valor em seu saldo, por favor consulte o seu saldo e realize novamente a operação.")
    elif elimmite:
        print("O limite de saque é R$500,00, por favor tente novamente com um valor menor.")
    elif esaque:
        print("O número de saques de hoje foi excedido, tente novamente amanhã.")
    elif valor > 0:
        sld -= valor
        nsaques += 1
        ext += f"Saque: R${valor:.2f}\n"
    else:
        print("Operação falhou! O número informado é inválido")
    return sld, ext, nsaques

def exibir_extrato(sld, /, *, ext):
    print("\n======EXTRATO======")
    print("Não foram realizadas movimentações." if not ext else ext)
    print(f"\nSaldo: R$ {sld:.2f}")        
    print("=====================")

menu = """
==================MENU==================

[d] Depósito
[s] Saque
[e] Extrato
[c] Criar Usuário
[u] Mostrar Usuários
[p] Criar Conta Corrente
[o] Mostrar Contas
[q] Sair

========================================

=> """

LIMITE_SAQUES = 3
AGENCIA = "001"

users = []
contas = []
extrato = ""

saldo = 0   
limite = 500
numero_saques = 0
nmr_conta = 1


while True:
    opcao = input(menu).lower()

    if opcao == "d":
        vl = float(input("Qual valor você gostaria de depositar?\n"))
        saldo, extrato = dep(saldo, vl, extrato)
    elif opcao == "s":
        vl = float(input("Qual valor você gostaria de sacar?\n"))
        saldo, extrato, numero_saques = saque(sld=saldo, valor=vl, ext=extrato, limite=limite, nsaques=numero_saques, lsaques=LIMITE_SAQUES)
    elif opcao == "e":
        exibir_extrato(saldo, ext=extrato)
    elif opcao == "c":
        usuario = criar_usu(users)
        users.append(usuario)
        print("Usuário criado com sucesso!")
    elif opcao == "u":
        show_users(users)
    elif opcao == "p":
        nmr_conta, conta_nova = criar_ccr(nmr_conta, AGENCIA)
        contas.append(conta_nova)
    elif opcao == "o":
        show_ccr(contas)
    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor, tente novamente com alguma opção presente no painel!")
