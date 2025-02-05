import os
from train_encapuslate import train_model  # Import the training function from train.py
import subprocess

# Define training configurations
training_configs = [
    {'max_iters': 2000, 'lr_decay_iters': 2000, 'out_dir': 'out-shakespeare-char-2000'},
    {'max_iters': 4000, 'lr_decay_iters': 4000, 'out_dir': 'out-shakespeare-char-4000'},
    {'max_iters': 8000, 'lr_decay_iters': 8000, 'out_dir': 'out-shakespeare-char-8000'}
]

# Base command
base_command = [
    "python", "train.py", "config/train_shakespeare_char.py",
    "--device=cpu", "--compile=False", "--eval_iters=20", "--log_interval=1",
    "--block_size=64", "--batch_size=64", "--n_layer=6", "--n_head=8", "--n_embd=384", "--dropout=0.0", "--learning_rate=3e-4"
]

# Train models with different configurations
for config in training_configs:
    command = base_command + [
        f"--max_iters={config['max_iters']}",
        f"--lr_decay_iters={config['lr_decay_iters']}",
        f"--out_dir={config['out_dir']}"
    ]
    print(f"Executing command: {' '.join(command)}")
    subprocess.run(command)