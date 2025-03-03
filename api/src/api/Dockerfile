# Start with a base image
FROM python:3.10-slim

WORKDIR /app

COPY ../shared ./shared

COPY ../requirements.txt .

# Install shared dependencies
RUN pip install -r requirements.txt

COPY api/requirements.txt .
RUN pip install -r requirements.txt

COPY api .

CMD ["python", "api.py"]
