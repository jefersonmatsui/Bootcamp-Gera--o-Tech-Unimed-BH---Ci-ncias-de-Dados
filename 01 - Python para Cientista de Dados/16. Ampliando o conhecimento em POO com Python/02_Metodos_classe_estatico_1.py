from mailbox import NotEmptyError


class Pessoa:
  def __init__(self, nome=None, idade=None):
    self.nome = nome
    self.idade = idade
  
  @classmethod # Não usa-se "self", usa-se "cls"
  def criar_de_data_nascimento(cls, ano, mes, dia, nome):
    #print(cls)
    idade = 2022 - ano
    return cls(nome, idade)

  @staticmethod
  def e_maior_idade(idade):
    return idade >= 18

#p = Pessoa("João", 28)
#print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1994,3,21,"João")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18)) #True
print(Pessoa.e_maior_idade(8)) #False