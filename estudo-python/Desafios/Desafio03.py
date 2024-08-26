n1 = int(input("Informe um número:"))
n2 = int(input("Informe um número:"))

s = n1 + n2

print(f'A soma entre {n1} e {n2} = {s}')

algo = input("Digite algo:")
print(type(algo))
print(f"É alfabético? {algo.isalpha()}")
print(algo.isnumeric())
print(algo.isalnum())