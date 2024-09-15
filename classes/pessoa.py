""" Para a classe Pessoa teremos os atributos: nome, telefone, email, endereco e 
cpf. Crie todos os atributos como públicos e implemente corretamente o método construtor. """


class Pessoa:
  def __init__(self, nome, telefone, endereco, cpf):  
    self.nome = nome
    self.telefone = telefone
    self.endereco = endereco
    self.cpf = cpf
