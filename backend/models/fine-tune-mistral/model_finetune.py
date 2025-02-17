from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, Seq2SeqTrainingArguments, Seq2SeqTrainer
import torch

def load_dataset():
    # 加载 psychology-dataset
    psychology_dataset = load_dataset("jkhedri/psychology-dataset")
    # print(psychology_dataset['train'][0])

    # 加载 PsyQA
    psyqa_dataset = load_dataset("lsy641/PsyQA")
    # print(psyqa_dataset['train'][0])

    # 加载 mental_health_chatbot_dataset
    mental_health_chatbot_dataset = load_dataset("heliosbrahma/mental_health_chatbot_dataset")
    # print(mental_health_chatbot_dataset['train'][0])

    train_test_datasets = psychology_dataset['train'].train_test_split(test_size=0.1, shuffle=True, seed=42)
    train_dataset = train_test_datasets['train']
    eval_dataset = train_test_datasets['test']

    return train_dataset, eval_dataset

def preprocess_data(examples, tokenizer):
    inputs = examples['question']  # 摘要作为输入
    targets = examples['response_j']  # 故事正文作为输出

    # 处理输入文本
    model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")
    tokenizer.padding_side = "right"
    # 设置标签
    labels = tokenizer(targets, max_length=512, truncation=True, padding="max_length")

    # 打印原始数据
    # print(f"Original input: {inputs[:1]}")
    # print(f"Original target: {targets[:1]}")

    # 检查 tokenizer 结果
    # print(f"Tokenized input_ids: {model_inputs['input_ids'][:1]}")
    # print(f"Tokenized labels: {labels['input_ids'][:1]}")

    if not model_inputs['input_ids'] or not labels['input_ids']:
        print("Error: Tokenization produced empty input_ids or labels!")

    labels['input_ids'] = [
        [(token if token != tokenizer.pad_token_id else -100) for token in label]
        for label in labels['input_ids']
    ]

    # 确保转换为 PyTorch Tensor
    model_inputs['input_ids'] = torch.tensor(model_inputs['input_ids'], dtype=torch.long, requires_grad=False)
    model_inputs['attention_mask'] = torch.tensor(model_inputs['attention_mask'], dtype=torch.long, requires_grad=False)
    model_inputs['labels'] = torch.tensor(labels['input_ids'], dtype=torch.long)
    # 打印检查数据
    # print(f"Input: {model_inputs['input_ids'][:1]}")
    # print(f"Labels: {model_inputs['labels'][:1]}")

    return model_inputs

def tokenizer_load(train_dataset, eval_dataset):
    # 应用预处理函数
    tokenized_train_dataset = train_dataset.map(preprocess_data, 
                                                batched=True, 
                                                # remove_columns=["question", "response_j"],
                                                num_proc=1)
    tokenized_eval_dataset = eval_dataset.map(preprocess_data, 
                                            batched=True, 
                                            # remove_columns=["question", "response_j"],
                                            num_proc=1)
    return tokenized_train_dataset, tokenized_eval_dataset