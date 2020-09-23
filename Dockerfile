FROM python:3.6

ENV PYTHONUNBUFFERED 1

WORKDIR /source

# Install essential packages
RUN apt-get update -y \
    && apt-get -y install \
        dumb-init gnupg wget ca-certificates apt-transport-https \
        ttf-wqy-zenhei unzip \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install requirements
EXPOSE 5000
COPY . /source
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade -r requirements.txt

# CMD ["python", "runjob.py"]