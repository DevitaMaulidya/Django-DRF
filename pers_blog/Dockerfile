# Pull Image dari Docker
FROM library/python:latest

# Set Bufferd Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Membuat Environment
ENV VIRTUAL_ENV=/opt/venv

RUN python -m venv $VIRTUAL_ENV

# Menjalankan Environment
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Proses Update Depedency di Sistem Operasi Image Docker
RUN apt update -y

# Setup Working Directory
RUN mkdir /app

RUN ls /app
WORKDIR /app

# Install Depedency
ADD . /app/

RUN pip install -r requirements.txt --no-cache-dir