from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib

from entries import EntryHandler

class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def get_post_body(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # JSON string -> Python dict
        post_body = json.loads(post_body)

        return post_body

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # URL includes query string - parse it and return tuple of resource name, 
        # query string param, and value for that param in the query string
        if "?" in resource:
            resource, param = resource.split("?")
            key, value = param.split("=")

            value = urllib.parse.unquote(value)

            return ( resource, key, value )

        # Otherwise, it is just a request for either all items of a particular resource,
        # or a single item by ID
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

        return (resource, id) 

    def get_resource_handler(self, resource):
        if resource == 'entries':
            return EntryHandler()
        
        raise Exception('Unrecognized resource')

    def do_GET(self):
        self._set_headers(200)
        response = {}

        url_parts = self.parse_url(self.path)

        if len(url_parts) == 2:
            resource, id = url_parts

            resource_handler = self.get_resource_handler(resource)

            if id is None:
                response = resource_handler.get_all()
            else:
                response = resource_handler.get_by_id(id)

        self.wfile.write(response.encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == '__main__':
    main()