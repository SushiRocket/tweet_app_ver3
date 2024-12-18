FROM python:3.11-slim

# 基本ツールをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    openssh-client \
    curl \
    && apt-get clean

# 作業ディレクトリの作成
WORKDIR /workspace

# 必要なPythonパッケージのインストール
COPY requirements.txt /workspace/
RUN pip install --upgrade pip && pip install -r requirements.txt
