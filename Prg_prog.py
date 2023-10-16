# Prog_Verificação de Triângulos!!


#Begin
print('\t\t\t\n\n***Sistema de Validação de Triângulo***\n\n')


#Inputs
l1 = float(input('Digite o valor do Lado 1 do Objeto: '))
l2 = float(input('Digite o valor do Lado 2 do Objeto: '))
l3 = float(input('Digite o valor do Lado 3 do Objeto: '))

#Proc and Output
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1+l2):
    print(f'\nO objeto de lados equivalentes á {l1:.2f}, {l2:.2f},{l3:.2f} é um Triângulo!')

    if l1 == l2 == l3:
        print('O Triângulo é Equilatero.')

    elif l1 != l2 != l3:
        print('O Triângulo é Escaleno.')

    else:
        print('O Triângulo é Isósceles.')

else:
    print(f'\nO objeto de lados equivalentes á {l1:.2f}, {l2:.2f}, {l3:.2f} não é um Triângulo!')


