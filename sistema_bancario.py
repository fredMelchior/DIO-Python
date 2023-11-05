# v1
menu = """
Digite para escolher sua operação:

[d] Depositar
[s] Sacar
[e] Ver extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_de_saques = 0
LIMITE_DE_SAQUES = 3


def depositar():
    global saldo
    valor_deposito = int(input("Digite o valor do depósito: "))
    novo_saldo = saldo + valor_deposito
    print(f"Você depositou: R${valor_deposito}")
    print(f"Seu saldo agora é de: R${novo_saldo}")
    saldo = novo_saldo


def sacar():
    global saldo, numero_de_saques
    valor_saque = int(input("Digite o valor do saque: "))
    if valor_saque <= 500:
        if numero_de_saques < LIMITE_DE_SAQUES:
            if valor_saque <= saldo:
                saldo -= valor_saque
                print(f"Você sacou: R${valor_saque}")
                numero_de_saques += 1
            else:
                print("Você não possui saldo suficiente!")
        else:
            print("Há um limite de 3 saques diários!")
    else:
        print("Há um limite de R$500,00 para cada saque!")


def extrato():
    print(f"Extrato bancário: R${saldo}")


while True:
    opcao = input(menu)

    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida!")
