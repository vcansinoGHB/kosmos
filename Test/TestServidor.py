import unittest
import socket

class TestServidor(unittest.TestCase):
    
    def test_mayusculas(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 5000))
        client_socket.send('hola'.encode())
        self.assertEqual(client_socket.recv(1024).decode(), 'HOLA')
        client_socket.close()
    
    def test_desconexion(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 5000))
        client_socket.send('DESCONEXION'.encode())
        self.assertEqual(client_socket.recv(1024).decode(), '')
        client_socket.close()


if __name__ == '__main__':
    unittest.main()