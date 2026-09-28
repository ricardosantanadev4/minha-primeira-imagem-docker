from http.server import BaseHTTPRequestHandler, HTTPServer


class MeuApp(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        mensagem = """
        <html>
            <head>
                <title>Minha primeira imagem Docker</title>
            </head>
            <body>
                <h1>Olá! Minha primeira aplicação Docker!</h1>
                <p>Esta aplicação está rodando dentro de um container.</p>
            </body>
        </html>
        """

        self.wfile.write(mensagem.encode("utf-8"))


servidor = HTTPServer(("0.0.0.0", 8000), MeuApp)

print("Servidor iniciado na porta 8000...")

servidor.serve_forever()
