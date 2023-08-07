saldo = 0
limite_diario = 0
extrato = []
import os

def depositar():
    global saldo
    while True:
        valor_deposito = float(input("Informe o valor que deseja depositar: "))
        if valor_deposito >= 0:
            while True:
                confirmacao = input(f"O valor do depósito será de R$ {valor_deposito:.2f}. Está correto? (S/N): ")
                if confirmacao.upper() == "S":
                    saldo += valor_deposito
                    extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
                    os.system("cls")
                    print(f"O valor de R$ {valor_deposito:.2f} foi depositado em sua conta com sucesso!")
                    break
                elif confirmacao.upper() == "N":
                    os.system("cls")
                    valor_deposito = float(input("Informe o novo valor que deseja depositar: "))
                else:
                    os.system("cls")
                    print("Opção inválida. Digite 'S' para confirmar ou 'N' para alterar o valor do depósito.")
            break
        else:
            os.system("cls")
            print("Valor inválido. Digite um valor positivo para depositar ou 0 para cancelar.")

def sacar():
    global saldo, limite_diario
    limite = 500
    if limite_diario >= 3:
        os.system("cls")
        print("Limite de 3 saques diários atingido. Não é possível fazer mais saques hoje.")
        return
    while True:
        valor_saque = float(input("Informe o valor que deseja sacar da sua conta: "))
        if valor_saque >= 0:
            if valor_saque <= limite:
                if valor_saque <= saldo:
                    while True:
                        confirmacao = input(f"O valor do saque será de R$ {valor_saque:.2f}. Está correto? (S/N): ")
                        if confirmacao.upper() == "S":
                            if limite_diario < 3:
                                saldo -= valor_saque
                                limite_diario += 1
                                extrato.append(f"Saque: R$ {valor_saque:.2f}")
                                os.system("cls")
                                print(f"O valor de R$ {valor_saque:.2f} foi sacado de sua conta com sucesso!")
                            else:
                                os.system("cls")
                                print("Limite de 3 saques diários atingido. Não é possível fazer mais saques hoje.")
                            break
                        elif confirmacao.upper() == "N":
                            os.system("cls")
                            valor_saque = float(input("Informe o novo valor que deseja sacar: "))
                        else:
                            os.system("cls")
                            print("Opção inválida. Digite 'S' para confirmar ou 'N' para alterar o valor do saque.")
                    break
                else:
                    os.system("cls")
                    print("Saldo insuficiente. Digite um valor menor ou igual ao saldo disponível.")
            else:
                os.system("cls")
                print("Não autorizado. Sua conta possui limite de R$ 500,00 por saque. Digite um valor válido para sacar ou 0 para cancelar.")
        else:
            os.system("cls")
            print("Valor inválido. Digite um valor positivo para sacar ou 0 para cancelar.")

def exibir_menu():
    
    print("""
SISTEMA BANCÁRIO

****** MENU ******
[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo
[5] Sair
""")
    

def imprimir_extrato():
    os.system("cls")
    print("\nExtrato da Conta:")
    print("-" * 30)
    for transacao in extrato:
        print(transacao)
    print("-" * 30)

def saldo_conta():
    os.system("cls")
    print(f"O saldo da sua conta é de R$ {saldo:.2f}.")
    

exibir_menu()
while True:
    opcao = input("Escolha a opção desejada: ")
    if opcao == "1":
        depositar()
    elif opcao == "2":
        sacar()
    elif opcao == "3":
        imprimir_extrato()
    elif opcao == "4":
        saldo_conta()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Escolha uma opção válida do menu.")
        os.system("cls")
    exibir_menu()
