nome = 'NeYmAR'
print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "    Olá Mundo!     "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = 'Python'
print('####' + menu + "####")
print(menu.center(14))
print(menu.center(20, '#'))
print('-'.join(menu))

for letra in menu:
  print(letra, end='-')
print()

print('-'.join(menu))