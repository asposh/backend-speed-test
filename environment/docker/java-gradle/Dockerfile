FROM asposh/bst-ubuntu-common

# Copy deploy directory
COPY ./deploy /var/deploy

# Install packages
RUN apt update \
    && apt install -y openjdk-17-jdk \

    # Gradle
    && wget -c https://services.gradle.org/distributions/gradle-7.4.2-bin.zip \
    && mkdir /opt/gradle \
    && unzip -d /opt/gradle gradle-7.4.2-bin.zip

# Gradle env
ENV PATH=$PATH:/opt/gradle/gradle-7.4.2/bin

EXPOSE 80 443

ENTRYPOINT ["/var/deploy/docker-entrypoint.sh"]
