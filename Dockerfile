FROM python:3.6.7-stretch

ADD minist.py /
ADD requirements.txt /
CMD ["bash", "start.sh"]