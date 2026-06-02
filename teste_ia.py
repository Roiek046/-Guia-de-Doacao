import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=AIzaSyBOMA9hjaQjMNIF-mF7KLDXJ2w7M3CQKGA"

payload = {
    "contents": [{
        "parts": [{
            "text": "Classifique: Tenho uma impressora velha que nao funciona. Responda em JSON com as chaves estado e categoria."
        }]
    }],
    "generationConfig": {
        "responseMimeType": "application/json"
    }
}

print("Conectando a API do Gemini... Aguarde.")

try:
    resposta = requests.post(url, json=payload, timeout=10)
    if resposta.status_code == 200:
        print("\n=== CONEXAO REALIZADA COM SUCESSO! ===")
        print(resposta.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        print(f"\nErro na API (Status {resposta.status_code}): {resposta.text}")
except Exception as e:
    print(f"\nFalha de conexao: {e}")
