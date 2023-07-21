# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install rye
RUN pip install rye

# Set work directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run rye to install dependencies
RUN rye install

# Specify the command to run your application
CMD ["rye", "start"]
