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

        # for now just import Ollama

        class OllamaParams(BaseModel):
            base_url: str = "http://localhost:11434"
            """Base url the model is hosted under."""

            model: str = "llama2"
            """Model name to use."""

            mirostat: Optional[int] = None
            """Enable Mirostat sampling for controlling perplexity.
            (default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)"""

            mirostat_eta: Optional[float] = None
            """Influences how quickly the algorithm responds to feedback
            from the generated text. A lower learning rate will result in
            slower adjustments, while a higher learning rate will make
            the algorithm more responsive. (Default: 0.1)"""

            mirostat_tau: Optional[float] = None
            """Controls the balance between coherence and diversity
            of the output. A lower value will result in more focused and
            coherent text. (Default: 5.0)"""

            num_ctx: Optional[int] = None
            """Sets the size of the context window used to generate the
            next token. (Default: 2048)	"""

            num_gpu: Optional[int] = None
            """The number of GPUs to use. On macOS it defaults to 1 to
            enable metal support, 0 to disable."""

            num_thread: Optional[int] = None
            """Sets the number of threads to use during computation.
            By default, Ollama will detect this for optimal performance.
            It is recommended to set this value to the number of physical
            CPU cores your system has (as opposed to the logical number of cores)."""

            num_predict: Optional[int] = None
            """Maximum number of tokens to predict when generating text.
            (Default: 128, -1 = infinite generation, -2 = fill context)"""

            repeat_last_n: Optional[int] = None
            """Sets how far back for the model to look back to prevent
            repetition. (Default: 64, 0 = disabled, -1 = num_ctx)"""

            repeat_penalty: Optional[float] = None
            """Sets how strongly to penalize repetitions. A higher value (e.g., 1.5)
            will penalize repetitions more strongly, while a lower value (e.g., 0.9)
            will be more lenient. (Default: 1.1)"""

            temperature: Optional[float] = None
            """The temperature of the model. Increasing the temperature will
            make the model answer more creatively. (Default: 0.8)"""

            stop: Optional[List[str]] = None
            """Sets the stop tokens to use."""

            tfs_z: Optional[float] = None
            """Tail free sampling is used to reduce the impact of less probable
            tokens from the output. A higher value (e.g., 2.0) will reduce the
            impact more, while a value of 1.0 disables this setting. (default: 1)"""

            top_k: Optional[int] = None
            """Reduces the probability of generating nonsense. A higher value (e.g. 100)
            will give more diverse answers, while a lower value (e.g. 10)
            will be more conservative. (Default: 40)"""

            top_p: Optional[float] = None
            """Works together with top-k. A higher value (e.g., 0.95) will lead
            to more diverse text, while a lower value (e.g., 0.5) will
            generate more focused and conservative text. (Default: 0.9)"""

            system: Optional[str] = None
            """system prompt (overrides what is defined in the Modelfile)"""

            template: Optional[str] = None
            """full prompt or prompt template (overrides what is defined in the Modelfile)"""

            format: Optional[str] = None
            """Specify the format of the output (e.g., json)"""

            timeout: Optional[int] = None
            """Timeout for the request stream"""

            keep_alive: Optional[Union[int, str]] = None
            """How long the model will stay loaded into memory.
    
            The parameter (Default: 5 minutes) can be set to:
            1. a duration string in Golang (such as "10m" or "24h");
            2. a number in seconds (such as 3600);
            3. any negative number which will keep the model loaded \
                in memory (e.g. -1 or "-1m");
            4. 0 which will unload the model immediately after generating a response;
    
            See the [Ollama documents](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-do-i-keep-a-model-loaded-in-memory-or-make-it-unload-immediately)"""

            headers: Optional[dict] = None
            """Additional headers to pass to endpoint (e.g. Authorization, Referer).
            This is useful when Ollama is hosted on cloud services that require
            tokens for authentication.
            """

        NodeType.objects.create(
            name="Ollama",
            category="LLM",
            json_schema=OllamaParams.schema_json(indent=2),
        )
