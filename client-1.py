import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conecte-se ao endereço IP e porta fornecidos pelo Ngrok
    client_socket.connect(('187.69.82.157', 550))

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Recebido do servidor: {data.decode()}")
        if data.decode().lower() == "sair":
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
