FROM tensorflow/tensorflow
COPY . /home/test
WORKDIR /home/test
CMD ["python", "minist.py"]
