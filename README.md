# Deepsparse Llama2-7b Server

This repository is a simple example of [deepsparse cpu inference server](https://neuralmagic.com/deepsparse/) serving sparse zoo [llama2-7b](https://sparsezoo.neuralmagic.com/models/llama2-7b-llama2_chat_llama2_pretrain-base_quantized?hardware=deepsparse-c6i.12xlarge&comparison=llama2-7b-llama2_chat_llama2_pretrain-base) using [fastapi](https://fastapi.tiangolo.com/).

## Background

The repo is an experiment based on the [blogpost](https://neuralmagic.com/blog/fast-llama-2-on-cpus-with-sparse-fine-tuning-and-deepsparse/) from neural magic regarding `llama2` on CPUs based on Sparse fine-tuning and `DeepSparse`.

## Usage

The project is based on [uv](https://github.com/astral-sh/uv) and `python 3.11`. To run it locally you'll need to:

- Install all dependencies:

```bash
pip install .
```

- Download the model:

```
# export the model used -> default is "zoo:llama2-7b-llama2_chat_llama2_pretrain-base_quantized"
export PIPELINE_MODEL_PATH="your-model"

# export the model dir to store your model -> default is ""
export MODEL_DIR="./local-model"

python tools/download.py
```

- Serve the model:

```bash
fastapi run main.py --proxy-headers --port <port-number>
```

## Build

The project offers a `Containerfile` so we can build an image for the deepsparse fast api server. To build the image run:

```bash
<your-container-management-tool> build -f Containerfile -t <your-image-name>:<tag> .
```
