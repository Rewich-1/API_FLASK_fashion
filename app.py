from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    model = keras.models.load_model("fashion_mnist")
    id2class = {0: "T-shirt/top",
                1: "Trouser",
                2: "Pullover",
                3: "Dress",
                4: "Coat",
                5: "Sandal",
                6: "Shirt",
                7: "Sneaker",
                8: "Bag",
                9: "Ankle boot", }


    parameters = request.get_json(force=True)
    print("1")
    im = np.array(parameters['image'])
    print("2")
    im = im.astype("float32") / 255
    print("3")
    im = np.expand_dims(im, -1)[None]
    print("4")
    out = id2class[np.argmax(model.predict(im))]
    print("5")
    return out
if __name__ == '__main__':
    app.run(host='0.0.0.0')