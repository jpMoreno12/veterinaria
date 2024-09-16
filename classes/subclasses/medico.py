from classes.pessoa import Pessoa

class Medico(Pessoa):
  def __init__(self, nome, telefone, endereco, cpf, registro_profissional, especialidade, carga_horaria):
    super().__init__(nome, telefone, endereco, cpf)

    self.__registro_profissional = registro_profissional
    self.__especialidade = especialidade
    self.__carga_horaria = carga_horaria

  @property
  def registro_profissional(self):
    return self.__registro_profissional
  @registro_profissional.setter
  def registro_profissional(self, registro_profissional):
    self.__registro_profissional = registro_profissional
  
  @property
  def especialidade(self):
    return self.__especialidade

  @especialidade.setter
  def especialidade(self, especialidade):
    self.__especialidade = especialidade

  @property
  def carga_horaria(self):
    return self.__carga_horaria

  @carga_horaria.setter
  def carga_horaria(self, carga_horaria):
    self.__carga_horaria = carga_horaria
