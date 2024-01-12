menu = print("""
        Bem vindo ao Sistema Bancário Banrisul
        [d] depósito
        [s] saque
        [e] extrato
        [q] sair""")

extrato = []
saldo = 0
LIMITE_SAQUES_VALOR = 500
LIMITE_SAQUES_QTD = 3
num_saques = 1

def depositar():
    global saldo
    valor_deposito = float(input("Digite o valor que você quer depositar: "))
    while valor_deposito <= 0:
        print("Valor inválido, digite um valor maior que R$ 0,00")
        valor_deposito = float(input("Digite o valor que você quer depositar: "))
    saldo += valor_deposito
    valor_extrato = str("Depsósito " + "R$ {:.2f}".format(valor_deposito))
    extrato.append(valor_extrato)

while True:
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "d":
        depositar()
        # valor_deposito = float(input("Digite o valor que você quer depositar: "))
        # while valor_deposito <= 0:
        #     print("Valor inválido, digite um valor maior que R$ 0,00")
        #     valor_deposito = float(input("Digite o valor que você quer depositar: "))
        # saldo += valor_deposito
        # valor_extrato = str("Depsósito " + "R$ {:.2f}".format(valor_deposito))
        # extrato.append(valor_extrato)
        
        
        
    elif opcao == "s":
        
        valor_saque = float(input("Digite o valor que você quer sacar: "))
        
        if valor_saque <= 0 or valor_saque > LIMITE_SAQUES_VALOR:
            print("Valor inválido, digite um valor maior que R$ 0.00 e menor ou igual a R$ 500.00")
            valor_saque = float(input("Digite o valor que você quer sacar: "))
        elif valor_saque > saldo:
            print("Valor de saque maior do que o saldo disponível em conta")
            valor_saque = float(input("Digite o valor que você quer sacar: "))
        elif num_saques > LIMITE_SAQUES_QTD:
            print("Número de saques diários excedido!")
        else:
            saldo -= valor_saque
            valor_extrato = str("Saque " + "R$ {:.2f}".format(valor_saque))
            extrato.append(valor_extrato)
            num_saques += 1
            
            
    elif opcao == "e":
        print()
        if not extrato:
            print("Não foram realizadas movimentações.")
            print()
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
        else:    
            for i in extrato:
                print(i)
            print()
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
    else:
        break      