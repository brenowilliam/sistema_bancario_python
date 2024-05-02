menu = """

[1] Depositar
[2] Sacar 
[3] Extrato
[4] Sair 

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "2":
        valor = float(input("Informe o valor do Saque: "))
        
        excedeu_saque = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite = valor > LIMITE_SAQUES

        if excedeu_saque:
          print("Voce nao tem saldo suficiente para realizar essa operaçao")

        elif excedeu_limite:
          print("Voce ultrapassou seu limite")

        elif excedeu_limite:
          print("Voce ultrapassou o limite de Saques")

        elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques += 1

        else:
          print("Operação falhou! O valor informado é inválido.")
        
 
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas operaçoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================")


    elif opcao == "4":
        break

    else:
        print("Operacao Invalida,Tente Novamente")