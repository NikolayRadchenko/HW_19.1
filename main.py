from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """ 
        Специальный класс, который отвечает за 
        обработку входящих запросов от клиентов
    """

    def __clients(self):
        with open("contacts.html", encoding="utf-8") as index_file:
            page = index_file.read()
            return page

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_ = parse_qs(urlparse(self.path).query)
        print(query_)
        page_content = self.__clients()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
