import http.server
import socketserver
import os
import socket
import re

PORT = 8000
DIRECTORY = r"c:\Users\moham\Downloads\blackroots website"

class RangeHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def send_head(self):
        """Common code for GET and HEAD commands.
        Supports HTTP 206 Partial Content for video/audio seeking on iOS & Android.
        """
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            parts = [path, "index.html"]
            index = os.path.join(*parts)
            if os.path.exists(index):
                path = index
            else:
                return super().send_head()

        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None

        fs = os.fstat(f.fileno())
        total_length = fs[6]

        # Check for Range header
        range_header = self.headers.get('Range')
        if range_header and ctype.startswith(('video/', 'audio/', 'application/octet-stream')):
            range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
            if range_match:
                first_byte = int(range_match.group(1))
                last_byte = int(range_match.group(2)) if range_match.group(2) else total_length - 1
                if last_byte >= total_length:
                    last_byte = total_length - 1
                
                length = last_byte - first_byte + 1

                self.send_response(206, "Partial Content")
                self.send_header("Content-Type", ctype)
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Content-Range", f"bytes {first_byte}-{last_byte}/{total_length}")
                self.send_header("Content-Length", str(length))
                self.send_header("Cache-Control", "public, max-age=3600")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

                f.seek(first_byte)
                return f

        # Standard 200 response
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(total_length))
        self.send_header("Accept-Ranges", "bytes")
        if ctype.startswith(('video/', 'image/', 'font/')):
            self.send_header("Cache-Control", "public, max-age=3600")
        else:
            self.send_header("Cache-Control", "no-cache, must-revalidate")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        return f

    def copyfile(self, source, outputfile):
        """Copy file chunk according to range request length"""
        range_header = self.headers.get('Range')
        if range_header and hasattr(self, '_headers_buffer'):
            # If partial content was sent
            try:
                length = int([h.split(':')[1].strip() for h in self._headers_buffer if h.startswith(b'Content-Length:')][0])
            except Exception:
                length = None
            
            if length:
                buffer_size = 64 * 1024
                bytes_sent = 0
                while bytes_sent < length:
                    to_read = min(buffer_size, length - bytes_sent)
                    chunk = source.read(to_read)
                    if not chunk:
                        break
                    outputfile.write(chunk)
                    bytes_sent += len(chunk)
                return

        super().copyfile(source, outputfile)

class DualStackServer(socketserver.ThreadingTCPServer):
    address_family = socket.AF_INET6 if socket.has_ipv6 else socket.AF_INET
    allow_reuse_address = True

    def server_bind(self):
        if socket.has_ipv6:
            try:
                self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            except Exception:
                pass
        super().server_bind()

if __name__ == '__main__':
    server_address = ("::", PORT) if socket.has_ipv6 else ("0.0.0.0", PORT)
    try:
        httpd = DualStackServer(server_address, RangeHTTPRequestHandler)
        print(f"DualStack Streaming Server listening on port {PORT} (HTTP 206 Range Enabled)...")
        httpd.serve_forever()
    except Exception as e:
        print("Fallback to IPv4 TCPServer:", e)
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("0.0.0.0", PORT), RangeHTTPRequestHandler) as httpd:
            print(f"IPv4 Streaming Server listening on port {PORT} (HTTP 206 Range Enabled)...")
            httpd.serve_forever()
