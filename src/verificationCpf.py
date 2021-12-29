def verifier_first_digit(cpf_argument):
	cpf = list(cpf_argument)
	
	soma = 0
	cont = 0
	for i in range(10, 1, -1):
		soma += (i * cpf[cont])
		cont += 1

	if (soma % 11 == 0 or soma % 11 == 1):
		cpf[-2] = 0
	else:
		cpf[-2] = (11 - (soma % 11))

	return cpf


def verifier_final_digit(cpf_argument):
	# cpf = list(cpf_argument)
	soma = 0
	cont = 0
	for i in range(11, 1, -1):
		soma += (i * cpf_argument[cont])
		cont += 1

	if (soma % 11 == 0 or soma % 11 == 1):
		cpf_argument[-1] = 0
	else:
		cpf_argument[-1] = (11 - (soma % 11))

	return cpf_argument


def validate_cpf():
	cpf_input = []
	aux = str(input('Digite o CPF: '))

	for i in range(len(aux)):
		cpf_input.append(int(aux[i]))

	if len(cpf_input) == 11:
		cpf = verifier_final_digit(verifier_first_digit(tuple(cpf_input)))

		if (cpf_input[-2] == cpf[-2]) and (cpf_input[-1] == cpf[-1]):
			print('O CPF digitado é válido :)')
		else:
			print('O CPF digitado não é válido :(')
	else:
		print('O número digitado não é um CPF...')
