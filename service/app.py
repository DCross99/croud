from fastapi import FastAPI
from uvicorn import run
from service.endpoints import features, probes


app = FastAPI()
app.include_router(probes.router)
app.include_router(features.router)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080, reload=True)
