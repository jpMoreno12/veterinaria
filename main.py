from classes.subclasses.medico import Medico
from classes.subclasses.funcionario import Funcionario
from classes.subclasses.cliente import Cliente
from classes.animal import Animal
from classes.agendamento import Agendamento

print('Digite os dados do cliente para o cadastro:')
nome_cliente = input('Nome: ')
nome_animal = input('Nome do animal: ')
cpf_cliente = input('CPF: ')
endereco_cliente = input('Endereço: ')
status_inadimplencia = input('Status de inadimplência: ')
telefone_cliente = input('Telefone: ')

cliente = Cliente(nome_cliente, nome_animal, cpf_cliente, endereco_cliente, status_inadimplencia, telefone_cliente)

print('Digite os dados do funcionário:')
nome_funcionario = input('Nome: ')
endereco_funcionario = input('Endereço: ')
cpf_funcionario = input('CPF: ')
telefone_funcionario = input('Telefone: ')
funcao_funcionario = input('Função: ')
sindicalizado_funcionario = input('Sindicalizado (Sim/Não): ')
carga_horaria_semanal = input('Carga horária semanal: ')

funcionario = Funcionario(nome_funcionario, endereco_funcionario, cpf_funcionario, telefone_funcionario, funcao_funcionario, sindicalizado_funcionario, carga_horaria_semanal)

print('Digite os dados do médico:')
nome_medico = input('Nome: ')
cpf_medico = input('CPF: ')
carga_horaria_medico = input('Carga horária: ')
endereco_medico = input('Endereço: ')
especialidade_medico = input('Especialidade: ')
registro_profissional = input('Registro profissional: ')
telefone_medico = input('Telefone: ')

medico = Medico(nome_medico, cpf_medico, carga_horaria_medico, endereco_medico, especialidade_medico, registro_profissional, telefone_medico)

print('Digite os dados do animal:')
nome_animal = input('Nome: ')
raca_animal = input('Raça: ')
especie_animal = input('Espécie: ')
data_nascimento_animal = input('Data de nascimento: ')
peso_animal = input('Peso: ')
sexo_animal = input('Sexo: ')

animal = Animal(nome_animal, raca_animal, especie_animal, data_nascimento_animal, peso_animal, sexo_animal)

print('Digite os dados do agendamento:')
data_agendamento = input('Data: ')
compareceu = input('Compareceu (Sim/Não): ')
concluido = input('Concluído (Sim/Não): ')
valor = float(input('Valor: '))
pago = input('Pago (Sim/Não): ')

agendamento = Agendamento(data_agendamento, medico.nome, cliente.nome, funcionario.nome, compareceu, concluido, valor, pago)

print(f'O animal {animal.nome}, dono {cliente.nome}, concluiu a consulta com o médico {medico.nome}, conforme registrado pelo funcionário {funcionario.nome}.')
