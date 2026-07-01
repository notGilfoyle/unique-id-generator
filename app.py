from fastapi import FastAPI

from id_generator.generator import SnowflakeGenerator

app = FastAPI()

generator = SnowflakeGenerator(worker_id=1)


@app.get("/generate-id")
def generate():

    return {
        "id": generator.generate_id()
    }