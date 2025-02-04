from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import logging
import os
import traceback

app = Flask(__name__)
CORS(app, resources={r"/generate": {"origins": "https://chenqiwei.org"}})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/test', methods=['GET', 'OPTIONS'])
def test():
    return jsonify({"message": "CORS test successful"})

@app.route('/generate', methods=['POST', 'OPTIONS'])
def generate():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'OK'})
        response.headers.add('Access-Control-Allow-Origin', 'https://chenqiwei.org')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    try:
        data = request.json
        logger.info(f"Received request data: {data}")

        model = data.get('model', 'out-shakespeare-char-2000')

        command = [
            'python', 'sample.py',
            f'--out_dir={model}',
            '--device=cpu'
        ]

        logger.info(f"Executing command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(__file__)))

        logger.info(f"Command output: {result.stdout}")
        if result.stderr:
            logger.error(f"Command error: {result.stderr}")

        if result.returncode != 0:
            error_msg = f"Error generating text: {result.stderr}"
            logger.error(error_msg)
            return jsonify({'error': error_msg}), 500

        return jsonify({'generated_text': result.stdout})

    except Exception as e:
        error_msg = f"Server error: {str(e)}\n{traceback.format_exc()}"
        logger.error(error_msg)
        return jsonify({'error': error_msg}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)