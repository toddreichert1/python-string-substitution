FROM python:3.9-slim

ADD pss.py ./

CMD ["python", "./pss.py"]