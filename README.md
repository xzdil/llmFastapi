# Проект Saiga Mistral with llamaindex

Этот проект представляет собой приложение на FastAPI с интерфейсом Gradio.
В этом проекте я реализоал RAG(retrieval augmented generation), используя библиотеку llama-index.
В качестве LLM я использовал квантизированную модель Saiga Mistral(https://huggingface.co/TheBloke/saiga_mistral_7b-GGUF)

## Установка

1. Сначала клонируйте репозиторий:

git clone https://github.com/xzdil/llmFastapi

2. Перейдите в папку репозитория

cd llmFastapi

3. Установите зависимости с помощью `pip`:

pip install -r requirements.txt

<div style="display: flex;">
  <div style="flex: 1; padding-right: 10px;">
    <h2>Первая колонка</h2>
    <p>Текст первой колонки.</p>
  </div>
  <div style="flex: 1; padding-left: 10px;">
    <h2>Вторая колонка</h2>
    <p>Текст второй колонки.</p>
  </div>
</div>


5. Запустите приложение:

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



