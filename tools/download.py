import os
from sparsezoo import Model

PIPELINE_MODEL_PATH: "str" = os.getenv(
    "PIPELINE_MODEL_PATH", "zoo:llama2-7b-llama2_chat_llama2_pretrain-base_quantized"
)

MODEL_DIR: "str" = os.getenv("MODEL_DIR", "./local-model")

assert PIPELINE_MODEL_PATH and MODEL_DIR

sz_model = Model(PIPELINE_MODEL_PATH, MODEL_DIR)
sz_model.deployment.download()
