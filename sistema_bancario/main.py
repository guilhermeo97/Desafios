extrato = []
clientes = []
cadastros_clientes = {}
saldo = 0
LIMITE_SAQUES_VALOR = 500
LIMITE_SAQUES_QTD = 3
num_saques = 1
conta = {}
contagem_contas = []
agencia = []
usuario = []

menu = print("""
        Bem vindo ao Sistema Bancário Banrisul
        [c] cadastrar novo cliente
        [n] cadastrar novo cliente
        [d] depósito
        [s] saque
        [e] extrato
        [l] listar clientes
        [q] sair
        """)


def cadastro_cliente(cadastros_clientes):
    if cadastros_clientes is None:
        cpf_cliente = input("Digite o CPF do cliente: ")
        while (len(cpf_cliente) < 11 and len(cpf_cliente) > 14):
            print("O cpf digitado é inválido")
            cpf_cliente = input("Digite o CPF do cliente: ")
    else:
        cpf_cliente = input("Digite o CPF do cliente: ")
        while (len(cpf_cliente) < 11 and len(cpf_cliente) > 14) or cpf_cliente in cadastros_clientes:
            print("O cpf digitado é inválido")
            cpf_cliente = input("Digite o CPF do cliente: ")
    
    nome_cliente = input("Digite o nome completo do cliente: ")
    while not nome_cliente or len(nome_cliente) <= 3:
        print("O nome é obrigatório")
        nome_cliente = input("Digite o nome completo do cliente: ")
    
    dt_nascimento_cliente = input("Digite a data de nascimento no formato 'dd/mm/aaaa': ")
    while len(dt_nascimento_cliente) != 10:
        print("Data de nascimento incorreta!")
        nome_cliente = input("Digite a data de nascimento no formato 'dd/mm/aaaa': ")

    endereco_logradouro_cliente = input("Digite o logradouro do cliente: ")
    while not endereco_logradouro_cliente or len(endereco_logradouro_cliente) < 5:
        print("O logradouro é obrigatório")
        endereco_logradouro_cliente = input("Digite o logradouro do cliente: ")

    endereco_numero_cliente = input("Digite o número do cliente: ")
    while not endereco_numero_cliente:
        print("O número é obrigatório")
        endereco_logradouro_cliente = input("Digite o número do cliente: ")
    
    endereco_bairro_cliente = input("Digite o bairro do cliente: ")
    while not endereco_bairro_cliente or len(endereco_bairro_cliente) <= 3:
        print("O bairro é obrigatório")
        endereco_bairro_cliente = input("Digite o bairro do cliente: ")

    endereco_cidade_cliente = input("Digite a cidade do cliente: ")
    while not endereco_cidade_cliente or len(endereco_cidade_cliente) <= 3:
        print("A cidade é obrigatória")
        endereco_cidade_cliente = input("Digite a cidade do cliente: ")
    
    endereco_uf_cliente = input("Digite a sigla do estado do cliente: ")
    while len(endereco_uf_cliente) != 2:
        print("A sigla do estado é obrigatória")
        endereco_uf_cliente = input("Digite a sigla do estado do cliente: ")

    endereco_unificado_cliente = f'{endereco_logradouro_cliente}, {endereco_numero_cliente} - {endereco_bairro_cliente} - {endereco_cidade_cliente}/{endereco_uf_cliente.upper()}'
    
    cadastros_clientes = {
        cpf_cliente: {
        'nome': nome_cliente,
        'data_nascimento': dt_nascimento_cliente,
        'endereco': endereco_unificado_cliente,
        'conta': {}
        }
    }

    clientes.append(cadastros_clientes)
    return clientes


def cadastrar_conta(conta, usuario, cadastro_clientes):
    codigo_conta = str(len(contagem_contas) + 1)
    if cadastro_clientes is None:
        print("Não há clientes cadastrdos!")
    else:
        cpf_cliente_2 = input("Digite o CPF do cliente: ")
        while cpf_cliente_2 not in cadastro_clientes:
            print("O CPF digitado não foi encontrado")
            cpf_cliente_2 = input("Digite o CPF do cliente: ")
        
        usuario_cliente = input("Digite o nome de usuário do cliente: ")
        while not usuario_cliente or len(usuario_cliente) <= 3 or usuario_cliente in usuario:
            print("O nome de usuário é obrigatório")
            usuario_cliente = input("Digite o nome de usuário do clientek ")
        
        conta.append(codigo_conta)
        

        print(conta)
        cadastros_clientes[cpf_cliente_2]['conta'][codigo_conta] = {'usuario': usuario_cliente, 'agencia': '0001'} 

        print(clientes)

    

def depositar():
    global saldo
    valor_deposito = float(input("Digite o valor que você quer depositark "))
    while valor_deposito <= 0:
        print("Valor inválido, digite um valor maior que R$ 0,00")
        valor_deposito = float(input("Digite o valor que você quer deposktar: "))
    saldo += valor_deposito
    valor_extrato = str("Depsósito " + "R$ {:.2f}".format(valor_deposito))
    extrato.append(valor_extrato)

def sacar():
    global saldo
    global num_saques
    valor_saque = float(input("Digite o valor que você quer sacar: ")) 
    if valor_saque <= 0 or valor_saque > LIMITE_SAQUES_VALOR:
        print("Valor inválido, digite um valor maior que R$ 0.00 e menorkou igual a R$ 500.00")
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

def imprimir_extrato():
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
while True:
    print(clientes)
    print(cadastros_clientes)
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "d":
        depositar()     
        
    elif opcao == "s":
        sacar()
    elif opcao == "c":
        cadastro_cliente(cadastros_clientes)                 
        cadastrar_conta(contagem_contas, usuario, cadastros_clientes)
    elif opcao == "e":
        imprimir_extrato()

    elif opcao == "n":
        cadastrar_conta(contagem_contas, usuario, dados)
    elif opcao == "l":
        print(clientes)
    
    else:
        break      