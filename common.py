import cv2, json, shutil, numpy

CONFIG = "config.json"
CONFIG_BAK = "config_bak.json"

def get_config():
    f = open(CONFIG)
    config = json.load(f)
    f.close()
    return config

def get_image(config):
    image = None
    if config['type'] == 'url':
        cap = cv2.VideoCapture(config['url'])
        _, image = cap.read()
    else:
        image = cv2.imread(config['file'])
    return image

def backup_config():
    shutil.copy(CONFIG, CONFIG_BAK)

    
