import time
import numpy as np
import os
from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
import cv2
from io import BytesIO
import base64
from tensorflow import keras

from flask_cors import CORS, logging

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
port = int(os.environ.get("PORT", 80))
app.config["DEBUG"] = False # turn off in prod


def format_image(img_string):
  img = Image.open(BytesIO(base64.b64decode(img_string.split(',')[1])))
  img_array = np.array(img)
  image = tf.image.resize(img_array, (224, 224))/255.0
  image = tf.expand_dims(image, 0)
  return image


def make_inference(model, image):
  prediction = model(image,training=False).numpy()
  predicted_batch = tf.squeeze(prediction).numpy()
  predicted_result = np.argmax(predicted_batch, axis=-1)
  return predicted_result


@app.route('/predict', methods=["POST"])
def predict():
  try:
    img_string =  request.json["data"]
    image = format_image(img_string)
    result = make_inference(model,image)
    if result == 0:
      return('This image is a Live Image')
    else:
      return('This image is pic of pic')
  except Exception:
    return('Bad image, try again!')
      


if __name__ == '__main__':
    model = keras.models.load_model("model_weight")
    app.run(host="0.0.0.0", port=port, use_reloader=False)