FROM python
WORKDIR /myapp
COPY . /myapp
RUN pip install -r requirements.txt 
CMD ["python3", "-u", "scheduler.py"]