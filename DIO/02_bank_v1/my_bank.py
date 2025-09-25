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
numero_saques = 0

while True:
  opcao = input(menu)
  
  if opcao == "1":
    deposito = float(input('Digite o valor a depositar: '))
    if deposito > 0:
      saldo += deposito
      extrato += f'Depositado: R${deposito:.2f}̣\n'

  elif opcao == "2":
    saque = float(input('Digite o valor a retirar: '))
   
    if saque > 0 and saque <= 500 and numero_saques <= 3:
      saldo -= saque
      numero_saques += 1
      extrato += f'Sacado: R${saque:.2f} ({numero_saques}/3̣)\n'
    else:
      print ("Opcao invalida no momento")
      
  elif opcao == "3":
    print (extrato)
    
    print(f'Saldo atual:   R${saldo}')

  elif opcao == "0":
    break

else:
  print ("Opcao invalida!")
