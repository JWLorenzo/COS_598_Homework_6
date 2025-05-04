FROM python:alpine
RUN pip install redis
RUN pip install requests
COPY co_worker.py /
CMD ["python", "co_worker.py"]
