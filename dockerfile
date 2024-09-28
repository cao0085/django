# 使用適合 M1 的 Python 映像檔，這裡使用的是 arm64 版本的 Python 3.9
FROM python:3.9-slim-buster

# 設定工作目錄
WORKDIR /app

# 複製本機的 requirements.txt 檔案到容器內
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 開放 8000 端口
EXPOSE 8000

# 預設命令：啟動 Django 開發伺服器，指向 myproject/manage.py
CMD ["tail", "-f", "/dev/null"]
