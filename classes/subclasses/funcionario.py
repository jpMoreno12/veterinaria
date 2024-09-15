from classes.pessoa import Pessoa

class Funcionario(Pessoa):
  def __init__(self, nome, telefone, endereco, cpf, carga_horaria_semanal, sindicalizando, funcao):
    super().__init__(nome, telefone, endereco, cpf) 

    self.carga_horaria_semanal = carga_horaria_semanal
    self.sindicalizando = sindicalizando
    self.funcao = funcao
