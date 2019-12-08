FROM python:3
LABEL maintainer="devfb"

RUN pip install pytest

WORKDIR /src
COPY hamming /src/.
COPY hello-world /src/.
COPY high-scores /src/.
COPY isogram /src/.
COPY matrix /src/.
COPY raindrops /src/.
COPY two-fer /src/.

CMD ["pytest", "-vs"]
