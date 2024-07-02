menu = """
==================MENU==================


[d] Depósito
[s] Saque
[e] Extrato
[q] Sair


========================================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        vl = float(input("Qual valor você gostaria de depositar?\n"))

        if vl > 0:
            saldo += vl
            extrato += f"Depósito: R${vl:.2f}\n"

        else:
            print("O valor informado é inválido.")

    elif opcao == "s":
        vl = float(input("Qual valor você gostaria de sacar?\n"))

        esaldo = vl > saldo
        elimmite = vl > limite
        esaque = numero_saques >= LIMITE_SAQUES

        if esaldo:
            print("O valor de saque excedeu o valor em seu saldo, por favor consulte o seu saldo e realize novamente a operação.")

        elif elimmite:
            print("O limite de saque é R$500,00, por favor tente novamente com um valor menor.")

        elif esaque:
            print("O número de saques de hoje foi excedido, tente novamente amanhã.")

        elif vl > 0:
            saldo -= vl
            numero_saques =+ 1
            extrato += f"Saque: R${vl:.2f}\n"

        else:
            print("Operação falhou! O número informado é inválido")

    elif opcao == "e":
        print("\n======EXTRATO======")
        print("Não fortam realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor tente novamente.")
