
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Fashion-MNIST Classifier")

CLASS_NAMES = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

MODEL_PATH = "Task_3.1_FashionMNIST_TensorFlow_CNN.keras"

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

st.title("Fashion-MNIST Image Classifier")
st.write("Upload a 28×28 grayscale Fashion-MNIST-style image.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")
    st.image(image, caption="Uploaded image")

    image = image.resize((28, 28))
    x = np.array(image).astype("float32") / 255.0
    x = x[np.newaxis, ..., np.newaxis]

    try:
        model = load_model()
        probabilities = model.predict(x, verbose=0)[0]
        prediction = int(np.argmax(probabilities))

        st.subheader(f"Prediction: {CLASS_NAMES[prediction]}")
        st.write(f"Confidence: {probabilities[prediction] * 100:.2f}%")

        st.bar_chart(
            {CLASS_NAMES[i]: float(probabilities[i]) for i in range(10)}
        )
    except Exception as exc:
        st.error(
            "Could not load the trained model. "
            "Run Task 3.1 first so the .keras model file exists."
        )
        st.exception(exc)
