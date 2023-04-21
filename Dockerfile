#Use an official Python runRUN python manage.py makemigrations
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE school_app.settings

# Expose the port that Django listens on
EXPOSE 8000

# Run the command to start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
