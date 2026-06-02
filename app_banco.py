import sqlite3

DB_NAME = "doacoes.db"

def inicializar_banco():
    # Passo 2: Faz a conexão com o banco de dados
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    
    print("[Banco] Conectado com sucesso!")

    # Passo 1: Cria a tabela do projeto
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Instituicoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_ong TEXT NOT NULL,
            categoria_aceita TEXT NOT NULL,
            endereco TEXT NOT NULL,
            contato TEXT NOT NULL
        )
    """)
    print("[Banco] Tabela 'Instituicoes' verificada/criada!")
    
    # Busca a contagem e corrige o bug pegando a primeira posição da tupla [0]
    cursor.execute("SELECT COUNT(*) FROM Instituicoes")
    total = cursor.fetchone()[0]
    
    if total == 0:
        ongs_exemplo = [
            ("ONG Recicla Tech", "Eletronicos", "Rua da Computacao, 123", "(42) 99999-1111"),
            ("Anjos da Guarda", "Vestuario", "Avenida Solidariedade, 456", "(42) 99999-2222"),
            ("Moveis Solidarios", "Moveis", "Rua do Desapego, 789", "(42) 99999-3333"),
            ("Banco de Alimentos", "Alimentos", "Alameda da Nutricao, 101", "(42) 99999-4444")
        ]
        cursor.executemany("""
            INSERT INTO Instituicoes (nome_ong, categoria_aceita, endereco, contato)
            VALUES (?, ?, ?, ?)
        """, ongs_exemplo)
        conexao.commit()
        print("[Banco] Dados iniciais de teste inseridos com sucesso!")
    else:
        print(f"[Banco] O banco já possui {total} instituições cadastradas.")
        
    conexao.close()
    print("[Banco] Conexão fechada com segurança.")

# Passo 3: Função para realizar inserções conforme a utilização do sistema
def inserir_instituicao(nome, categoria, endereco, contato):
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    
    cursor.execute("""
        INSERT INTO Instituicoes (nome_ong, categoria_aceita, endereco, contato)
        VALUES (?, ?, ?, ?)
    """, (nome, categoria, endereco, contato))
    
    conexao.commit()
    conexao.close()
    print(f"[Passo 3] Nova instituição '{nome}' inserida com sucesso!")

if __name__ == "__main__":
    # Garante que o banco está iniciado
    inicializar_banco()
    
    print("\n--- Testando o Passo 3 (Inserção de Dados) ---")
    # Simula a utilização do sistema inserindo uma nova ONG de teste
    inserir_instituicao(
        "Lar dos Idosos Feliz", 
        "Moveis", 
        "Rua da Terceira Idade, 77", 
        "(42) 98888-5555"
    )
