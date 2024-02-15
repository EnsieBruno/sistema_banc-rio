menu = """#### Sistema Bancário ####
   
    [d] Depósito
    [s] Saque
    [e] Extrato
    [q] Sair

##########################\n\n
  """

saldo = 0
saques = 0
extrato = []

LIMITE_SAQUES = 3

while True :

    print(menu)
      
    opcao_menu = input("Digite a opção desejada")

    if opcao_menu == "d":
        valor_deposito = float(input("Digite o valor a ser depositado: "))

        if valor_deposito >= 0:
            print("Realizando depósito ...\n")
            saldo += valor_deposito
            extrato.append(f"Depósito de R$ {valor_deposito:.2f}.")
            print(f"Seu novo saldo é de: R$ {saldo:.2f}.\n\n")   
        else:
            print("São permitidos apenas valores positivos.")

    elif opcao_menu == "s":
        if saques < LIMITE_SAQUES:
              valor_saque = float(input("Digite o valor do Saque: \n"))
              saques += 1
              
              if valor_saque <= saldo:
                  print("Realizando Saque ...")
                  saldo -= valor_saque
                  print(f"Seu novo saldo é de: R$ {saldo:.2f}.\n\n")
                  extrato.append(f"Saque de R$ {valor_saque:.2f}.")
              else:
                  print("Saldo insuficiente!! \n")
                  saques -=1
        else:
            print("Você atingiu o número máximo de saques diários \n")

    elif opcao_menu == "e":
        i = 0
        while i < len(extrato):
            print(extrato[i])
            i +=1
        if i == len(extrato):
            print(f"Seu saldo atual é de R$ {saldo:.2f}\n")
    elif opcao_menu == "q":
        print("Até mais, Obrigado por usar nosso Sistema Bancário")
        break
else:
        print("Opção inválida, selecione apenas uma das opções acima!! \n")