import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# 1. Carrega a chave de API de forma segura a partir do arquivo .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Configuração do modelo Gemini seguindo o framework LangChain
# Usamos o modelo 'gemini-2.5-flash' conforme o seu projeto original
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="AQ.Ab8RN6KNKRA4rS0QYox_pSOmxi43fLzPJguhugBh9Dkndjzv1g",
    temperature=0.2 # Baixamos a temperatura para a IA ser mais precisa na classificação
)

# 3. Criação do Prompt estruturado usando o padrão ChatPromptTemplate do LangChain
# O prompt instrui a IA a classificar o item do doador e responder estritamente em JSON
prompt = ChatPromptTemplate.from_template(
    """
    Você é o assistente inteligente do projeto Guia de Doação.
    Analise o seguinte item que o usuário deseja doar: '{item}'
    
    Responda ESTRITAMENTE em formato JSON (sem blocos de código markdown como ```json) com as seguintes chaves:
    - 'estado': (Novo, Usado ou Estragado)
    - 'categoria': (Eletronicos, Vestuario, Moveis ou Alimentos)
    
    Não utilize acentos ou caracteres especiais nas respostas das chaves.
    """
)

# 4. Criação da Chain (Cadeia de processamento do LangChain) usando o operador pipe '|'
chain = prompt | llm

def classificar_item_com_langchain(descricao_item: str):
    print(f"\n[LangChain] Enviando descrição para análise: '{descricao_item}'")
    
    try:
        # Executa a cadeia passando o item do usuário
        resposta_ia = chain.invoke({"item": descricao_item})
        
        # O LangChain retorna um objeto, pegamos o texto com .content
        conteudo_texto = resposta_ia.content
        
        # Converte o texto JSON retornado pela IA em um dicionário Python
        dados_classificados = json.loads(conteudo_texto)
        return dados_classificados
        
    except Exception as e:
        print(f"[Erro LangChain] Falha ao processar com a IA: {e}")
        return None

if __name__ == "__main__":
    # Teste de execução isolada da IA com LangChain
    item_teste = "Tenho uma impressora velha que nao funciona"
    resultado = classificar_item_com_langchain(item_teste)
    
    if resultado:
        print("\n=== RESULTADO DA CLASSIFICAÇÃO (LANGCHAIN) ===")
        print(f"Categoria: {resultado.get('categoria')}")
        print(f"Estado: {resultado.get('estado')}")
        print("==============================================")
