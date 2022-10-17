class cachorro:
  def __init__(self, nome, cor, acordado=True):
    print('Inicializando a classe...')
    self.nome = nome
    self.cor = cor
    self.acordado = acordado

  def __del__(self):
    print('Removendo a instância da classe.')

  def falar(self):
    print('Au Au')

def criar_cachorro():
  c = cachorro('Zeus', 'Branco e preto', False)
  print(c.nome)

#c = cachorro('Chappie', 'amarelo')
#c.falar()

criar_cachorro()