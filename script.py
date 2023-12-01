import os
from llama_cpp import Llama

model_path = "/Users/rlm/Desktop/Code/llama/code-llama/codellama-13b-instruct.Q4_K_M.gguf"

if not os.path.exists(model_path):
    raise ValueError(f"Model path does not exist: {model_path}")

# Rest of your code to initialize llama
# ...
