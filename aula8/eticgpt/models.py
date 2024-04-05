from typing import Literal
from pydantic import BaseModel

class OllamaPrompt(BaseModel):

    model: Literal["gemma"]="gemma"
    prompt: str
    stream: bool = False 
    

class OllamaResponse(BaseModel):
    done: bool
    response: str