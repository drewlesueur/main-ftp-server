from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("lesueur", "lesueur", "/home/drew/tmp/ftp", perm="elradfmwM")
authorizer.add_anonymous("/home/drew/tmp/ftp", perm="elradfmwM")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
# server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
