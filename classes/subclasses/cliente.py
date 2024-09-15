from classes.pessoa import Pessoa

class Cliente(Pessoa):
  def __init__(self, nome, telefone, endereco, cpf, animal, status_inadimplencia):
    super().__init__(nome, telefone, endereco, cpf)

    self.animal = animal
    self.status_inadimplencia = status_inadimplencia
