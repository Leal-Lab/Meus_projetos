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
  
  if opcao == "1":
    deposito = (float(input('Digite o valor a depositar: ')))
    if deposito > 0:
      saldo += deposito
      extrato += f'Depositado: R${deposito:.2f}̣\n'


  elif opcao == "2":
    print("Depois eu monto essa parte..")
  # elif opcao == "3":
  #   print ("extrato")
    
  #   for input in deposito:
  #     print (f'Deposito de R$ {deposito}')
    
  elif opcao == "0":
    break

else:
  print ("Opcao invalida!")
