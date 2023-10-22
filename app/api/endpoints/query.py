from fastapi import APIRouter

router = APIRouter()

# @router.post("/generate")
# def generate(message: Message):
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     #initialize the promt
#     messages = []
#     for prompt in init_prompt:
#         messages.append(prompt)
    
#     # reflect the request
#     messages.append({"role": "user", "content": message.message})
    
#     # request the answer to the ChatGPT
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#         )
#     answer = response.choices[0]["message"]["content"].strip()
#     return {"answer": answer}