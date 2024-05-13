menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso!')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print('Operação falhou!: Saldo suficiente.')
    
        elif excedeu_limite:
            print('Operação falhou!: Valor do saque excede o limite.')
    
        elif excedeu_saques:
            print('Operação falhou!:Número de saques diários excedidos.')
    
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso!')
    
    elif opcao == 'e':
        print('\n================ EXTRATO ================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('==========================================')

    elif opcao == 'q':
        print('Saindo...') 
        break
        
    else:
        print('Operação inválida: Por favor selecione novamente a operação desejada.Caiu no else')
