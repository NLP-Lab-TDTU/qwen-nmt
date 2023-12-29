```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate trl datasets metrics tokenizers evaluate deepspeed bitsandbytes tiktoken --upgrade

# flash-attention-2
pip install flash-attn
```

# Prepare model checkpoint
```bash
python prepare_model.py --model-name Qwen/Qwen-7B-Chat --output-path Qwen-7B-Chat
```
