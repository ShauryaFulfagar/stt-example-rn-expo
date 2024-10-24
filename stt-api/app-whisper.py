from flask import Flask, request, jsonify
import whisper
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load the Whisper model
# Change to base if innacurate
# Can be to 'tiny', 'base' on CPU and 'small', 'medium' & 'large' on GPU
model = whisper.load_model("tiny")

# Ensure uploads directory exists
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    filename = secure_filename(audio_file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    audio_file.save(filepath)

    # Transcribe using Whisper
    result = model.transcribe(filepath)

    # Remove the audio file after processing
    os.remove(filepath)

    print('result: ', result)
    return jsonify({
        'transcription': result['text']
    })


if __name__ == '__main__':
    app.run(debug=True)
