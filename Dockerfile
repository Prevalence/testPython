FROM python:3.6.7-stretch

ADD minist.py /
ADD requirements.txt /
ADD start.sh /
CMD ["bash", "start.sh"]