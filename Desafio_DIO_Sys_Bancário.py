class Conta:
    def __init__(self, numero):
        self._numero = numero
        self._saldo = 0.0
        self._nome = None
        self._saques = 0

    def get_numero(self):
        return self._numero

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_saques(self):
        return self._saques

    def set_saques(self, saques):
        self._saques = saques


def deposita(conta, valor):
    saldo = conta.get_saldo()
    if valor >= 0:
        saldo += valor
        conta.set_saldo(saldo)
        extrato.append(f"Depósito de R$ {valor:.2f}.")
        return saldo
    else:
        raise ValueError("São permitidos apenas valores positivos.")

def sacar(conta):
    saques = conta.get_saques()
    if saques < LIMITE_SAQUES:
        valor = float(input("Digite o valor do Saque: \n"))
        saques += 1
        saldo = conta.get_saldo()
        if valor <= saldo:
            saldo -= valor
            conta.set_saldo(saldo)
            conta.set_saques(saques)
            extrato.append(f"Saque de R$ {valor:.2f}.")
            return saldo
        else:
            print("Saldo insuficiente!! \n")
            saques -= 1
    else:
        print("Você atingiu o número máximo de saques diários \n")

def criar_conta(numero):
    if numero not in contas:
        contas[numero] = Conta(numero)
        print("Conta criada com sucesso, e pronta para usar!!")
        return True
    else:
        print("Conta já existe")
        return False

def cadastrar_usuario(conta, nome):
    if conta in contas:
        contas[conta].set_nome(nome)
        print(f"Conta criada com sucesso , {conta} para o usuario {contas[conta].get_nome()}")
        return True
    else:
        print("Conta não existe, crie a conta antes de atribuir um usuário!")
        return False

extrato = []
contas = {}
saldo = 0.0
LIMITE_SAQUES = 3  # Defina o limite de saques diários

# Defina a variável 'menu'
menu = """#### Sistema Bancário ####
   
    [d] Depósito
    [s] Saque
    [e] Extrato
    [c] Criar Conta
    [u] Atribuir conta 
    [q] Sair

##########################\n\n
"""

while True:
    opcao_menu = input(menu)

    if opcao_menu == "d":
        numero_conta = input("Digite o número da conta: ")
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta = contas.get(numero_conta)
        if conta:
            saldo = deposita(conta, valor_deposito)
            print(f"Depósito realizado. Saldo atual: R$ {saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao_menu == "s":
        numero_conta = input("Digite o número da conta: ")
        conta = contas.get(numero_conta)
        if conta:
            saldo = sacar(conta)
            if saldo is not None:
                print(f"Saque realizado. Saldo atual: R$ {saldo:.2f}")
        else:
            print("Conta não encontrada.")

    elif opcao_menu == "e":
        for operacao in extrato:
            print(operacao)
        if saldo:
            print(f"Seu saldo atual é de R$ {saldo:.2f}\n")
        else:
            print("Sem operações realizadas.\n")

    elif opcao_menu == "c":
        numero_conta = input("Digite o número da conta: ")
        criar_conta(numero_conta)

    elif opcao_menu == "u":
        numero_conta = input("Digite o número da conta: ")
        nome_usuario = input("Digite o nome do usuário: ")
        cadastrar_usuario(numero_conta, nome_usuario)

    elif opcao_menu == "q":
        print("Até mais, Obrigado por usar nosso Sistema Bancário")
        break

    else:
        print("Digite uma opção válida!!")
