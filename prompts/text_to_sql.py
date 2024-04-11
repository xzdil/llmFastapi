from llama_index.core.prompts.prompt_type import PromptType
from llama_index.core.prompts import PromptTemplate

RUSSIAN_RESPONSE_SYNTHESIS_PROMPT_TMPL = (
    "При наличии входного вопроса синтезируйте ответ из результатов запроса.\n"
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
    "Учитывая входной вопрос, сначала создайте синтаксически правильный {dialect} "
    "запрос для выполнения, затем просмотрите результаты запроса и верните ответ. "
    "Вы можете упорядочить результаты по соответствующему столбцу, чтобы получить больше всего "
    "интересных примеров в базе данных.\n\n"
    "Никогда не запрашивайте все столбцы из определенной таблицы,попроси только "
    "несколько соответствующих столбцов с учетом вопроса.\n\n"
    "Обратите внимание: используйте только те имена столбцов, которые вы видите в схеме "
    "описания. "
    "Будьте осторожны и не запрашивайте несуществующие столбцы. "
    "Обратите внимание, какой столбец в какой таблице находится. "
    "Также,при необходимости уточняйте имена столбцов именем таблицы. "
    "Вам необходимо использовать следующий формат, каждая из которых занимает одну строку:\n\n"
    "Вопрос: Вопрос здесь\n"
    "SQLQuery: SQL-запрос для выполнения\n"
    "SQLResult: результат SQLQuery\n"
    "Ответ: Окончательный ответ здесь\n\n"
    "Используйте только таблицы, перечисленные ниже.\n"
    "{schema}\n\n"
    "Вопрос: {query_str}\n"
    "SQLQuery: "
)

RUSSIAN_TEXT_TO_SQL_PROMPT = PromptTemplate(
    RUSSIAN_TEXT_TO_SQL_TMPL,
    prompt_type=PromptType.TEXT_TO_SQL,
)
