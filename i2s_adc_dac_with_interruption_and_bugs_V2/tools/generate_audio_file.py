# from __future__ import print_function

# import os
# import struct
# import wave
# from builtins import range


# def get_wave_array_str(filename, target_bits):
#     wave_read = wave.open(filename, 'r')
#     array_str = ''
#     nchannels, sampwidth, framerate, nframes, comptype, compname = wave_read.getparams()
#     sampwidth *= 8
#     for i in range(wave_read.getnframes()):
#         val, = struct.unpack('<H', wave_read.readframes(1))
#         scale_val = (1 << target_bits) - 1
#         cur_lim   = (1 << sampwidth) - 1
#         # scale current data to 8-bit data
#         val       = val * scale_val / cur_lim
#         val       = int(val + ((scale_val + 1) // 2)) & scale_val
#         array_str += '0x%x, ' % (val)
#         if (i + 1) % 16 == 0:
#             array_str += '\n'
#     return array_str


# def gen_wave_table(wav_file_list, target_file_name, scale_bits=8):
#     with open(target_file_name, 'w') as audio_table:
#         print('#include <stdio.h>', file=audio_table)
#         print('const unsigned char audio_table[] = {', file=audio_table)
#         for wav in wav_file_list:
#             print('processing: {}'.format(wav))
#             print(get_wave_array_str(filename=wav, target_bits=scale_bits), file=audio_table)
#         print('};\n', file=audio_table)
#     print('Done...')


# if __name__ == '__main__':
#     print('Generating audio array...')
#     wav_list = []
#     for filename in os.listdir('./'):
#         if filename.endswith('.wav'):
#             wav_list.append(filename)
#     gen_wave_table(wav_file_list=wav_list, target_file_name='audio_example_file.h')


# from pyftpdlib.handlers import FTPHandler
# from pyftpdlib.servers import FTPServer
# from pyftpdlib.authorizers import DummyAuthorizer


# class MyHandler(FTPHandler):

#     def on_connect(self):
#         print ("%s:%s connected" % (self.remote_ip, self.remote_port))

#     def on_disconnect(self):
#         # do something when client disconnects
#         pass

#     def on_login(self, username):
#         # do something when user login
#         pass

#     def on_logout(self, username):
#         # do something when user logs out
#         pass

#     def on_file_sent(self, file):
#         fichier = "/home/laura/Bureau/ProjetS10/traitement_wav/Test_secouage.wav"
#         file = open(fichier, 'rb') # ici, j'ouvre le fichier ftp.py 
#         connect.storbinary('STOR '+fichier, file) # ici (où connect est encore la variable de la connexion), j'indique le fichier à envoyer
#         file.close() # on ferme le fichier  

#     def on_file_received(self, file):
#         # do something when a file has been received
#         pass

#     def on_incomplete_file_sent(self, file):
#         # do something when a file is partially sent
#         pass

#     def on_incomplete_file_received(self, file):
#         # remove partially uploaded files
#         import os
#         os.remove(file)
# from __future__ import print_function

# # import os
# # import struct
# # import wave
# # from builtins import range


# # def get_wave_array_str(filename, target_bits):
# #     wave_read = wave.open(filename, 'r')
# #     array_str = ''
# #     nchannels, sampwidth, framerate, nframes, comptype, compname = wave_read.getparams()
# #     sampwidth *= 8
# #     for i in range(wave_read.getnframes()):
# #         val, = struct.unpack('<H', wave_read.readframes(1))
# #         scale_val = (1 << target_bits) - 1
# #         cur_lim   = (1 << sampwidth) - 1
# #         # scale current data to 8-bit data
# #         val       = val * scale_val / cur_lim
# #         val       = int(val + ((scale_val + 1) // 2)) & scale_val
# #         array_str += '0x%x, ' % (val)
# #         if (i + 1) % 16 == 0:
# #             array_str += '\n'
# #     return array_str


# # def gen_wave_table(wav_file_list, target_file_name, scale_bits=8):
# #     with open(target_file_name, 'w') as audio_table:
# #         print('#include <stdio.h>', file=audio_table)
# #         print('const unsigned char audio_table[] = {', file=audio_table)
# #         for wav in wav_file_list:
# #             print('processing: {}'.format(wav))
# #             print(get_wave_array_str(filename=wav, target_bits=scale_bits), file=audio_table)
# #         print('};\n', file=audio_table)
# #     print('Done...')


# # if __name__ == '__main__':
# #     print('Generating audio array...')
# #     wav_list = []
# #     for filename in os.listdir('./'):
# #         if filename.endswith('.wav'):
# #             wav_list.append(filename)
# #     gen_wave_table(wav_file_list=wav_list, target_file_name='audio_example_file.h')


# def main():
#     authorizer = DummyAuthorizer()
#     authorizer.add_user('laura367', 'abc123', homedir='.', perm='elradfmwMT')
#     host = 'localhost'
#     user = 'laura367'
#     password = 'abc123'
#     connect = pyftpdlib(host,user,password) # on se connectes
#     authorizer.add_anonymous(homedir='.')

#     handler = MyHandler
#     handler.authorizer = authorizer
#     server = FTPServer(('', 2121), handler)
#     server.serve_forever()

# if __name__ == "__main__":
#     main()


from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login()
ftp.cwd('directory_name') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = 'Test_environ_1m_avec_voiture.wav' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'Test_environ_1m_avec_voiture.wav' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()
#downloadFile()