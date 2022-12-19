# Pull base image
FROM python:3.10.7-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /fashion

# Install dependencies
COPY Pipfile Pipfile.lock /fashion/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /fashion/
