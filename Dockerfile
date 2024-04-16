# Use an official Python runtime as a parent image
FROM python:3.9

# Add a label to the image
LABEL maintainer="mykhailo"
LABEL version="1.0.1"
LABEL description="Docker image which pings your nginx container infinitely"

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# delete requirements.txt
RUN rm /app/requirements.txt