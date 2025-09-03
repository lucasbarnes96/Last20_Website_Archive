#!/usr/bin/env python3
"""
Simple HTTP server for Last20 Website Archive
Run this to serve the website locally on http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        # Add CORS headers to allow loading of external resources
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    try:
        with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
            print(f"🚀 Last20 Website Archive server starting...")
            print(f"📡 Serving on http://localhost:{PORT}")
            print(f"📁 Serving directory: {os.getcwd()}")
            print(f"🌐 Opening browser automatically...")
            print(f"⏹️  Press Ctrl+C to stop the server")
            
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped.")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use. Try a different port or stop the existing server.")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()
