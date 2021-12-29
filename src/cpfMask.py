def mask_cpf(cpf):
	cpf_format = []
	for i in range(len(cpf)):
		cpf_format.append(str(cpf[i]))

	cpf_format.insert(3, '.')
	cpf_format.insert(7, '.')
	cpf_format.insert(11, '-')
	cpf_formated = ''.join(cpf_format)
	print(cpf_formated)

	return cpf_formated
