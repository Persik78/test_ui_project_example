FROM python:3.13

RUN apt-get update && apt-get install -y \
    wget gnupg2 unzip curl tar fonts-liberation \
    libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 \
    libcairo2 libcups2 libdbus-1-3 libgbm1 libglib2.0-0 libgtk-3-0 \
    libnspr4 libnss3 libpango-1.0-0 libwayland-client0 \
    libxcomposite1 libxkbcommon0 xdg-utils libu2f-udev libvulkan1 xvfb \
    && rm -rf /var/lib/apt/lists/*

# Chrome
ARG CHROME_VERSION=139.0.7258.68
RUN wget https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chrome-linux64.zip \
    && rm -rf /opt/chrome \
    && unzip -o chrome-linux64.zip -d /opt/chrome \
    && rm chrome-linux64.zip
ENV CHROME_BINARY="/opt/chrome/chrome-linux64/chrome"

# Chromedriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip \
    && rm -rf /opt/chromedriver \
    && unzip -o chromedriver-linux64.zip -d /opt/chromedriver \
    && rm chromedriver-linux64.zip \
    && ln -sf /opt/chromedriver/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver

# JDK 17 (с фиксированным JAVA_HOME)
RUN mkdir -p /opt/java && \
    curl -fsSL https://api.adoptium.net/v3/binary/latest/17/ga/linux/x64/jdk/hotspot/normal/eclipse -o /tmp/openjdk17.tar.gz && \
    tar -xzf /tmp/openjdk17.tar.gz -C /opt/java --strip-components=1 && \
    rm /tmp/openjdk17.tar.gz
ENV JAVA_HOME=/opt/java
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Allure
RUN curl -o allure-2.34.1.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.34.1/allure-commandline-2.34.1.tgz && \
    tar -zxvf allure-2.34.1.tgz -C /opt/ && \
    ln -sf /opt/allure-2.34.1/bin/allure /usr/bin/allure && \
    rm allure-2.34.1.tgz

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
