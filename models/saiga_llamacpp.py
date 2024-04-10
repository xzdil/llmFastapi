from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.llama_cpp.llama_utils import (
    messages_to_prompt,
    completion_to_prompt
)

model_url = 'https://huggingface.co/TheBloke/saiga_mistral_7b-GGUF/resolve/main/saiga_mistral_7b.Q5_K_S.gguf'
model_path = "saiga_mistral_7b.Q5_K_S.gguf"

saiga_mistral = LlamaCPP(
    model_url=model_url,
    model_path=None,
    max_new_tokens=4096,
    context_window=20000,
    generate_kwargs={},
    model_kwargs={"cache": True,
                  "use_mmap": True},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True
)
