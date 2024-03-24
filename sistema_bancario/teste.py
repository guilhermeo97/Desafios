lista = []

def menu():
    print("""
        Bem vindo ao Sistema de RH
        [c] Cadastrar funcionário
        [e] Exibir funcionários
        [s] Cadastrar Salário
        [q] Sair  """)

def cadastrar_pessoa(): 
    cpf = input('CPF: ')
    for dicionario in lista:
        if dicionario['cpf'] == cpf:
            print(f'CPF {cpf} já cadastrado. Novo cadastro não permitido.')
            return 
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    dic = {
            'cpf': cpf,
                'dados': {
                    'nome': nome,
                    'sobrenome': sobrenome
                }
        }
    lista.append(dic)

def exibir_lista():
    print(lista)        

def cadastrar_salario():
    cpf_pesquisar = input('CPF: ')
    for dicionario in lista:
        if dicionario['cpf'] == cpf_pesquisar:
            salario = float(input('Salário: '))
            dicionario['dados']['Salario'] = salario
            break
        else:
            print(f'CPF {cpf_pesquisar} não encontrado.')
    

while True:
    menu()
    
    opcao = input('Digite a opção desejada: ')
    
    if opcao == 'c':
        cadastrar_pessoa() 
    
    elif opcao == 'e':
        exibir_lista()

    elif opcao == 's':
        cadastrar_salario()

    elif opcao == 'q':
        break
