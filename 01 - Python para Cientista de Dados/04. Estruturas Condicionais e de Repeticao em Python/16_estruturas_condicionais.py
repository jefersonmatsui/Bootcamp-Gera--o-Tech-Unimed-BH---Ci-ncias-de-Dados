MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

# if/else/elif

# Exemplo 1
if idade >= MAIOR_IDADE:
  print('Maior de idade, pode tirar a CNH.')

if idade < MAIOR_IDADE:
  print('Ainda não pode tirar a CNH.')

# Exemplo 2
if idade >= MAIOR_IDADE:
  print('Maior de idade, pode tirar a CNH.')
else:
  print('Ainda não pode tirar a CNH.')

# Exemplo 3
if idade >= MAIOR_IDADE:
  print('Maior de idade, pode tirar a CNH.')
elif idade == IDADE_ESPECIAL:
  print('Pode fazer aulas teóricas, ams não pode fazer aulas práticas')
else:
  print('Ainda não pode tirar a CNH.')

# if aninhado

# Exemplo 4
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
  if saldo >= saque:
    print('Saque realizado com sucesso!')
  elif saque <= (saldo + cheque_especial):
    print('Saque realizado com uso do cheque especial!')
elif conta_universitaria:
  if saldo >= saque:
    print('Saque realizado com sucesso!')
  else:
    print('Saldo insuficiente')

# Exemplo 5
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
  if saldo >= saque:
    print('Saque realizado com sucesso!')
  elif saque <= (saldo + cheque_especial):
    print('Saque realizado com uso do cheque especial!')
  else:
    print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
  if saldo >= saque:
    print('Saque realizado com sucesso!')
  else:
    print('Saldo insuficiente')

# Exemplo 6

conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
  if saldo >= saque:
    print('Saque realizado com sucesso!')
  elif saque <= (saldo + cheque_especial):
    print('Saque realizado com uso do cheque especial!')
  else:
    print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
  if saldo >= saque:
    print('Saque realizado com sucesso!')
  else:
    print('Saldo insuficiente')
else: 
  print('Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.')


# if ternário

# Exemplo 7
saldo = 2000
saque = 500

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} aoa realizar o saque')

# Exemplo 8
saldo = 2000
saque = 2500

status = 'Sucesso' if saldo >= saque else 'Falha'

print(f'{status} aoa realizar o saque')
