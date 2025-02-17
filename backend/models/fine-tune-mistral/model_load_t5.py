from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def load_flan_t5():
    # 加载预训练的模型和分词器
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    # 设置 padding token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    # 确保模型知道 padding token ID
    model.config.pad_token_id = tokenizer.pad_token_id
    
    return model, tokenizer

def generate_response(model, tokenizer, prompt, 
                     max_length=128,
                     temperature=0.7,
                     top_p=0.9,
                     num_beams=4):
    """
    生成回答，带有更多控制参数
    
    Args:
        model: Flan-T5 模型
        tokenizer: 分词器
        prompt: 输入文本
        max_length: 最大生成长度
        temperature: 采样温度
        top_p: 核采样参数
        num_beams: beam search 的束宽
    """
    try:
        # 添加 padding 和 attention mask 设置
        inputs = tokenizer(
            prompt, 
            return_tensors="pt", 
            padding=True,
            truncation=True,
            max_length=max_length,
            add_special_tokens=True,  # 添加特殊标记
            return_attention_mask=True  # 明确返回 attention mask
        )
        
        # 确保有 attention mask
        if 'attention_mask' not in inputs:
            inputs['attention_mask'] = torch.ones_like(inputs['input_ids'])
        
        outputs = model.generate(
            input_ids=inputs.input_ids,
            attention_mask=inputs.attention_mask,  # 传入 attention mask
            max_length=max_length,
            num_beams=num_beams,
            num_return_sequences=1,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            pad_token_id=tokenizer.pad_token_id,
            early_stopping=True,
            no_repeat_ngram_size=2
        )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
        
    except Exception as e:
        print(f"Error generating response: {e}")
        return None

# 测试代码
if __name__ == "__main__":
    model, tokenizer = load_flan_t5()
    
    test_prompt = "You are now acting as a Freudian psychotherapist. Provide a short motivational statement to help someone who is feeling anxious."
    
    print(f"Prompt: {test_prompt}")
    response = generate_response(model, tokenizer, test_prompt)
    print(f"Response: {response}")



