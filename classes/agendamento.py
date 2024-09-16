class Agendamento:
  def __init__(self, data, medico, cliente, funcionario, compareceu, concluido, valor, pago) :
    self.__data = data
    self.__medico = medico
    self.__cliente = cliente
    self.__funcionario = funcionario
    self.__compareceu = compareceu
    self.__concluido = concluido
    self.__valor = valor
    self.__pago = pago


  @property
  def data(self):
    return self.__data

  @data.setter
  def data(self, data):
    self.__data = data

  @property
  def medico(self):
    return self.__medico

  @medico.setter
  def medico(self, medico):
    self.__medico = medico

  @property
  def cliente(self):
    return self.__cliente

  @cliente.setter
  def cliente(self, cliente):
    self.__cliente = cliente
  
  @property
  def funcionario(self):
    return self.__funcionario

  @funcionario.setter
  def funcionario(self, funcionario):
    self.__funcionario = funcionario

  @property
  def compareceu(self):
    return self.__compareceu

  @compareceu.setter
  def compareceu(self, compareceu):
    self.__compareceu = compareceu


  @property
  def concluido(self):
    return self.__concluido
  
  @concluido.setter
  def concluido(self, concluido):
    self.__concluido = concluido

  @property
  def valor(self):
    return self.__valor

  @valor.setter
  def valor(self, valor):
    self.__valor = valor

  @property
  def pago(self):
    return self.__pago

  @pago.setter
  def pago(self, pago):
    self.__pago = pago

  
  def agendar(self, data, cliente, funcionario, medico, valor, compareceu = False, concluido = False):
    print('Agendamento realizado com sucesso')

  def finalizar(self, compareceu = True, concluido = True, pago = True):
      print('Consulta concluida con sucesso')


      



