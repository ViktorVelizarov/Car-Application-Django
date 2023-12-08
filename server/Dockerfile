# Use an official Python runtime as a parent image
FROM python:3.8.2

# Set environment variables
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

# Install netcat
RUN apt-get update && apt-get install -y netcat

# Set the working directory to /app
ENV APP=/app
WORKDIR $APP

# Copy the current directory contents into the container at /app
COPY requirements.txt $APP/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . $APP/

# Make entrypoint.sh executable
RUN chmod +x /app/entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Define the entry point for the application
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# Default command to run the application
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangobackend.wsgi"]
