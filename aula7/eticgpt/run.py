from typing import Literal
from pydantic import BaseModel

class OllamaPrompt(BaseModel):

    model: Literal["gemma"]
    prompt: str
    stream: bool = False 