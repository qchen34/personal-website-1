# Personal Website Project

This project is a personal website that integrates a machine learning model trained on Shakespeare's text dataset. The website allows users to train the model and generate text similar to what Shakespeare would write.

## Project Structure

- **Backend**: A Flask server that handles model training and text generation.
- **Frontend**: A React application that provides the user interface.

## Backend Process

1. **Training the Model**:
   - Run the `train.py` script with the appropriate command to train the model.
   - The output will save the model as a checkpoint (`ckpt.pt`) file.

   ```bash
   python train.py config/train_shakespeare_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0

2. **Generating Text**:
    -Run the following command.
    ```bash
    python sample.py --model_path=out-shakespeare-char/ckpt.pt --start="To be, or not to be"