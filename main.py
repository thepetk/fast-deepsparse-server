from dataclasses import dataclass
import os
from deepsparse import TextGeneration
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

MODEL_DIR: "str" = os.getenv("MODEL_DIR", "./local-model")

assert MODEL_DIR

pipeline = TextGeneration(model_path=MODEL_DIR)


class InputData(BaseModel):
    prompt: "str"


@app.post("/inference")
def inference(data: "InputData") -> "dict[str, str]":
    output = pipeline(prompt=data.prompt)
    return {"results": output.generations[0].text}
