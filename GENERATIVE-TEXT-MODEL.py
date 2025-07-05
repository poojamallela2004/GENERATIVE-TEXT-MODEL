pip install transformers torch

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium" or "gpt2-large" for more power
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# Function to generate text from a user prompt
def generate_text(prompt, max_length=150, temperature=0.7, top_p=0.9):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=max_length,
            temperature=temperature,
            top_p=top_p,
            do_sample=True,
            top_k=50,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Example: User prompt
user_prompt = input("Enter a topic or prompt: ")
generated_text = generate_text(user_prompt)

print("\n--- Generated Text ---\n")
print(generated_text)
