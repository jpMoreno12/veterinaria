from classes.pessoa import Pessoa

class Cliente(Pessoa):
  def __init__(self, nome, telefone, endereco, cpf, animal, status_inadimplencia):
    super().__init__(nome, telefone, endereco, cpf)

    self.__animal = animal
    self.__status_inadimplencia = status_inadimplencia

  @property
  def animal(self):
    return self.__animal
  @animal.setter
  def animal(self, animal):
    self.__animal = animal
  
  @property
  def status_inadimplencia(self):
    return self.__status_inadimplencia

  @status_inadimplencia.setter
  def status_inadimplencia(self, status_inadimplencia):
    self.__status_inadimplencia = status_inadimplencia
