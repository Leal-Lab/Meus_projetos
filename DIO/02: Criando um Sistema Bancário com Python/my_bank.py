'''
 Criar um sistema bancário com as operações:
    sacar, depositar e visualizar extrato.
'''

menu = """

[1] Depositar
[2] Sacar
[3] extrato
[0] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
  opcao = input(menu)
  
  if opcao == 1:
    print ("depósito")
  
  elif opcao == 2:
    print ("saque")
  
  elif opcao == 3:
    print ("extrato")
  
  elif opcao == 0:
    break
