from fastapi import FastAPI

app = FastAPI()

@app.get("/mul10/{num}")
def mul10(num: float):
    return {"result": num * 10}

@app.get("/getcode")
def get_code():
    return {"code": "hello world spdx!!"}