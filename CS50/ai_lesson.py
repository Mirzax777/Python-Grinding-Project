from openai import OpenAI

client = OpenAI()

prompt = input("Prompt : ")

response = client.response.create(
    input=prompt,
    model="gpt-5"
)

print(response.output_text)