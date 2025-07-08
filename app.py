from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/signal/")
async def receive_signal(request: Request):
    data = await request.json()
    print("Received:", data)
    return {"status": "received"}

   
