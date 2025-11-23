from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
import uvicorn
import os

app = FastAPI()

@app.post("/remove")
async def remove_bg(image: UploadFile = File(...)):
    input_data = await image.read()
    output_data = remove(input_data)
    return Response(output_data, media_type="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
