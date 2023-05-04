from transformers import AutoTokenizer, AutoModelForCausalLM,pipeline
import os
abs_path = os.path.dirname(__file__)
model_path = os.path.join(abs_path,"model")

print(model_path)

class magic_prompt(object):
    def __init__(self):      
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        self.model = AutoModelForCausalLM.from_pretrained(model_path)

        self.pipeline = pipeline(task="text-generation",tokenizer=self.tokenizer,model=self.model)
    
    def run(self,input):
        return self.pipeline(input)[0]['generated_text']


if __name__ == "__main__":
    test = magic_prompt()
    
    print(test.run("xxx"))