from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# A chave da OpenAI será passada pela Vercel como variável de ambiente
openai.api_key = os.environ.get("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")

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
