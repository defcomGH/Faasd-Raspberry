from fastapi import FastAPI
import time

app = FastAPI()

@app.get('/temperatura')
def get_temperatura():
    return {"timestamp": time.time(),"valor" : 25}

@app.get('/humedad')
def get_humedad():
    return {"timestamp": time.time(),"valor" : 25}