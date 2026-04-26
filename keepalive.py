# Tiny HTTP keepalive so Render's free web tier doesn't kill the bot.
# Import and call keep_alive() before bot.run() in main.py.
import os, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class _H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
    def log_message(self, *a, **k): pass

def keep_alive():
    port = int(os.environ.get("PORT", "10000"))
    srv = HTTPServer(("0.0.0.0", port), _H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()

if __name__ == "__main__":
    keep_alive()
    import time
    while True: time.sleep(3600)
