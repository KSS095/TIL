# 멀티 플레이 서버 예시 (Flask 기반)
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# 카테고리 및 곡 데이터 로딩
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/category_example.json')
with open(DATA_PATH, encoding='utf-8') as f:
    categories = json.load(f)

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(list(categories.keys()))

@app.route('/songs', methods=['GET'])
def get_songs():
    cat = request.args.get('category')
    if cat not in categories:
        return jsonify([])
    return jsonify(categories[cat])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
