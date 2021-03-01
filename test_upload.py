from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer


class MyHandler(FTPHandler):

    def on_connect(self):
        print ("%s:%s connected" % (self.remote_ip, self.remote_port))

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        fichier = "/home/laura/Bureau/ProjetS10/traitement_wav/Test_secouage.wav"
        file = open(fichier, 'rb') # ici, j'ouvre le fichier ftp.py 
        connect.storbinary('STOR '+fichier, file) # ici (où connect est encore la variable de la connexion), j'indique le fichier à envoyer
        file.close() # on ferme le fichier  

    def on_file_received(self, file):
        # do something when a file has been received
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('laura367', 'abc123', homedir='.', perm='elradfmwMT')
    host = 'localhost'
    user = 'laura367'
    password = 'abc123'
    authorizer.add_anonymous(homedir='.')

    handler = MyHandler
    handler.authorizer = authorizer
    server = FTPServer(('', 2121), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
