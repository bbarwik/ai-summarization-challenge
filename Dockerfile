FROM python:3.12-slim-bookworm AS builder

WORKDIR /build

COPY . .
RUN pip install --no-cache-dir --prefix=/install .

FROM python:3.12-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    iptables \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --uid 1000 --shell /bin/bash appuser

COPY --from=builder /install /usr/local
COPY --chown=1000:1000 scripts /app/scripts

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
CMD ["python", "-m", "ai_summarization", "/workspace/"]