FROM python:3.10-slim

# System deps
RUN apt-get update && apt-get install -y \
    nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# Install rembg + python libs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js deps
COPY package.json .
RUN npm install

# Copy app files
COPY server.js .

EXPOSE 8080

CMD ["node", "server.js"]
