FROM python:3.7 as base

# NTL
ENV LIBRARY_PATH /usr/local/lib
ENV LIBRARY_INCLUDE_PATH /usr/local/include
COPY --from=initc3/ntl:11.4.1-buster $LIBRARY_INCLUDE_PATH/NTL $LIBRARY_INCLUDE_PATH/NTL
COPY --from=initc3/ntl:11.4.1-buster $LIBRARY_PATH/libntl.a $LIBRARY_PATH/libntl.a

WORKDIR /usr/src/pyntl
COPY Makefile pyproject.toml setup.py setup.cfg ./
COPY src src


FROM base as dev

RUN apt-get update && apt-get install -y --no-install-recommends \
                vim \
        && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install cython
RUN pip install --editable .['dev']

COPY tests tests
COPY .flake8 pytest.ini ./

FROM base as dist

RUN pip install build

FROM scratch AS export-stage
COPY --from=dist /usr/src/pyntl/dist /
