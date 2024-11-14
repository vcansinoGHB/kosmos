import socket
import threading

def handle_client(client_socket):
    DISCONNECT_MESSAGE = "DESCONEXION"
    connected = True
    while connected:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        if message == DISCONNECT_MESSAGE:
            connected = False
            print(f"-> Servidor cierra la conexión con el cliente.")
        else:
            print(f"Mensaje recibido: {message}")
            response = message.upper()
            client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5000
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor escuchando en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada desde {client_address}")
        client_handler = threading.Thread(
            target=handle_client,
            args=(client_socket,)
        )
        client_handler.start()

if __name__ == "__main__":
    main()