from random import randint

def new_cpf():
	new_cpf_input = [None] * 11

	for i in range(len(new_cpf_input)):
		new_cpf_input[i] = randint(0, 9)
	
	return new_cpf_input
