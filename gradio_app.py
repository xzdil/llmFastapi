import gradio as gr
from conversation import Conversation
import requests
import time

s = requests.Session()
DEFAULT_SYSTEM_PROMPT = "Ты — ИИ ассистент, отвечай на вопросы вежливо и точно"
def get_stream_llm(text, history):
    conversation = Conversation(system_prompt=DEFAULT_SYSTEM_PROMPT)
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

DOC_QUERY_SYSTEM_PROMPT = "Ты — Ассистент по договору о долевом участии, отвечай строго по инструкции, если вопрос " \
                        "задается не о договоре о долевом участии, проси задавать вопросы только по теме."
def get_stream_query(text, history):
    conversation = Conversation(system_prompt=DOC_QUERY_SYSTEM_PROMPT)
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

SQL_SYSTEM_PROMPT = """Ты ассистент для написания Postrgres SQL запросов, твоя задача писать качественные Postgres SQL запросы. 
Когда используешь условие SELECT и WHERE обязательно заключай колонны в кавычки. 
Пример правильного запроса: SELECT COUNT("колонна(обязательно в кавычках)") FROM rental_portfolio WHERE "колонна(обязательно в кавычках)" > 'значение';    
Eсли запрос будет неправильный, то ты будешь уволен! Если запрос будет правильный, ты получишь премию. 
Обязательно обрати внимание, заключены ли колонны в кавычки."""
def get_db_agent(text, history):
    conversation = Conversation(system_prompt=SQL_SYSTEM_PROMPT)
    for user, bot in history:
        print(f'user: {user}')
        print(f'bot: {bot}')
        conversation.add_user_message(user)
        conversation.add_bot_message(bot)
    conversation.add_user_message(text+", следи чтобы все колонны в запросе были в кавычках, и в конце запроса после ; не было ничего.")
    prompt = conversation.get_prompt()
    url = f'http://localhost:8000/db_agent?question={prompt}'
    response = s.get(url)
    print(response.text)
    return response.text
    
db_chat = gr.ChatInterface(fn=get_db_agent, examples=["Сколько записей в базе?"],title="SQL бот",description="Бот-ассистент по базе данных")
doc_chat = gr.ChatInterface(fn=get_stream_query, examples=["Что такое договор о долевом участии?",
                                                 "Чем отличается уполномоченная компания от застройщика?",
                                                 "Как мне себя обезопасить при покупке строящегося жилья?",
                                                 "Где я могу найти утвержденную форму договора долевого участия?",
                                                 "Какие действия необходимо совершить дольщику для приобретения жилья "
                                                 "в строящемся доме?",
                                                 "Кто гарантирует завершение строительства жилого объекта?",
                                                 "Какие меры предпринимаются для предотвращения риска двойных продаж "
                                                 "недвижимости?",
                                                 "Какие договора не безопасны?"],
                        title="ДолУчас-бот",
                        description="Это чат-бот, у которого вы можете спросить информацию о долевом участии в "
                                    "жилищном строительстве в РК")
llm_chat = gr.ChatInterface(fn=get_stream_llm, examples=["Привет"],title="Saiga mistral",description="Saiga mistral Q5 Small")
#demo.launch(debug=True, share=True, server_name="0.0.0.0", server_port=8765)
