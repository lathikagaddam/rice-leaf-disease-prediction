# 🌾 Rice Leaf Disease Detection – End-to-End Deployment

## 📌 Project Overview

Rice Leaf Disease Detection is a Deep Learning project that uses a pre-trained and fine-tuned **MobileNetV2** model to identify diseases in rice leaf images.

The project integrates a trained TensorFlow/Keras model with **FastAPI** to create an image-based prediction API. Users can upload a rice leaf image, and the API processes the image and predicts the disease category.

## 🎯 Objectives

- Detect diseases in rice leaf images using Deep Learning.
- Use MobileNetV2 for image classification.
- Build a REST API using FastAPI.
- Process uploaded images using Pillow and NumPy.
- Return predicted disease names and confidence scores.
- Prepare the application for frontend integration and cloud deployment.

## 🦠 Disease Classes

The model identifies three categories:

1. Bacterial Leaf Blight
2. Brown Spot
3. Leaf Smut

## 🧠 Model Details

| Parameter | Description |
|---|---|
| Model | MobileNetV2 |
| Framework | TensorFlow / Keras |
| Input Image Size | 128 × 128 |
| Color Channels | RGB (3) |
| Input Shape | (1, 128, 128, 3) |
| Model Format | `.keras` |
| Number of Classes | 3 |

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- FastAPI
- Uvicorn
- Pillow
- NumPy
- Pydantic
- Git and GitHub

## 📂 Project Structure

```text
Rice_Leaf_Disease_Deployment/
│
├── backend/
│   └── main.py
│
├── models/
│   └── rice_leaf_disease_mobilenetv2.keras
│
├── frontend/
│   └── app.py
│
├── requirements.txt
│
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Rice_Leaf_Disease_Deployment
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Running the FastAPI Application

Start the FastAPI server from the project root directory:

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

### Image Prediction Endpoint

**Endpoint:** `/predict`

**Method:** `POST`

**Input:** Rice leaf image uploaded as a multipart file.

### Image Preprocessing

The uploaded image goes through the following steps:

1. Image validation.
2. RGB conversion.
3. Resizing to 128 × 128 pixels.
4. Conversion into a NumPy array.
5. Pixel normalization.
6. Addition of a batch dimension.

The final input shape is:

```text
(1, 128, 128, 3)
```

### Prediction Output

The API returns the predicted disease category and its confidence score.

Example response:

```json
{
    "filename": "rice_leaf.jpg",
    "predicted_disease": "Brown Spot",
    "confidence": 96.45
}
```

*Example output only; actual predictions and confidence scores depend on the uploaded image.*

## 🔄 Project Workflow

```text
Rice Leaf Image
       |
       v
FastAPI Image Upload
       |
       v
Image Validation
       |
       v
Image Preprocessing
       |
       v
MobileNetV2 Model
       |
       v
Disease Classification
       |
       v
Predicted Disease
       |
       v
Confidence Score
```

## 📈 Future Improvements

- Develop a Streamlit frontend for image uploads.
- Deploy the FastAPI backend to Render.
- Integrate the frontend with the deployed API.
- Improve model performance with additional training data.
- Add prediction history and downloadable results.

## 👩‍💻 Author

**GADDAM LATHIKA**

Aspiring AI / Machine Learning Engineer

**Areas of Interest:** Artificial Intelligence, Machine Learning, Deep Learning, Computer Vision and API Development.

---

⭐ If you find this project useful, feel free to explore the repository!
