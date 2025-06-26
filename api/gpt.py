from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# A chave da OpenAI será passada pela Vercel como variável de ambiente
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/', methods=['POST'])
def responder():
    data = request.get_json()
    pergunta = data.get('text', '')

    if not pergunta:
        return jsonify({'text': 'Pergunta não recebida'}), 400

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": pergunta}],
            max_tokens=150
        )
        conteudo = resposta.choices[0].message.content.strip()
        return jsonify({'text': conteudo})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
