FROM python:3.12-slim

# Install required system dependencies and locales
RUN apt-get update && apt-get install -y \
    locales \
    build-essential \
    libdbus-1-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    libglib2.0-dev \
    cmake \
    gettext \
    libcairo2-dev \
    libgirepository1.0-dev \
    python3-apt \
    librsync-dev \                
    libcups2-dev \                
    libsystemd-dev \              
    && rm -rf /var/lib/apt/lists/* 

# Set the locale to en_US.UTF-8 and generate locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=en_US.UTF-8

# Install Meson and Ninja via pip
#RUN pip install meson ninja
RUN pip install --root-user-action=ignore meson ninja


# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app


RUN pip uninstall --root-user-action=ignore -y kafka
RUN pip uninstall  --root-user-action=ignore -y confluent-kafka 
RUN pip uninstall  --root-user-action=ignore -y kafka-python


# Install Python dependencies (after removing python-apt from requirements.txt)
RUN pip install --root-user-action=ignore --no-cache-dir -r requirements.txt
#RUN pip install --root-user-action=ignore kafka-python six

# Expose port for FastAPI app
EXPOSE 8001

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
