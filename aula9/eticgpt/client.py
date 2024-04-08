import requests
import logging
from eticgpt.models import OllamaPrompt , OllamaResponse
from eticgpt import decorator 

logger = logging.getLogger(__name__)

class OllamaAPI:

    @decorator
    def __init__(self) -> None:
        self.base_url="http://localhost:11434"
        self.prompt_endpoint="api/generate"

    @decorator
    def prompt(self, prompt: OllamaPrompt) -> OllamaResponse:
        assert prompt

        response: requests.Response = requests.get(
            url=f"{self.base_url}/{self.prompt_endpoint}",
            data=prompt.model_dump_json()
        )
        
        response.raise_for_status()

        logger.info("()")
        return OllamaResponse(
            done=response.json().get('done',False),
            response=response.json().get('reponse',None)
        )
