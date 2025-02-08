"""
预处理 Jordan Peterson 访谈数据集
"""
import os
import pickle
import numpy as np
import re

# 读取输入文件
input_file_path = os.path.join(os.path.dirname(__file__), 'video_tbp.txt')

with open(input_file_path, 'r') as f:
    data = f.read()

# 数据清理
def clean_text(text):
    # 移除行号
    text = re.sub(r'\d+\|', '', text)
    # 移除说话者标记
    text = re.sub(r'-\s*\[.*?\]', '', text)
    # 移除多余空行
    text = re.sub(r'\n\s*\n', '\n', text)
    # 移除其他特殊字符
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()

data = clean_text(data)
print(f"length of dataset in characters: {len(data):,}")

# 获取所有唯一字符
chars = sorted(list(set(data)))
vocab_size = len(chars)
print("all the unique characters:", ''.join(chars))
print(f"vocab size: {vocab_size:,}")

# 创建字符到整数的映射
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
def encode(s):
    return [stoi[c] for c in s] # encoder: take a string, output a list of integers
def decode(l):
    return ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

# create the train and test splits
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode both to integers
train_ids = encode(train_data)
val_ids = encode(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# save the meta information as well, to help us encode/decode later
meta = {
    'vocab_size': vocab_size,
    'itos': itos,
    'stoi': stoi,
}
with open(os.path.join(os.path.dirname(__file__), 'meta.pkl'), 'wb') as f:
    pickle.dump(meta, f)

# length of dataset in characters:  1115394
# all the unique characters:
#  !$&',-.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
# vocab size: 65
# train has 1003854 tokens
# val has 111540 tokens
