from fastai.vision.all import load_learner, PILImage
from time import sleep
import cv2, os

import common
import hass_stove

config = common.get_config()

print("loading model...")
learn_inf = load_learner("model.pkl")

print("starting inference")
while True:
    cv2_image = common.get_image(config)
    rgb_frame = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    pil_image = PILImage.create(rgb_frame)

    prediction = learn_inf.predict(pil_image)[0]
    print(prediction)
    if prediction == 'off':
        hass_stove.turn_off()
    else:
        hass_stove.turn_on()
    sleep(5)
