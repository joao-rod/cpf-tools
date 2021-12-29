from src.menu import menu_options
from src.cpfMask import mask_cpf
from src.setNewCpf import new_cpf
from src.clickEnter import click_enter
from src.verificationCpf import validate_cpf
from src.verificationCpf import verifier_first_digit
from src.verificationCpf import verifier_final_digit

while True:
	option = menu_options()
	
	if option == '1':
		mask_cpf(verifier_final_digit(verifier_first_digit(new_cpf())))
		click_enter()
	elif option =='2':
		validate_cpf()
		click_enter()
	elif option == '3':
		print('Você escolher sair...')
		break
	else:
		print('Digite uma opção válida...')
		click_enter()
