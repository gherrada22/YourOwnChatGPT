# !/usr/bin/env python3
# Autor: @gherrada22 (GitHub) (Linkedin)
# import openai library
# pip install openai
import openai
# set up the OpenAI client
openai.api_key = "Your API Key"
# this loop will let us ask questions continuously
# and behave like a chatGPT
while True:
    # set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = input('Enter new prompt: ')
    if 'exit' in prompt or 'quit' in prompt:
        break
    # generate the response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1, stop=None,
        temperature=0.5)
    # extracting useful oart of the response
    response = completion.choices[0].text
    # print the response
    print(response)
