import socket

def main():
    DISCONNECT_MESSAGE = "DESCONEXION"
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    host = '127.0.0.1'
    port = 5000
    client_socket.connect((host, port))
    conected = True

    while conected:
        message = input("Por favor, introduza su mensaje: ")
        encode_message = message.encode('utf-8')
        client_socket.sendall(encode_message)
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        _message = encode_message.decode('utf-8')
        if _message == DISCONNECT_MESSAGE:
            conected = False
        else:
            print(f"Respuesta del servidor: {response}")


if __name__ == "__main__":
    main()