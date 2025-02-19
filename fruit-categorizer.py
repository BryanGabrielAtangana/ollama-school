import os
import ollama

input_file = "./data/fruits.txt"
output_file = "./data/fruit-categories.txt"
model = "llama3.2:1b"
fruits = ""

if not os.path.exists(input_file):
    print(f'{input_file}, not found!!!')
    exit(1)

with open( input_file, "r") as f:
    fruits = f.read().strip()

prompt= """
You are a fruit expert that categorizes fruits in families.
Here is a list of fruits.
{fruits}
Please:
1. Categorize them into appropriate families;
2. Arrange each family in alphabetical order;
3. Present everything in an organized manner.
""" 

try:
    res = ollama.generate(model=model, prompt=prompt)
    generated_txt = res.get("response", "")
    
    with open(output_file,"w") as f:
        f.write(generated_txt.strip())

    print(f'The families have been saved in {output_file}')
except Exception as e:
    print(f"An error occurred: {e}")


