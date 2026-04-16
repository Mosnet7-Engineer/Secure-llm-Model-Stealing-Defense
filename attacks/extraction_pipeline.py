from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ModelExtractor:
    def __init__(self, target_model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(target_model_name)
        self.model = AutoModelForCausalLM.from_pretrained(target_model_name)

    def query(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=100)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    extractor = ModelExtractor()
    print(extractor.query("Explain what a model stealing attack is."))
