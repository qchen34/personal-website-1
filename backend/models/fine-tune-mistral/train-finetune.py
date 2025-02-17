from peft import prepare_model_for_kbit_training
from peft import LoraConfig, get_peft_model
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
from transformers import DataCollatorForSeq2Seq
import torch
from model_load import load_base_model

# 1. 准备模型进行量化训练
model, tokenizer = load_base_model()
qlora_model = prepare_model_for_kbit_training(model)

# 2. 配置 LoRA 适配器
lora_config = LoraConfig(
    r=8,                      # LoRA 低秩维度（8~64）
    lora_alpha=16,            # LoRA 缩放因子
    target_modules=["q_proj", "v_proj"],  # 需要应用 LoRA 的层
    lora_dropout=0.1,        # dropout 防止过拟合
    bias="none",              # 不微调 bias
    task_type="CAUSAL_LM"  # 指定任务类型（序列到序列）
)

# 3. 应用 LoRA 适配器到模型
peft_model = get_peft_model(qlora_model, lora_config)
peft_model.print_trainable_parameters()  # 打印可训练的参数数量

# 4. 冻结 LoRA 以外的层，确保只训练 LoRA 层
for name, param in peft_model.named_parameters():
    if "lora" not in name:
        param.requires_grad = False  # 冻结其它层


# 5. 配置训练参数
training_args = Seq2SeqTrainingArguments(
    output_dir="/content/drive/MyDrive/models/mistral-7B_LoRA",          # 输出目录
    evaluation_strategy="epoch",     # 每轮评估一次
    report_to="none",
    learning_rate=1e-4,              # 学习率
    per_device_train_batch_size=4,   # 训练时每个设备的批量大小
    per_device_eval_batch_size=4,    # 评估时每个设备的批量大小
    gradient_accumulation_steps=4,   # 累积8个小批次的梯度
    num_train_epochs=2,              # 训练轮数
    weight_decay=0.01,               # 权重衰减
    logging_dir='./logs',            # 日志目录
    logging_steps=100,                # 每隔多少步记录一次日志
    save_steps=1000,                 # 每隔多少步保存一次模型
    save_total_limit=1,              # 最多保存多少个模型
    bf16=True,                        # 使用混合精度训练
    gradient_checkpointing=True,    # 启用梯度检查点
)

# 6. 定义优化器
optimizer = torch.optim.AdamW(
    filter(lambda p: p.requires_grad, model.parameters()), 
    lr=1e-4
)

# 7. 定义数据整理器
data_collator = DataCollatorForSeq2Seq(tokenizer, model=peft_model)

# 8. 初始化 Trainer
trainer = Seq2SeqTrainer(
    model=peft_model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,     # 提供评估数据集
    data_collator=data_collator,  # ✅ 正确的替换
    optimizers=(optimizer, None)  # 显式传递优化器
)

# 开始训练
trainer.train()