FROM tensorflow/tensorflow:latest-gpu-py3

ADD demo.py /root/k8s/

CMD ["python","/root/k8s/demo.py"]
