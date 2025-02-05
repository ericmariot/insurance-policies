FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]