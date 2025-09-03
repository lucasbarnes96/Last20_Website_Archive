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
import json
from urllib.parse import urlparse, parse_qs

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def do_GET(self):
        # Handle specific paths that need mock responses
        if '/app/cms/ping' in self.path:
            self.send_mock_json({'status': 'ok'})
            return
        elif '/static/icons/' in self.path:
            self.send_mock_svg()
            return
        elif self.path == '/' or self.path == '/index' or self.path == '/home':
            # Show index page with links to both versions
            self.send_index_page()
            return
        elif self.path.startswith('/css/') and '.css' in self.path and '?' in self.path:
            # Handle CSS requests with query parameters
            clean_path = self.path.split('?')[0]
            self.path = clean_path
            super().do_GET()
            return
        elif self.path.startswith('/js/') and '.js' in self.path and '?' in self.path:
            # Handle JS requests with query parameters
            clean_path = self.path.split('?')[0]  
            self.path = clean_path
            super().do_GET()
            return
        
        # Default handling
        super().do_GET()
    
    def do_POST(self):
        # Handle API calls with mock responses
        if '/ajax/api/JsonRPC/' in self.path:
            self.send_mock_json({'result': 'archived'})
            return
        else:
            super().do_POST()
    
    def send_mock_json(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def send_mock_svg(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/svg+xml')
        self.end_headers()
        # Simple placeholder SVG
        svg = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><rect width="24" height="24" fill="#ccc"/></svg>'
        self.wfile.write(svg.encode())
    
    def send_index_page(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Last20 Website Archive</title>
            <meta charset="utf-8">
            <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
            <meta http-equiv="Pragma" content="no-cache">
            <meta http-equiv="Expires" content="0">
            <style>
                body { font-family: system-ui, -apple-system, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.6; background: #fff; }
                .option { background: #f5f5f5; padding: 2rem; margin: 1rem 0; border-radius: 8px; border: 2px solid #ddd; }
                .btn { background: #25abe2; color: white; padding: 15px 30px; border-radius: 6px; text-decoration: none; display: inline-block; margin: 0.5rem 0; font-weight: bold; font-size: 16px; }
                .btn:hover { background: #1a8fb8; transform: translateY(-1px); }
                .archive-notice { background: #fff3cd; border: 1px solid #ffeaa7; padding: 1.5rem; border-radius: 6px; color: #856404; margin: 2rem 0; }
                .troubleshoot { background: #e7f3ff; border: 1px solid #b3d9ff; padding: 1rem; border-radius: 6px; color: #0056b3; margin: 2rem 0; font-size: 14px; }
                h1 { color: #333; text-align: center; margin-bottom: 2rem; }
                .logo { text-align: center; font-size: 3rem; margin-bottom: 1rem; }
            </style>
        </head>
        <body>
            <div class="logo">🏛️</div>
            <h1>Last20 Website Archive</h1>
            
            <div class="archive-notice">
                <strong>📚 Archived Website</strong> - This is a preserved copy of Last20's website (www.last20.ca) for historical reference and memories.
            </div>
            
            <div class="option">
                <h2>🌟 Complete Archive (Recommended)</h2>
                <p>Full multi-page archive with all content, navigation, and news. All pages in one interactive site!</p>
                <a href="complete.html" class="btn">View Complete Archive</a>
            </div>
            
            <div class="option">
                <h2>📖 Simple Version</h2>
                <p>A clean, simplified single-page version that works perfectly offline.</p>
                <a href="simple.html" class="btn">View Simple Version</a>
            </div>
            
            <div class="option">
                <h2>⚙️ Original Version</h2>
                <p>The original Square Online version. Some features may not work due to missing external dependencies.</p>
                <a href="index.html" class="btn">View Original Version</a>
                <small style="display: block; margin-top: 1rem; color: #666;">
                    Note: This version requires external services and may show errors in the browser console.
                </small>
            </div>
            
            <div class="troubleshoot">
                <strong>🔧 Troubleshooting:</strong> If you see a loading spinner or blank page:
                <br>• Try refreshing the page (Ctrl+R or Cmd+R)
                <br>• Clear your browser cache
                <br>• Try the Simple Version instead - it works reliably!
            </div>
            
            <hr style="margin: 3rem 0;">
            
            <h3>About Last20</h3>
            <p>Last20 was a Canadian clean-tech startup that developed innovative plastic-infused pavement technology. They combined traditional pavement materials with low-density polyethylene to create sustainable infrastructure solutions.</p>
            
            <p><em>"Upcycling plastic into pavement - Canadian clean-tech innovators paving the way to a sustainable future!"</em></p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())
    
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
