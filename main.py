def validaDig(dig):
    return 11 - (dig % 11)

cpf = input('Digite o CPF para validação: ')
contador = 0
dig_validador1 = 10
dig_validador2 = 11
somaDig1 = 0
somaDig2 = 0
novo_cpf = ''

for x in range(9):
    numero = cpf[contador]
    somaDig1 += int(numero) * dig_validador1
    somaDig2 += int(numero) * dig_validador2
    dig_validador1 -= 1
    dig_validador2 -= 1
    contador += 1
    novo_cpf += numero

dig1 = validaDig(somaDig1)

if dig1 <= 9:
    somaDig2 += dig1 * 2
    novo_cpf += str(dig1)
else:
    novo_cpf += '0'

novo_cpf += str(validaDig(somaDig2))

if novo_cpf == cpf:
    print(f'CPF VALIDO, {novo_cpf}')
else:
    print(f'CPF INVALIDO, {novo_cpf}')