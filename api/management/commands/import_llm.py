from django.conf import settings
from django.core.management.base import BaseCommand
from langchain.llms import get_type_to_cls_dict


class Command(BaseCommand):
    help = "Imports the llm schemas from langchain"

    def handle(self, *args, **options):
        llms_cls = get_type_to_cls_dict()
        for llm_type, llm_cls in llms_cls.items():
            print(llm_cls().__pydantic_core_schema__)

        # TODO: convert class to json schema and import it to django
