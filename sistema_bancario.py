# v2
# feats: create and filter user, create and list accounts, new menu

# Menu de atividades bancárias
menu = """
|Digite para escolher sua operação:
|                                   |
|->   [d] Depositar             <-  |
|->   [s] Sacar                 <-  |
|->   [e] Ver extrato           <-  |
|->   [q] Sair                  <-  |
|                                   |
|––> """

# Menu de Login e Cadastro
enter_menu = """

|Digite para escolher sua operação: 
|                                   |
|                                   |
|->   [e] Entrar                <-  |
|->   [c] Criar Conta           <-  |
|                                   |
|                                   |
|––> """

# Variáveis
saldo = 0
limite = 500
numero_de_saques = 0
usuarios = []
contas = []

# Constantes
LIMITE_DE_SAQUES = 3
AGENCIA = "0001"

# Dicionários
usuario = {
    "nome": "",
    "data_de_nascimento": "",
    "cpf": 0,
    "endereço": {
        "rua": "",
        "numero": 0,
        "bairro": "",
        "cidade": "",
        "estado": "",
    },
}

conta = {"agencia": "0001", "numero": 0, "usuario": usuario["nome"]}


# Função para renderizar o menu após o Login
def render_menu():
    while True:
        opcao_menu = input(menu)
        if opcao_menu == "d":
            depositar()
        elif opcao_menu == "s":
            sacar()
        elif opcao_menu == "e":
            extrato()
        elif opcao_menu == "x":
            mostrar_dados(usuario, conta)
        elif opcao_menu == "f":
            filter_users(usuarios)
        elif opcao_menu == "l":
            list_users(usuarios)
            list_accounts(contas)
        elif opcao_menu == "q":
            main()


# Função de criação de usuário
def create_user(usuario):
    user = usuario["cpf"]
    usuario["cpf"] = input("Digite apenas os NÚMEROS do seu CPF: ").strip()

    if user:
        print("Este CPF já está sendo utilizado!")
        return main()

    usuario["nome"] = input("---> Nome completo: ").strip().title()
    usuario["data_de_nascimento"] = input("---> Sua data de nascimento: ").strip()
    usuario["endereço"]["rua"] = input("---> Nome da rua: ").strip().title()
    usuario["endereço"]["numero"] = input("---> Numero: ").strip()
    usuario["endereço"]["bairro"] = input("---> Bairro: ").strip().title
    usuario["endereço"]["cidade"] = input("---> Cidade: ").strip().title()
    usuario["endereço"]["estado"] = input("---> Estado (sigla):").strip().upper()

    usuarios.append(usuario)


# Função para filtrar usuários pelo número de CPF
def filter_users(usuarios):
    cpf = input("Digite o CPF para buscar pelo usuário")
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return print(usuario_filtrado[0]["nome"]) if usuario_filtrado else None


# Função de criação de conta bancária
def create_account(conta):
    conta["agencia"] = AGENCIA
    conta["numero"] = conta["numero"] + 1
    conta["usuario"] = usuario["cpf"]

    contas.append(conta)


# Função de listagem dde usuários
def list_users(usuarios):
    print("Usuários: ")
    for usuario in usuarios:
        print(f"{usuario['nome']}")


# Função de listagem de contas
def list_accounts(contas):
    for conta in contas:
        print(f"{conta}")


# Função de apresentação de dados do usuário
def mostrar_dados(usuario, conta):
    print(f"{usuario.items()}")
    print(f"{conta.items()}")


# Função de depósito
def depositar():
    global saldo
    valor_deposito = int(input("Digite o valor do depósito: "))
    novo_saldo = saldo + valor_deposito
    print(f"Você depositou: R${valor_deposito}")
    print(f"Seu saldo agora é de: R${novo_saldo}")
    saldo = novo_saldo


# Função de saque
def sacar():
    global saldo, numero_de_saques
    valor_saque = int(input("Digite o valor do saque: "))
    if valor_saque <= 500:
        if numero_de_saques < LIMITE_DE_SAQUES:
            if valor_saque <= saldo:
                saldo -= valor_saque
                print("   ")
                print(f"Você sacou: R${valor_saque}")
                numero_de_saques += 1
            else:
                print("   ")
                print("Você não possui saldo suficiente!")
        else:
            print("   ")
            print("Há um limite de 3 saques diários!")
    else:
        print("   ")
        print("Há um limite de R$500,00 para cada saque!")


# Função de exibição de extrato
def extrato():
    print(f"Extrato bancário: R${saldo}")


# Função Principal
def main():
    opcao = input(enter_menu)

    if opcao == "e":
        render_menu()
    elif opcao == "c":
        create_user(usuario)
        create_account(conta)
        print(f"Bem-vindo {usuario.get('nome')}!")
        render_menu()
    else:
        print("Operação inválida!")


main()
