from flask import Flask, render_template, redirect, request
from classes.subclasses.cliente import Cliente  # Ajuste o caminho conforme necessário
from classes.subclasses.medico import Medico  # Ajuste o caminho conforme necessário
from classes.subclasses.funcionario import Funcionario  # Ajuste o caminho conforme necessário
from classes.animal import Animal   # Ajuste o caminho conforme necessário
from classes.agendamento import Agendamento   # Ajuste o caminho conforme necessário


app = Flask(__name__, template_folder='screens')
app.config['SECRET_KEY'] = 'MINHAKEY'


funcionario = Funcionario(
    nome='Ana Oliveira',
    endereco='Rua das Flores, 123, Centro',
    cpf='123.456.789-00',
    telefone='(11) 98765-4321',
    funcao='Veterinária',
    sindicalizando='Sim',
    carga_horaria_semanal='40 horas/semana'
)

# Dados fictícios para Medico
medico = Medico(
    nome='Dr. João Silva',
    cpf='987.654.321-00',
    carga_horaria='20 horas/semana',
    endereco='Avenida Brasil, 456, Sala 301',
    especialidade='Cardiologia',
    registro_profissional='CRM 123456',
    telefone='(21) 12345-6789'
)

# Dados fictícios para Animal
animal = Animal(
    nome='Rex',
    raca='Labrador',
    especie='Canino',
    data_nascimento='2018-05-10',
    peso='30 kg',
    sexo='Macho'
)

# Dados fictícios para Agendamento
agendamento = Agendamento(
    data='2024-09-20',
    medico='Dr. João Silva',
    cliente= 'x',
    funcionario= 'Ana Oliveira',
    compareceu='Sim',
    concluido='Não',
    valor=150.00,
    pago='Não'
)

@app.route('/')
def home():
    # Renderize o formulário de cadastro
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    endereco = request.form.get('endereco')
    cpf = request.form.get('cpf')
    animal = request.form.get('animal')
    status_inadimplencia = request.form.get('inadimplencia')

    # Crie uma instância da classe Cliente com os dados recebidos
    cliente = Cliente(
        nome=nome,
        telefone=telefone,
        endereco=endereco,
        cpf=cpf,
        animal=animal,
        status_inadimplencia=status_inadimplencia
    )

    # Imprima os dados no console para verificação
    print("Nome:", cliente.nome)
    print("Telefone:", cliente.telefone)
    print("Endereço:", cliente.endereco)
    print("CPF:", cliente.cpf)
    print("Animal:", cliente.animal)
    print("Inadimplência:", cliente.inadimplencia)

    agendamento.agendar(agendamento.data, cliente.nome, funcionario.nome, medico.nome, agendamento.valor)

    return render_template('resultado.html', agendamento=agendamento)

if __name__ == "__main__":
    app.run(debug=True)
