""" Para a classe Pessoa teremos os atributos: nome, telefone, email, endereco e 
cpf. Crie todos os atributos como públicos e implemente corretamente o método construtor. """


class Pessoa:
  def __init__(self, nome, telefone, endereco, cpf):  
    self.__nome = nome
    self.__telefone = telefone
    self.__endereco = endereco
    self.__cpf = cpf

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def telefone(self):
    return self.__telefone

  @telefone.setter
  def telefone(self, telefone):
    self.__telefone = telefone

  @property
  def endereco(self):
    return self.__endereco

  @endereco.setter
  def endereco(self, endereco):
    self.__endereco = endereco

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self, cpf):
    self.__cpf = cpf
