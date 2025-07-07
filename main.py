from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
import io

app = FastAPI()


@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    # Read file
    input_image = await file.read()

    # Remove background
    output_image = remove(input_image)

    # Prepare output stream
    return StreamingResponse(io.BytesIO(output_image), media_type="image/png")
