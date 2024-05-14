from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def add_data():
    # POST isteğinden gelen JSON verisini al
    data = request.get_json()

    # JSON dosyasını oku
    with open('data.json', 'r') as f:
        json_data = json.load(f)

    # Yeni veriyi JSON dosyasına ekle
    json_data[data['name']] = data['value']

    # Güncellenmiş JSON verisini dosyaya yaz
    with open('data.json', 'w') as f:
        json.dump(json_data, f)

    # Başarılı yanıt gönder
    return jsonify({'message': 'Veri başarıyla eklendi!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
