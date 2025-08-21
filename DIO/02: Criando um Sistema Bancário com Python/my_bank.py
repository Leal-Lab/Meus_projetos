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
saque = ""
limite_saques = 3

while True:
  opcao = input(menu)
  
  if opcao == "1":
    deposito = float(input('Digite o valor a depositar: '))
    if deposito > 0:
      saldo += deposito
      extrato += f'Depositado: R${deposito:.2f}̣\n'

  elif opcao == "2":
    saque = float(input('Digite o valor a retirar: '))
    if saque > 0 <= 500 and limite_saques <= 3:
      saldo = saque - saldo
      limite_saques += 1
      extrato += f' Sacado: R${saque:.2f} ({limite_saques}/3̣)\n'
    else:
      print ("Opcao invalida no momento")
      
  # elif opcao == "3":
  #   print ("extrato")
    
  #   for input in deposito:
  #     print (f'Deposito de R$ {deposito}')
    
  elif opcao == "0":
    break

else:
  print ("Opcao invalida!")
