from flask import Flask
import requests
import threading
import time

app = Flask("")

# ここにReplitのFlaskサーバーのURL（https://xxx.repl.coなど）を入れる
REPLIT_URL = "https://40136f86-36d6-4bcc-98ce-86ed32e085a0-00-2r8ncznvawljw.pike.replit.dev/"

@app.route("/")
def ping_replit():
    return "Ping server running"

def ping_loop():
    while True:
        try:
            print("Pinging Replit...")
            requests.get(REPLIT_URL)
        except Exception as e:
            print(f"Error pinging: {e}")
        time.sleep(280)  # 約4分40秒間隔（Replitのスリープ回避）

def run():
    threading.Thread(target=ping_loop).start()
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    run()