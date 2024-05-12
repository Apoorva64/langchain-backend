from typing import Optional, Union, List

from django.conf import settings
from django.core.management.base import BaseCommand
from langchain.llms import get_type_to_cls_dict
from pydantic import BaseModel

from api.models import NodeType


class Command(BaseCommand):
    help = "Imports the llm schemas from langchain"

    def handle(self, *args, **options):
        # llms_cls = get_type_to_cls_dict()
        # for llm_type, llm_cls in llms_cls.items():
        #     print(llm_cls().__pydantic_core_schema__)

        # TODO: convert class to json schema and import it to django
        ollama_schema = {
            "title": "ollama",
            "type": "object",
            "properties": {
                "base_url": {"type": "string", "default": "http://localhost:11434"},
                "model": {"type": "string", "default": "llama2"},
                "mirostat": {"type": "integer"},
                "mirostat_eta": {"type": "number"},
                "mirostat_tau": {"type": "number"},
                "num_ctx": {"type": "integer"},
                "num_gpu": {"type": "integer"},
                "num_thread": {"type": "integer"},
                "num_predict": {"type": "integer"},
                "repeat_last_n": {"type": "integer"},
                "repeat_penalty": {"type": "number"},
                "temperature": {"type": "number"},
                "stop": {"type": "array", "items": {"type": "string"}},
                "tfs_z": {"type": "number"},
                "top_k": {"type": "integer"},
                "top_p": {"type": "number"},
                "system": {"type": "string"},
                "template": {"type": "string"},
                "format": {"type": "string"},
                "timeout": {"type": "integer"},
                "keep_alive": {"type": ["integer", "string"]},
                "headers": {"type": "object"}
            },
            "required": ["base_url", "model"],
        }
        NodeType.objects.create(
            name="ollama",
            category="LLM",
            json_schema=ollama_schema
        )
