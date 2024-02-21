stoveml

Uses a custom ML model to determine whether or not a stove is on, based on training data from a camera pointing at the stove, then sends that state to Home Assistant via the hassAPI.

Training data is in training_data folder. Model can be trained at https://colab.research.google.com/drive/1oVGmJN9rRYyOdY2_zntwW3LOtpqRdWra

This code runs the inference based on the exported model file at model.pkl.

Instructions to run the inference service:
- Update the values in config.json to point to your camera stream and Home Assiant config
- Run "pip install -r requirements.txt" to install the requirements (ideally  in a virtualenv)
- Run "python infer.py" and make sure it works. Use CTRL+C to kill it.

To make this a long running service on a Docker container
- Run "docker buildx build -t stoveml ."
- Run "docker run -it stoveml" and make sure it works
- Run "docker run -d --restart unless-stopped stoveml"



