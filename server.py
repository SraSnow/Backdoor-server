import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 550))
    server_socket.listen(1)
    print("Servidor aguardando conexão...")

    conn, addr = server_socket.accept()
    print(f"Conectado por {addr}")

    while True:
        data = input("Digite a mensagem para enviar ao cliente: ")
        conn.sendall(data.encode())
        if data.lower() == "sair":
            break

    conn.close()

if __name__ == "__main__":
    start_server()
