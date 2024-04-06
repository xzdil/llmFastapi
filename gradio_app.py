import gradio as gr
from conversation import Conversation
import requests

conversation = Conversation()


def get_stream(text, history):
    s = requests.Session()
    conversation.add_user_message(text)
    prompt = conversation.get_prompt()
    url = f'localhost:/query?={prompt}'
    with s.get(url, headers=None, stream=True) as resp:
        response = ''
        for line in resp.iter_lines():
            if line:
                response += line
                yield response


demo = gr.ChatInterface(fn=get_stream, examples=["Что такое договор о долевом участии?",
                                                 "Чем отличается уполномоченная компания от застройщика?",
                                                 "Как мне себя обезопасить при покупке строящегося жилья?",
                                                 "Где я могу найти утвержденную форму договора долевого участия?",
                                                 "Какие действия необходимо совершить дольщику для приобретения жилья "
                                                 "в строящемся доме?",
                                                 "Кто гарантирует завершение строительства жилого объекта?",
                                                 "Какие меры предпринимаются для предотвращения риска двойных продаж "
                                                 "недвижимости?",
                                                 "Какие договора не безопасны?"],
                        title="ДелУчас-бот",
                        description="Это чат-бот, у которого вы можете спросить информацию о делевом участии в "
                                    "жилищном строительстве в РК")
demo.launch(debug=True, share=True, server_name="0.0.0.0", server_port=8765)
