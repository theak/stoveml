FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
ADD model.pkl /
ADD config.json /
ADD common.py /
ADD hass_stove.py /
ADD infer.py /
CMD [ "python", "./infer.py" ]
