FROM python:3.7

# NTL
ENV LIBRARY_PATH /usr/local/lib
ENV LIBRARY_INCLUDE_PATH /usr/local/include
COPY --from=initc3/ntl:11.4.1-buster $LIBRARY_INCLUDE_PATH/NTL $LIBRARY_INCLUDE_PATH/NTL
COPY --from=initc3/ntl:11.4.1-buster $LIBRARY_PATH/libntl.a $LIBRARY_PATH/libntl.a

RUN apt-get update && apt-get install -y --no-install-recommends \
                vim \
        && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /usr/src/pyntl

COPY setup.py setup.cfg ./
COPY src src

RUN pip install cython
RUN pip install --editable .['dev']

COPY tests tests
COPY .flake8 Makefile pytest.ini ./
