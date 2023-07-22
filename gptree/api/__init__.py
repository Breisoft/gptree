import openai
import os
import html

def call_api(prompt, model='gpt-3.5-turbo'):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(model=model, messages=[
    {"role": "system", "content": "You are a a coding assistant designed to help with debugging and improving security code. You will be evaluating entire directories/code workspaces holistically."},
    {"role": "user", "content": prompt}
  ])
    
    parsed_data = ''

    for choice in completion['choices']:
        message = choice['message']
        role = message['role'].upper()

        content = message['content']


        data = f'<h2>{role}:</h2><br/><br/>'
        data += html.escape(content)
        data += '<br/>'

        parsed_data += data

    return parsed_data