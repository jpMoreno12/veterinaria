class Agendamento:
  def __init__(self, data, medico, cliente, funcionario, compareceu, concluido, valor, pago) :
    self.data = data
    self.medico = medico
    self.cliente = cliente
    self.funcionario = funcionario
    self.compareceu = compareceu
    self.concluido = concluido
    self.valor = valor
    self.pago = pago

  
  def agendar(self, data, cliente, funcionario, medico, valor, compareceu = False, concluido = False):
    print('Agendamento realizado com sucesso')

  def finalizar(self, compareceu = True, concluido = True, pago = True):
      print('Consulta concluida con sucesso')


      



agendando = Agendamento('23/04', 'joao', 'pedro', 'moreno', '', '', 50.00, 00.00)
agendueido  = agendando.agendar('23/05', 'pedro', 'moreno', 'joao', 50.00)
agendando.finalizar('nao', 'nao', 'nao')
