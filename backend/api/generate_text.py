from flask import Blueprint, request, jsonify
import os
import sys
from pathlib import Path

# 创建蓝图
generate_bp = Blueprint('generate', __name__)

# 获取 nanoGPT 目录的路径
NANOGPT_DIR = Path(__file__).parent.parent / 'models' / 'nanoGPT'
sys.path.append(str(NANOGPT_DIR))

@generate_bp.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        model = data.get('model', 'out-shakespeare-char-2000')
        
        # 切换到 nanoGPT 目录
        original_dir = os.getcwd()
        os.chdir(str(NANOGPT_DIR))
        
        try:
            from sample import generate_text
            generated_text = generate_text(
                model_path=f'{model}/ckpt.pt',
                max_new_tokens=500
            )
            return jsonify({'generated_text': generated_text})
        finally:
            os.chdir(original_dir)
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500