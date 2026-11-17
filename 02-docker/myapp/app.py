from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my DevOps Portfolio App!\n"

@app.route('/health')
def health():
    return "OK\n", 200

@app.route('/info')
def info():
    hostname = socket.gethostname()
    return f"Running on server: {hostname}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
