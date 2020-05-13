FROM python:3.8-slim as build

RUN pip install poetry \
    && mkdir -p /build/cloudrun_lifecycle
COPY pyproject.toml /build/
COPY cloudrun_lifecycle /build/cloudrun_lifecycle/
RUN cd /build && poetry build

FROM python:3.8-slim

RUN apt update \
    && apt install -y --no-install-recommends \
        libmagic-dev \
    && apt -y clean \
    && rm -rf /var/lib/apt/lists/*
COPY --from=build /build/dist/cloudrun_lifecycle-*-py3-none-any.whl /
RUN pip install /cloudrun_lifecycle-*-py3-none-any.whl

ENTRYPOINT ["python"]
CMD ["-m", "cloudrun_lifecycle"]
