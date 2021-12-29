from os import system

def menu_options():
	system('clear')
	print('=+=' * 15)
	print('\t\t\t\tCPF TOOLS')
	print('=+=' * 15)

	print('\t1 \t------\t Gerar um CPF válido')
	print('\t2 \t------\t Verificar se CPF é válido')
	print('\t3 \t------\t Encerrar aplicação')
	print('---' * 15)
	
	option = str(input('Digite o valor da opção desejada: '))

	return option
