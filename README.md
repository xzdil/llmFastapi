# Проект Saiga Mistral with llamaindex

Этот проект представляет собой приложение на FastAPI с интерфейсом, созданным с использованием Gradio.
В этом проекте я реализоал RAG(retrieval augmented generation), используя библиотеку llama-index.
В качестве LLM я использовал квантизированную модель Saiga Mistral(https://huggingface.co/TheBloke/saiga_mistral_7b-GGUF)

## Установка

1. Сначала клонируйте репозиторий:
git clone https://github.com/xzdil/llmFastapi
cd llmFastapi

2. Установите зависимости с помощью `pip`:
pip install -r requirements.txt

3. Запустите приложение:
uvicorn main_gradio:app --reload --host 0.0.0.0 --port 8000


## Использование

После запуска приложения перейдите по адресу `http://localhost:8000`, чтобы получить доступ к интерфейсу Gradio.
Здесь вы можете взаимодействовать с моделью, задавая ей вопросы и получая ответы.

## Лицензия

Этот проект лицензируется в соответствии с лицензией [MIT](LICENSE).

## Автор

Автор этого проекта:

- Адиль Рахимжанов

## Вклад

Мы приветствуем ваши вклады! Если вы хотите внести свой вклад, пожалуйста, откройте issue или создайте pull request.



