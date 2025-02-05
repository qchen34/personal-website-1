from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import logging
import os
import traceback

app = Flask(__name__)
# 允许本地开发环境的请求
CORS(app, resources={r"/generate": {"origins": ["http://localhost:3000", "https://chenqiwei.org"]}})

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
        # 允许本地开发环境的请求
        response.headers.add('Access-Control-Allow-Origin', request.headers.get('Origin', '*'))
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    try:
        data = request.json
        logger.info(f"Received request data: {data}")

        # 获取模型名称，例如 "out-shakespeare-char-2000"
        model = data.get('model', 'out-shakespeare-char-2000')
        
        # 更新 nanoGPT 目录的路径
        nanogpt_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'nanoGPT')
        
        # 确保模型输出目录存在
        model_dir = os.path.join(nanogpt_dir, 'out', model)
        logger.info(f"Model directory path: {model_dir}")
        
        if not os.path.exists(model_dir):
            error_msg = f"Model directory not found at: {model_dir}"
            logger.error(error_msg)
            return jsonify({'error': error_msg}), 500
        
        # 简化命令，使用相对于 nanoGPT 目录的路径
        command = [
            'python', 'sample.py',
            '--out_dir=out/' + model,  # 使用等号连接参数和值
            '--device=cpu',             # 使用等号连接参数和值
            '--max_new_tokens=100'
        ]

        logger.info(f"Executing command in {nanogpt_dir}: {' '.join(command)}")
        
        # 在 nanoGPT 目录中执行命令
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=nanogpt_dir
        )

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