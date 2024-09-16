from classes.pessoa import Pessoa

class Funcionario(Pessoa):
  def __init__(self, nome, telefone, endereco, cpf, carga_horaria_semanal, sindicalizando, funcao):
    super().__init__(nome, telefone, endereco, cpf) 

    self.__carga_horaria_semanal = carga_horaria_semanal
    self.__sindicalizando = sindicalizando
    self.__funcao = funcao

  @property
  def carga_horaria_semanal(self):
    return self.__carga_horaria_semanal
  @carga_horaria_semanal.setter
  def carga_horaria_semanal(self, carga_horaria_semanal):
    self.__carga_horaria_semanal = carga_horaria_semanal
  
  @property
  def sindicalizado(self):
    return self.__sindicalizando

  @sindicalizado.setter
  def sindicalizado(self, sindicalizado):
    self.__sindicalizando = sindicalizado

  @property
  def funcao(self):
    return self.__funcao

  @funcao.setter
  def funcao(self, funcao):
    self.__funcao = funcao

