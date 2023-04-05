# Set the base image to use for the container
FROM ubuntu:latest

# Update the package manager and install basic utilities
RUN apt-get update && \
    apt-get install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    python3 \
    python3-pip

# Set the default working directory
WORKDIR /app

# Expose any ports required by the application
EXPOSE 80

# Install any required Python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the default command to run when the container starts
CMD ["bash"]
