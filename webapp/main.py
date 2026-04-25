import io
import uuid

from datetime import datetime
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
from threading import Lock

app = FastAPI()
lock = Lock()

history = []
IMG_SUFFIXES = {"png", "jpg", "jpeg", "gif", "webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
MIN_FILE_SIZE = 1024  # 1KB


@app.get("/history")
def read_history():
    with lock:
        return {
            "total": len(history),
            "history": history
        }


@app.post("/upload-compress")
def upload_compress(file: UploadFile = File(...)):
    try:
        # Judge size of the file whether it is valid
        check_file_size(file)

        # Judge the file whether it is valid
        if not is_valid_img_file(file):
            raise HTTPException(status_code=400, detail="This file is not of image format")

        # original Image
        original_image_byte = file.file.read()
        file.file.seek(0)
        original_image = Image.open(io.BytesIO(original_image_byte))

        # Compress the Image
        compressed_image_bytes_io = compress_image(file)
        compressed_image_byte = compressed_image_bytes_io.getvalue()
        compressed_image = Image.open(io.BytesIO(compressed_image_byte))

        with lock:
            record = {
                "id": str(uuid.uuid4()),
                "img_name": file.filename,
                "original_img_info": {
                    "format": original_image.format,
                    'width': original_image.width,
                    'height': original_image.height,
                    "byte": len(original_image_byte)
                },
                "compressed_img_info": {
                    "format": compressed_image.format,
                    'width': compressed_image.width,
                    'height': compressed_image.height,
                    "byte": len(compressed_image_byte)
                },
                "created_at": datetime.now().strftime("%B %d, %Y %H:%M:%S")
            }
            history.append(record)
        return {
            "status": "success",
            "info": record
        }
    except Exception as e:
        return {"error": str(e)}


def is_valid_img_file(file: UploadFile = File(...)) -> bool:
    try:
        # Judge the file suffix whether it belongs to the image format
        suffix = get_file_suffix(file.filename)
        if suffix not in IMG_SUFFIXES:
            return False

        # Judge the image whether it is normal to open, ensure the image is not broken
        img_byte = file.file.read()
        file.file.seek(0)
        img = Image.open(io.BytesIO(img_byte))
        img.verify()
        img.close()
        return True
    except Exception:
        return False


def get_file_suffix(filename: str) -> str:
    if "." in filename:
        return filename.split(".")[-1].lower()
    else:
        return ""


def compress_image(file: UploadFile = File(...)):
    image_byte = file.file.read()
    file.file.seek(0)
    img = Image.open(io.BytesIO(image_byte)).convert("RGB")

    output = io.BytesIO()
    img.save(output, format="JPEG", quality=50)
    output.seek(0)
    return output


def check_file_size(file: UploadFile = File(...)):
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(413, f"File size is too large, the maximum is {MAX_FILE_SIZE / (1024 * 1024)}MB")
    if file_size < MIN_FILE_SIZE:
        raise HTTPException(400, "File size is too small")
