import textwrap

def menu():
    menu = """\n
    ================ Menu ========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNovo cliente
    [lc]\tListar Contas
    [nu]\tNovo usuario
    [q]\tSair
    """

    return input(textwrap.dedent(menu))

def nova_conta(contas):
    cpf = input("CPF: ")
    for item in contas:
        if item['cpf'] == cpf:
            print(f"O CPF {cpf}, já existe no sistema.")
            return
    
    nome_completo = input('Nome completo: ')
    data_nascimento = input('Data de Nascimento: ')
    logradouro = input('Logradouro: ')
    numero_residencia = int(input('Número: '))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla_estado = input("Sigla do estado: ")
    endereco = f"{logradouro}, {numero_residencia} - {bairro} - {cidade}/{sigla_estado}"

    dados = {
            'cpf': cpf,
                'dados': {
                    'nome': nome_completo,
                    'data_nascimento': data_nascimento,
                    'endereco': endereco
                }
        }
    
    contas.append(dados)

    #endereco = input("Informe o Endereço: logradouro, número - bairro - cidade/sigla do estado: ")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    
    while True:
        opcao = menu()
        if opcao == "nc":
            print("Cadastrar novo cliente")
            nova_conta(contas)
        
        elif opcao == "lc":
            print("Listar contas")
        
        
        elif opcao == "nu":
            print("Criar novo usuário para uma conta existente")
        
        
        elif opcao == "d":
            print("Depositar valor em Conta")
        
        
        elif opcao == "s":
            print("Sacar valor da conta")
        
        
        elif opcao == "e":
            print("Extrato da conta")
        
        
        elif opcao == "q":
            print("Saindo do sistema...")
            break
    
main()