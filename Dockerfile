FROM tensorflow/tensorflow
ADD minist.py /
CMD ["python", "minist.py"]