import sqlite3

# 1. Conecta ao banco de dados (se o arquivo não existir, ele será criado automaticamente)
conexao = sqlite3.connect('sistema_escolar.db')

# 2. Cria um cursor para executar os comandos SQL
cursor = conexao.cursor()

# 3. Cria a tabela 'alunos' com os campos solicitados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        RA TEXT NOT NULL UNIQUE,
        nota REAL,
        justificativa TEXT
    )
''')
conexao.commit()

# --- FUNÇÕES DE MANIPULAÇÃO DO BANCO ---

def inserir_aluno(nome, ra, nota, justificativa):
    """Insere um novo aluno no banco de dados."""
    try:
        cursor.execute('''
            INSERT INTO alunos (nome, RA, nota, justificativa)
            VALUES (?, ?, ?, ?)
        ''', (nome, ra, nota, justificativa))
        conexao.commit()
        print(f"Sucesso: Aluno(a) {nome} cadastrado(a)!")
    except sqlite3.IntegrityError:
        print(f"Erro: O RA '{ra}' já está cadastrado no sistema.")

def listar_alunos():
    """Busca e exibe todos os alunos cadastrados."""
    cursor.execute('SELECT * FROM alunos')
    linhas = cursor.fetchall()
    
    print("\n" + "="*50)
    print("REGISTROS CADASTRADOS NO BANCO:")
    print("="*50)
    
    if not linhas:
        print("Nenhum registro encontrado.")
    else:
        for linha in linhas:
            print(f"ID: {linha[0]}")
            print(f"Nome: {linha[1]}")
            print(f"RA: {linha[2]}")
            print(f"Nota: {linha[3]}")
            print(f"Justificativa: {linha[4]}")
            print("-" * 30)

# --- EXEMPLO PRÁTICO DE USO ---

# Inserindo alguns registros de teste
inserir_aluno("Mariana Costa", "RA202601", 9.5, "Apresentou um ótimo projeto final.")
inserir_aluno("Pedro Henrique", "RA202602", 5.0, "Faltou na entrega da atividade principal.")

# Tentando inserir um RA duplicado para testar a validação
inserir_aluno("Lucas Lima", "RA202601", 8.0, "Nota regular.")

# Exibindo os resultados
listar_alunos()

# 4. Fecha a conexão com o banco de dados ao terminar
conexao.close()


