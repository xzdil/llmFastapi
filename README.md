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

4. Выберите способ запуска LLM (Локально или на Google colab)

Локально:

Установите ollama: `curl -fsSL https://ollama.com/install.sh | sh`

В папку models загрузите нужную вам модель, например saiga mistral: `wget https://huggingface.co/TheBloke/saiga_mistral_7b-GGUF/resolve/main/saiga_mistral_7b.Q5_K_S.gguf`

Создайте Modelfile для этой модели: 

Для этого используем nano, если не установлен установите: `sudo apt update`

`sudo apt install nano`

Создайте файл: `nano Modelfile`

Впишите путь модели в файл, например: `FROM ./models/saiga_mistral_7b.Q5_K_S.gguf`

Создайте модель из файла Modelfile

`ollama create saiga -f Modelfile`

В файле gradio_code.py укажите `is_local = True`

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



