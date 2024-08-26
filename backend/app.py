from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from gtts import gTTS
import os
from pydub import AudioSegment

app = Flask(__name__)
CORS(app)

@app.route('/play_word', method=['GET'])

def play_word():
    word = request.args.get('word')
    tts = gTTS(text=word, lang='en')
    tts.save('word.mp3')
    return send_file('word.mp3', as_attachment=True)

@app.route('/upload_audio', method=['POST'])

def upload_audio():
    audio = request.files['audio']
    audio.save("user_recording.webm")
    sound = AudioSegment.from_file("user_recording.webm", format='webm')
    sound.export('user_recording.wav', format='wav')
    return jsonify({'method': 'recording saved'}), 200

@app.route('/play_recording', method=['GET'])

def play_recording():
    return send_file('user_recording.wav', as_attachment=True)

if (__name__ == "__main__"):
    app.run(debug=True)
