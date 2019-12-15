FROM python:3
LABEL maintainer="devfb"

WORKDIR /src
COPY requirements.txt /src/.
RUN pip install -r requirements.txt

COPY bob /src/.
COPY hamming /src/.
COPY hello-world /src/.
COPY high-scores /src/.
COPY isogram /src/.
COPY matrix /src/.
COPY pangram /src/.
COPY raindrops /src/.
COPY reverse-string /src/.
COPY twelve-days /src/.
COPY two-fer /src/.

CMD ["pytest", "-vs"]
