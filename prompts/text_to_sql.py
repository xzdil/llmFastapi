from llama_index.core.prompts.prompt_type import PromptType
from llama_index.core.prompts import PromptTemplate

RUSSIAN_RESPONSE_SYNTHESIS_PROMPT_TMPL = (
    "Напиши ответ из результатов запроса.\n"
    "Запрос: {query_str}\n"
    "SQL: {sql_query}\n"
    "Ответ SQL: {context_str}\n"
    "Ответ: "
)
RUSSIAN_RESPONSE_SYNTHESIS_PROMPT = PromptTemplate(
    RUSSIAN_RESPONSE_SYNTHESIS_PROMPT_TMPL,
    prompt_type=PromptType.SQL_RESPONSE_SYNTHESIS_V2,
)

RUSSIAN_TEXT_TO_SQL_TMPL = (
    "Учитывая входной вопрос, сначала создай синтаксически правильный {dialect} "
    "запрос для выполнения, затем просмотри результаты запроса и верни ответ. "
    "Ты можешь упорядочить результаты по соответствующему столбцу, чтобы получить больше всего "
    "интересных примеров в базе данных.\n\n"
    "Никогда не запрашивай все столбцы из определенной таблицы, попроси только "
    "несколько соответствующих столбцов с учетом вопроса.\n\n"
    "Обрати внимание: используй только те имена столбцов, которые ты видишь в схеме описания. "
    "Будь осторожен и не запрашивай несуществующие столбцы. "
    "Обрати внимание, какой столбец в какой таблице находится. "
    "Также, при необходимости уточняй имена столбцов именем таблицы. "
    "Тебе необходимо использовать следующий формат:\n\n"
    "Вопрос: Вопрос здесь\n"
    "SQLQuery: SQL-запрос для выполнения\n"
    "SQLResult: результат SQLQuery\n"
    "Ответ: Окончательный ответ здесь\n\n"
    "Используй только таблицы и столбцы, перечисленные ниже.\n"
    "{schema}\n\n"
    "Вопрос: {query_str}\n"
    "SQLQuery: "
)

RUSSIAN_TEXT_TO_SQL_PROMPT = PromptTemplate(
    RUSSIAN_TEXT_TO_SQL_TMPL,
    prompt_type=PromptType.TEXT_TO_SQL,
)
