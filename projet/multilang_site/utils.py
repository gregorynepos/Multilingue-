import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

# Initialisation du modèle GPT-2
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2LMHeadModel.from_pretrained('gpt2')

# Fonction pour générer une réponse
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors='tf')
    outputs = model.generate(inputs['input_ids'], max_length=100, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text