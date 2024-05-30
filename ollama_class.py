import ollama

class Ollama:
    def __init__(self, model='llama3:8b-instruct-q5_K_M', temperature=0):
        self.model = model
        self.temperature = temperature

    def generate(self, prompt):
        return ollama.generate(prompt=prompt, model=self.model, options={'temperature': self.temperature})['response']
    

if __name__ == "__main__":
    # Example usage
    prompt = 'Tell me a joke!'
    ollama = Ollama()