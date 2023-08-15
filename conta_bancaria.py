from time import sleep
depositos = []
saques = []
saldo = 0
limite = 500
numero_saques = 0
numero_saques_restantes = 3
LIMITE_SAQUES = 3
extrato = []


while True:
    print('=-' * 63)
    print(' ' * 40 + 'Seja Benvindo ao Banco Martins Desenvolvedor')
    print('''
        Painel de Operações:
        
           [d] Depositar
           [s] Sacar
           [e] Extrato
           [q] Sair
           ''')
    opcao = input('Qual operação deseja realizar? ').lower()

    if opcao == 'd':
        deposito = float(input('Qual valor você quer depositar? '))
        if deposito > 0:
            depositos.append(deposito)
            print('Depósito efetuado com sucesso!')
            saldo += deposito
        else:
            print('Valor insuficiente para depósito, tente um valor acima de 0!')


    elif opcao == 's':
        saque = float(input('Qual valor você quer sacar? '))
        if numero_saques >= LIMITE_SAQUES:
            print('Operação Inválida! Limite de saque diário atingido!')

        elif saldo < saque:
            print('Operação Inválida! Saldo Insuficiente!')

        elif saque > limite:
            print('Operação Inválida! O limite de saque é de R$ 500,00')

        else:
            saques.append(saque)
            print('Saque efetuado com sucesso!')
            saldo -= saque
            numero_saques += 1
            numero_saques_restantes -= 1
            print(f'Você ainda pode fazer {numero_saques_restantes} saques!')

    elif opcao == 'e':

        print('=-' * 63)
        print(' ' * 15 + 'Exibindo Extrato:')
        print(f'Depósitos realizados:     =>', end=' ')
        for i in depositos:
            print(f'R$ {i:.2f}, ', end=' ')
        print()
        print(f'Saques realizados:        =>', end=' ')
        for c in saques:
            print(f'R$ {c:.2f}, ', end=' ')
        print()
        print(f'Seu saldo atual é:        => R$ {saldo:.2f}')

    elif opcao == 'q':
        print('Finalizando Programa...')
        sleep(2)
        print('Volte Sempre!!!')
        break

    else:
        print('Opção Inválida! Tente novamente!')

