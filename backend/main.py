import tensorflow as tf
import numpy as np


from fastapi import FastAPI
from fastapi import UploadFile,File,HTTPException
from PIL import Image
from io import BytesIO
from pathlib import Path


BASE_DIR=Path(__file__).resolve().parent.parent
MODEL_PATH=BASE_DIR/"models"/"rice_leaf_disease_mobilenetv2.keras"
model=tf.keras.models.load_model(MODEL_PATH)

app=FastAPI(
    title="Rice Leaf Disease Detection API",
    description="Deep Learning API using MobileNetV2",
    version="1.0.0"
)
class_names = [
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Leaf Smut"
]
def preprocessing_image(contents):
    image=Image.open(BytesIO(contents))

    image=image.convert("RGB")
    image=image.resize((128,128))
    
    image_array=np.array(image)
    image_array=image_array.astype("float32")/255.0
    image_array = np.expand_dims(image_array, axis=0)

    return image_array

@app.post("/predict")
async def predict(file:UploadFile=File(...)):
    contents=await file.read()
    if len(contents)>5*1024*1024:
        raise HTTPException(
            status_code=400,
            detail="Image size should not exceed 5MB"
        )
    try:
        image=Image.open(BytesIO(contents))
        image.verify()

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid image file: {str(e)}"
        ) 
    
    
    processed_image = preprocessing_image(contents)
    predictions=model.predict(processed_image)
    predicted_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_index]
    confidence = float(np.max(predictions[0])) * 100
    
    
    return{
        "filename": file.filename,
        "predicted_disease": predicted_class,
        "confidence": round(confidence, 2)
    }   
