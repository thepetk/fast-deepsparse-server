FROM python:3.11.11-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install .

ARG PIPELINE_MODEL_PATH="zoo:llama2-7b-llama2_chat_llama2_pretrain-base_quantized"

ARG MODEL_DIR="./local-model"

RUN python tools/download.py

ARG PORT=8000

EXPOSE $PORT

ENTRYPOINT ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", $PORT]