# Base Image
FROM python:3.10-slim

# Set Working Directory
ENV APP_HOME /app
WORKDIR @APP_HOME
COPY . ./

# Install Requirements
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000
ENV PORT 5000

CMD exec gunicorn --bind :$PORT main:app --workers 1 --threads 1 --timeout 60