import os
from train_encapuslate import train_model  # Import the training function from train.py
import subprocess

# Define training configurations
training_configs = [
    #{'max_iters': 2000, 'lr_decay_iters': 2000, 'out_dir': 'out-shakespeare-char-2000'},
    #{'max_iters': 4000, 'lr_decay_iters': 4000, 'out_dir': 'out-shakespeare-char-4000'},
    #{'max_iters': 8000, 'lr_decay_iters': 8000, 'out_dir': 'out-shakespeare-char-8000'},
    #{
    #    'max_iters': 2000,
    #    'lr_decay_iters': 2000,
    #    'out_dir': 'out-peterson-char-2000',
    #    'dataset': 'peterson_data'  # 添加数据集路径
    #},
    {
        'max_iters': 4000,
        'lr_decay_iters': 4000,
        'out_dir': 'out/out-peterson-char-4000',
        'dataset': 'peterson_data',  # 添加数据集路径
        'batch_size': 32,             # 调整批量大小
        'learning_rate': 5e-4,        # 调整学习率
        'warmup_iters': 1000,         # 增加预热步数
        'weight_decay': 0.1,          # 增加权重衰减
        'grad_clip': 1.0,             # 梯度裁剪
        'block_size': 256,            # 调整序列长度
        'eval_interval': 500,         # 更频繁的评估
    },
]

# Base command
base_command = [
    "python", "train.py", os.path.join("config", "train_shakespeare_char.py"),  # 使用相对路径,
    "--device=cpu", "--compile=False", "--eval_iters=20", "--log_interval=1",
    "--block_size=64", "--batch_size=32", "--n_layer=6", "--n_head=8", "--n_embd=384", "--dropout=0.0", "--learning_rate=5e-4"
]

# Train models with different configurations
for config in training_configs:
    command = base_command + [
        f"--max_iters={config['max_iters']}",
        f"--lr_decay_iters={config['lr_decay_iters']}",
        f"--out_dir={config['out_dir']}",
        f"--dataset={config['dataset']}"  # 添加数据集参数
    ]
    
    print(f"\nStarting training with configuration:")
    print(f"Dataset: {config['dataset']}")
    print(f"Output directory: {config['out_dir']}")
    print(f"Max iterations: {config['max_iters']}")
    print(f"Command: {' '.join(command)}\n")
    
    try:
        subprocess.run(command, check=True)
        print(f"Training completed for {config['out_dir']}")
    except subprocess.CalledProcessError as e:
        print(f"Error during training: {e}")
        continue