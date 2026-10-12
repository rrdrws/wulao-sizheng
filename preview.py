"""本地可选预览器。正式上线到 GitHub Pages 不需要 Python。"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

if __name__ == '__main__':
    os.chdir(Path(__file__).resolve().parent)
    address = ('127.0.0.1', 8000)
    print(f'浏览器打开 http://{address[0]}:{address[1]}/')
    ThreadingHTTPServer(address, SimpleHTTPRequestHandler).serve_forever()
