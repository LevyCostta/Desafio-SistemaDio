#Desafio da DIO BOOTCAMP para criar um sistema bancario simples
import textwrap

def menu():
    menu = """--------------------------------
-=-=-=-=-=-=- MENU -=-=-=-=-=-=-
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova Conta
[5]\tListar Contas Cadastradas
[6]\tNovo Usuario
[7]\tSair
--------------------------------
Digite a opção desejada:"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f'Deposito: \tR$ {valor_deposito:.2f}\n'
        print('\nDEPOSITO REALIZAD COM SUCESSO!')
    
    else:
        print('Operação falhou, valor informado é invalido.')

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print('\nVocê não tem saldo o suficiente!')

    elif excedeu_limite:
        print('\nValor de saque excede o limite.')

    elif excedeu_saques:
        print('\nNumero maximo de saques excedido!!!')

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f'Saque: \t\tR$ {valor_saque:.2f}\n'
        numero_saques += 1
        print('\nSAQUE REALIZADO COM SUCESSO!')

    else: 
        print('\nValor informado, é invalido.')
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n-=-=-=-=-=-=- EXTRATO -=-=-=-=-=-=-')
    print('Não foram realizadas transações.' if not extrato else extrato)
    print(f'\nSaldo: \t\tR$: {saldo:.2f}')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def criar_usuario(usuarios):
    cpf = int(input('Informe o CPF (somente numeros): '))
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\nJá existe um usuario com esse CPF.')
        return
    
    nome = input('Informe seu nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, numero - bairro - cidade - sigla do estado): ')

    usuarios.append({'nome': nome, 'data_nascimento' : data_nascimento, 'cpf' : cpf, 'endereco' : endereco})

    print('\nUSUARIO CADASTRADO COM SUCESSO!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input('Informe o CPF do usuario: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('CONTA CRIADA COM SUCESSO!')
        return {'agencia' : agencia, 'numero_conta' : numero_conta, 'usuario' : usuario}
    print('\nUsuario não encontrado.')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta['agencia']}
        C\C: \t\t{conta['numero_conta']}
        Titular: \t{conta['usuario']['nome']}
        """
        print('='*100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        #DEPOSITO
        if opcao == '1':
            valor_deposito = float(input('Digite o valor que deseja depositar em sua conta: '))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
    
        elif opcao == '2':
            valor_saque = float(input('Digite o valor que deseja sacar: '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == '5':
            listar_contas(contas)
        elif opcao == '6':
            criar_usuario(usuarios)

        elif opcao == '7':
            break

        else:
            print('Opção invalida, tente novamente.')

main()