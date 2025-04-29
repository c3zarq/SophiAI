import os
from crewai import Crew, Agent, Task, Process

# API Key 
os.environ['OPENAI_API_KEY'] = 'NA'

# agente 1
agente_escritor = Agent(
    role='Escritor de Reflexões Filosóficas',
    goal='Apresentar reflexões sobre o conflito apresentado, '
         'com base no que diriam os pensadores mencionados.',
    verbose=True,
    memory=True,
    llm="ollama/llama3.2:latest",
    backstory='Você é um filósofo experiente com muitos anos de estudo em filosofia.'
)

# tarefa 
tarefa = Task(
    description='Apresentar uma reflexão filosófica sobre o conflito apresentado.',
    expected_output='Um texto com pelo menos 6 parágrafas, contendo reflexões filosóficas '
                    'profundas.',
    agent = agente_escritor,
    output_file = 'reflexao.md'
)

# Criando a Crew
equipe = Crew(
    agents=[agente_escritor],
    tasks=[tarefa],
    process=Process.sequential
)

# Definição do conflito e dos pensadores
conflito = (
    'Descrição do conflito'
)

pensadores = [
    "Sócrates", "Platão",
    "Marco Aurélio", "Nietzsche"
]

# Executando a Crew 
try:
    resultados = equipe.kickoff(inputs={'conflito': conflito, 'pensadores': pensadores})
    print('Reflexão: \n', resultados)
except Exception as e:
    print(f"Erro durante a execução: {e}")