from flask import Flask, request, jsonify

app = Flask(__name__)

valid_moods = ['happy', 'sad', 'angry', 'neutral', 'excited']
moods_db = []

@app.route('/api/moods', methods=['POST'])
def submit_mood():
    data = request.get_json()
    mood = data.get('mood')
    user_id = data.get('user_id')
    if mood not in valid_moods:
        return jsonify({'error': 'Invalid mood value'}), 400
    moods_db.append({'user_id': user_id, 'mood': mood, 'timestamp': '2025-11-10T06:00:00Z'})
    # Integration with recommendation engine would happen here
    return jsonify({'message': 'Mood recorded successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
