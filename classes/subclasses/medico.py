from classes.pessoa import Pessoa

class Medico(Pessoa):
  def __init__(self, nome, telefone, endereco, cpf, registro_profissional, especialidade, carga_horaria):
    super().__init__(nome, telefone, endereco, cpf)

    self.registro_profissional = registro_profissional
    self.especialidae = especialidade
    self.carga_horaria = carga_horaria
