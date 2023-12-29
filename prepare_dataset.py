from datasets import load_dataset

load_dataset("vietgpt/qwen-nmt").save_to_disk("data/qwen-nmt")
