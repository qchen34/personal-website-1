from flask import Blueprint, request, jsonify
import openai

therapy_bp = Blueprint('therapy', __name__)

# 设置系统提示词来定义助手的角色和行为
SYSTEM_PROMPT = """
你是一位专业的心理咨询师，名叫"暖心"。你的职责是：
1. 以同理心倾听用户的问题
2. 运用积极倾听技巧
3. 提供专业的心理支持和建议
4. 保持专业和谨慎的态度
5. 在必要时建议寻求专业医疗帮助

注意事项：
- 保持对话友善和支持性
- 不做医疗诊断
- 遇到危机情况时提供紧急求助信息
- 保护用户隐私
"""

@therapy_bp.route('/api/therapy-chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')

        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # 调用API获取回复
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500
        )

        bot_response = response.choices[0].message.content

        return jsonify({'response': bot_response})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500 