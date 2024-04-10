import gradio as gr
from conversation import Conversation
import requests
import time

s = requests.Session()

def get_stream_llm(text, history):
    conversation = Conversation()
    for user, bot in history:
        print(f'user: {user}')
        print(f'bot: {bot}')
        conversation.add_user_message(user)
        conversation.add_bot_message(bot)
    conversation.add_user_message(text)
    prompt = conversation.get_prompt()
    url = f'http://localhost:8000/llm?question={prompt}'
    response = ''
    for line in s.get(url, headers=None, stream=True):
        print(line.decode('utf-8', errors='ignore'))
        response += line.decode('utf-8', errors='ignore')
        yield response

def get_stream_query(text, history):
    conversation = Conversation()
    for user, bot in history:
        print(f'user: {user}')
        print(f'bot: {bot}')
        conversation.add_user_message(user)
        conversation.add_bot_message(bot)
    conversation.add_user_message(text)
    prompt = conversation.get_prompt()
    url = f'http://localhost:8000/query?question={prompt}'
    response = ''
    for line in s.get(url, headers=None, stream=True):
        print(line.decode('utf-8', errors='ignore'))
        response += line.decode('utf-8', errors='ignore')
        yield response

def get_db_agent(text, history):
    conversation = Conversation()
    for user, bot in history:
        print(f'user: {user}')
        print(f'bot: {bot}')
        conversation.add_user_message(user)
        conversation.add_bot_message(bot)
    conversation.add_user_message(text)
    prompt = conversation.get_prompt()
    url = f'http://localhost:8000/db_agent?question={prompt}'
    response = s.get(url).decode('utf-8', errors='ignore')
    print(response.text)
    return response.text
    
demo = gr.ChatInterface(fn=get_stream, examples=["Сколько записей в базе?"],title="SQL бот",description="Бот-ассистент по базе данных")
#demo.launch(debug=True, share=True, server_name="0.0.0.0", server_port=8765)
