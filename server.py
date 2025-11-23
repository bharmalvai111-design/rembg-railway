from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
import uvicorn
import os

app = FastAPI()

@app.post("/remove")
async def remove_bg(image: UploadFile = File(...)):
    input_data = await image.read()
    output = remove(input_data)
    return Response(output, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
