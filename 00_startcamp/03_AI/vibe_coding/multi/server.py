# 멀티 플레이 서버 예시 (Flask 기반)
from flask import Flask, request, jsonify
import json
import os
import random

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/category_example.json')
with open(DATA_PATH, encoding='utf-8') as f:
    categories = json.load(f)

# 곡 데이터 저장 함수
def save_categories():
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(categories, f, ensure_ascii=False, indent=2)

ranking_data = {}
session_data = {}
current_problem = {}
player_stats = {}
chat_log = []
# 곡 삭제 API
@app.route('/delete_song', methods=['POST'])
def delete_song():
    data = request.get_json()
    category = data.get('category')
    title = data.get('title')
    if not (category and title):
        return jsonify({'error': 'invalid data'}), 400
    if category not in categories:
        return jsonify({'error': 'no category'}), 404
    before = len(categories[category])
    categories[category] = [s for s in categories[category] if s['title'] != title]
    save_categories()
    return jsonify({'result': 'ok' if len(categories[category]) < before else 'nochange'})

# 곡 수정 API
@app.route('/edit_song', methods=['POST'])
def edit_song():

    data = request.get_json()
    category = data.get('category')
    title = data.get('title')
    new_title = data.get('new_title')
    new_artist = data.get('new_artist')
    new_file = data.get('new_file')
    if not (category and title):
        return jsonify({'error': 'invalid data'}), 400
    if category not in categories:
        return jsonify({'error': 'no category'}), 404
    for song in categories[category]:
        if song['title'] == title:
            if new_title:
                song['title'] = new_title
            if new_artist:
                song['artist'] = new_artist
            if new_file:
                song['file'] = new_file
            save_categories()
            return jsonify({'result': 'ok'})
    return jsonify({'error': 'no song'}), 404

# 카테고리 삭제 API
@app.route('/delete_category', methods=['POST'])
def delete_category():
    data = request.get_json()
    category = data.get('category')
    if not category:
        return jsonify({'error': 'invalid data'}), 400
    if category in categories:
        del categories[category]
        save_categories()
        return jsonify({'result': 'ok'})
    return jsonify({'error': 'no category'}), 404

# 플레이어 통계 API
player_stats = {}

@app.route('/stats', methods=['GET'])
def get_stats():
    nickname = request.args.get('nickname')
    stats = player_stats.get(nickname, {'accuracy': 0, 'plays': 0})
    return jsonify(stats)

# 채팅 API (메모리 저장)
chat_log = []
@app.route('/chat', methods=['POST'])
def post_chat():
    data = request.get_json()

    nickname = data.get('nickname')
    msg = data.get('msg')
    if not (nickname and msg):
        return jsonify({'error': 'invalid data'}), 400
    chat_log.append({'nickname': nickname, 'msg': msg})
    return jsonify({'result': 'ok'})
# 멀티 플레이 서버 예시 (Flask 기반)
from flask import Flask, request, jsonify
import json
import os
import random

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/category_example.json')
with open(DATA_PATH, encoding='utf-8') as f:
    categories = json.load(f)

# 곡 데이터 저장 함수
def save_categories():
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(categories, f, ensure_ascii=False, indent=2)
@app.route('/add_song', methods=['POST'])
def add_song():
    data = request.get_json()
    category = data.get('category')
    title = data.get('title')
    artist = data.get('artist')
    file = data.get('file')
    if not (category and title and artist and file):
        return jsonify({'error': 'invalid data'}), 400
    if category not in categories:
        categories[category] = []
    categories[category].append({'title': title, 'artist': artist, 'file': file})
    save_categories()
    return jsonify({'result': 'ok'})

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(list(categories.keys()))

@app.route('/songs', methods=['GET'])
def get_songs():
    cat = request.args.get('category')
    randomize = request.args.get('random') == '1'
    if cat not in categories:
        return jsonify([])
    songs = categories[cat]
    if randomize and songs:
        return jsonify([random.choice(songs)])
    return jsonify(songs)



# 카테고리별 랭킹 데이터 (메모리)
ranking_data = {}
# 세션 데이터 (닉네임별)
session_data = {}
# 카테고리별 현재 문제 번호
current_problem = {}
@app.route('/session', methods=['POST'])
def post_session():
    data = request.get_json()
    nickname = data.get('nickname')
    category = data.get('category')
    if not (nickname and category):
        return jsonify({'error': 'invalid data'}), 400
    session_data[nickname] = {'category': category, 'problem_idx': 0}
    return jsonify({'result': 'ok'})

@app.route('/current_problem', methods=['POST', 'GET'])
def current_problem_api():
    if request.method == 'POST':
        data = request.get_json()
        category = data.get('category')
        idx = data.get('problem_idx')
        if not (category and isinstance(idx, int)):
            return jsonify({'error': 'invalid data'}), 400
        current_problem[category] = idx
        return jsonify({'result': 'ok'})
    else:
        category = request.args.get('category')
        idx = current_problem.get(category, 0)
        return jsonify({'problem_idx': idx})

@app.route('/score', methods=['POST'])
def post_score():
    data = request.get_json()
    nickname = data.get('nickname')
    score = data.get('score')
    category = data.get('category')
    if not (nickname and isinstance(score, int) and category):
        return jsonify({'error': 'invalid data'}), 400
    if category not in ranking_data:
        ranking_data[category] = []
    # 닉네임 중복 처리: 기존 점수보다 높을 때만 갱신
    updated = False
    for item in ranking_data[category]:
        if item['nickname'] == nickname:
            if score > item['score']:
                item['score'] = score
                updated = True
            break
    else:
        ranking_data[category].append({'nickname': nickname, 'score': score})
        updated = True
    # 점수 내림차순 정렬
    ranking_data[category] = sorted(ranking_data[category], key=lambda x: x['score'], reverse=True)
    return jsonify({'result': 'updated' if updated else 'nochange'})

@app.route('/ranking', methods=['GET'])
def get_ranking():
    category = request.args.get('category')
    if category not in ranking_data:
        return jsonify([])
    return jsonify(ranking_data[category])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
