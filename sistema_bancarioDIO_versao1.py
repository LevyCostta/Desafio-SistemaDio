#Desafio da DIO BOOTCAMP para criar um sistema bancario simples

menu = """
1- Depositar
2- Sacar
3- Extrato
4- Sair

Digite a opção desejada:
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    print('='*50)
    print('SISTEMA BANCARIO DIO'.center(50))
    print('='*50)
    opcao = int(input(menu))
    #DEPOSITO
    if opcao == 1:
        valor_deposito = float(input('Digite o valor que deseja depositar em sua conta: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Deposito de R$ {valor_deposito:.2f} realizado com sucesso!\n'
    
        else:
            print('Operação falhou! O valor informado é invalido.')
    
    elif opcao == 2:
        valor_saque = float(input('Digite o valor que deseja sacar: '))

        exedeu_saldo = valor_saque > saldo

        exedeu_limite = valor_saque > saldo

        execedeu_saques = numero_saques > limite_saques

        if exedeu_saldo:
            print('Falha...Saldo insuficiente para saque.')
        elif exedeu_limite:
            print('Falha...Execedeu o limite especial.')
        elif execedeu_saques:
            print('Numero maximo de saques foi execedido!')
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f'Saque de R$ {valor_saque:.2f} realizado com sucesso!'
            numero_saques += 1
        else:
            print('Operação Falhou, numero invalido.')
    
    elif opcao == 3:
        print('*'*50)
        print('EXTRATO'.center(50))
        print('Não foram realizadas transações'if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print('*'*50)

    elif opcao == 4:
        break

    else:
        print('Opção invalida, tente novamente.')

        