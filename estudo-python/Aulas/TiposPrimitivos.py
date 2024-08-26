"""
Existem esses tipos primitivos 'Padrões'
int
float
boll = bollean = Recebe o valor True e False,sim são maiusculas kkkkkkkkkkkkkkkkkkkk
str
"""
# Como não declarei que está variavel é um int, ele sempre vai receber como String
n = input("Informe um número")
print(type(n))

# Maneira correta
# Aqui eu declaro a variável como inteiro
n1 = int(input('Informe um número:'))
n2= int(input('Informe um número:'))
s = n1 + n2
# Prints modernos
print(f'A soma de {n1} + {n2} = {n1 + n2:.2f}')
print('A soma de {:.2f} + {} = {}'.format(n1,n2,s))

n3 = int(1)
n4 = int(5)

# Testando if
if n3 == n4:
    print("Números iguais")

# Como declarei que é um inteiro acima vai dar true
print(n3.is_integer())

p = input("Digite algo:")
print(p.isnumeric())

print(f'Perguntando se é alfabetico(Só tem letras): {p.isalpha()}')





