```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate trl datasets metrics tokenizers evaluate deepspeed bitsandbytes tiktoken --upgrade

# flash-attention-2
pip install flash-attn
```

## Prepare model checkpoint
```bash
python prepare_model.py --model-name Qwen/Qwen-7B-Chat --output-path Qwen-7B-Chat
```
## Tuining

```bash
accelerate launch --config_file config.yml --multi_gpu --num_processes 2 run_sft.py \
--model_name_or_path Qwen-7B-Chat \
--per_device_train_batch_size 1 \
--per_device_eval_batch_size 1 \
--output_dir checkpoints-nmt \
--torch_dtype bfloat16 \
--optim lion_8bit \
--dataloader_num_workers 64 \
--gradient_accumulation_steps 32 \
--logging_steps 100 --save_steps 500 \
--save_total_limit 10 \
--learning_rate 5e-6 \
--tokenizer_name Qwen-7B-Chat \
--num_train_epochs 1
```
