FROM ubuntu:20.04

ENV TZ=Europe/Moscow

# Copy deploy directory
COPY ./deploy /var/deploy

# Install packages 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && apt update \
    && apt install -y \
        software-properties-common \
        curl \
        git \
        zip \
        wget \
        python3 \
        python3-pip \

    # Pip
    && pip3 install -r /var/deploy/python/requirements.txt

EXPOSE 80 443

CMD ["echo", "Ubuntu init..."]  
