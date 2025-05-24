import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
import sqlite3

PORT = 8000
DB_FILE = 'myRestDB.db'

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        

        if path == '/':
            self.path = 'index.html'
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif path == '/api/users':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            #self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age FROM users")
            users_data = cursor.fetchall()
            conn.close()

            users_list = [{'id': row[0], 'name': row[1], 'age': row[2]} for row in users_data]
            response = json.dumps(users_list)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            #self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        pass

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
# The above code sets up a basic HTTP server using Python's built-in libraries. 