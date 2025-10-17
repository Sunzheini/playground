import socket
import threading


# ------------------------------------------------------
# Sockets
# ------------------------------------------------------
def start_server(server_ready_event):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))  # Bind to localhost and port 65432
    server_socket.listen()

    print("Server listening on port 65432...")

    # Signal that the server is ready by setting the event
    server_ready_event.set()

    conn, addr = server_socket.accept()  # Wait for a client to connect
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)  # Receive data from client
        if not data:
            break
        print(f"Received: {data.decode()}")
        conn.sendall(data)  # Echo back the received data

    conn.close()
    server_socket.close()


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))  # Connect to server

    message = "Hello, Server!"
    client_socket.sendall(message.encode())  # Send data
    data = client_socket.recv(1024)  # Receive echo from server

    print(f"Received from server: {data.decode()}")

    client_socket.close()


def main():
    # Create an event to signal when the server is ready
    server_ready_event = threading.Event()  # avoid race condition, so client waits until server is ready!

    # Define the server thread
    def server_thread_function():
        start_server(server_ready_event)

    # Define the client thread
    def client_thread_function():
        # Wait until the server is ready to accept connections
        server_ready_event.wait()
        start_client()

    # Create and start server thread
    server_thread = threading.Thread(target=server_thread_function)
    server_thread.start()

    # Create and start client thread
    client_thread = threading.Thread(target=client_thread_function)
    client_thread.start()

    # Wait for both threads to finish
    server_thread.join()
    client_thread.join()


if __name__ == "__main__":
    main()
