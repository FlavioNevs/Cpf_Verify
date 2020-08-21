cont1 = 10
soma = 0
try:
    cpf = input('Digite o cpf: ')

    #   Verificar 1° Digito
    if len(cpf) == 11:
        for num in cpf[:-2]:
            soma = soma + (int(num) * cont1)
            cont1 -= 1
    else:
        print('Caracteres insuficientes.')
    cont1 = 11
    vld1 = 11 - (soma % 11)
    if vld1 >= 10:
        vld1 = str(0)
    else:
        vld1 = str(vld1)
    soma = 0

    # Verificar 2° Digito
    for num in cpf[:-1]:
        soma = soma + (int(num) * cont1)
        cont1 -= 1
    vld2 = 11 - (soma % 11)
    if vld2 >= 10:
        vld2 = str(0)
    else:
        vld2 = str(vld2)
    validador = int(vld1 + vld2)

    #  Validando
    if int(cpf[9:]) == validador:
        print('CPF Válido!')
    else:
        print('Cpf Inválido!')
except:
    print('Error')
