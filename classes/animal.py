
class Animal:
  def __init__(self, nome, sexo, peso, especie, raca, data_nascimento):
    self.__nome = nome
    self.__sexo = sexo
    self.__peso = peso
    self.__especie = especie 
    self.__raca = raca
    self.__data_nascimento = data_nascimento
  


  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome
  @property
  def sexo(self):
    return self.__sexo

  @sexo.setter
  def sexo(self, sexo):
    self.__sexo = sexo

  @property
  def peso(self):
    return self.__peso

  @peso.setter
  def peso(self, peso):
    self.__peso = peso

  @property
  def especie(self):
    return self.__especie

  @especie.setter
  def especie(self, especie):
    self.__especie = especie

  @property
  def raca(self):
    return self.__raca

  @raca.setter
  def raca(self, raca):
    self.__raca = raca

  @property
  def data_nascimento(self):
    return self.__data_nascimento

  @data_nascimento.setter
  def data_nascimento(self, data_nascimento):
    self.__data_nascimento = data_nascimento
