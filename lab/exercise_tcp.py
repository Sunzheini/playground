import socket
import threading
import json
import time


HOST = "127.0.0.1"
PORT = 65432


def start_server(server_ready_event):
    def handle_client(conn, addr):
        print(f"Connected by {addr}")
        with conn:
            buffer = b""
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"Client {addr} disconnected.")
                    break
                buffer += data

                # Assume each message ends with a newline
                while b"\n" in buffer:
                    msg, buffer = buffer.split(b"\n", 1)
                    try:
                        request = json.loads(msg.decode())
                        print(f"Received from {addr}: {request}")

                        # Process the message
                        response = process_message(request)
                        response_bytes = (json.dumps(response) + "\n").encode()
                        conn.sendall(response_bytes)
                    except json.JSONDecodeError:
                        print("Invalid JSON received.")

    def process_message(request):
        """Define how the server responds to messages"""
        msg_type = request.get("type")

        if msg_type == "ping":
            return {"type": "pong"}
        elif msg_type == "greeting":
            name = request.get("name", "Anonymous")
            return {"type": "reply", "message": f"Hello, {name}!"}
        else:
            return {"type": "error", "message": "Unknown command"}

    # set up
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        # Signal that the server is ready by setting the event
        server_ready_event.set()

        # listener loop
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()


def start_client():
    def send_json_message(message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((HOST, PORT))
            except ConnectionRefusedError:
                print("Server not ready or connection refused.")
                return

            msg = json.dumps(message) + "\n"
            s.sendall(msg.encode())

            data = s.recv(1024)
            response = json.loads(data.decode())
            print("Response from server:", response)

    # Example messages
    send_json_message({"type": "ping"})
    time.sleep(1)
    send_json_message({"type": "greeting", "name": "Alice"})
    time.sleep(1)
    send_json_message({"type": "unknown"})


def main():
    # Create an event to signal when the server is ready
    server_ready_event = threading.Event()  # avoid race condition, client waits until server is rdy

    def server_thread_function():
        start_server(server_ready_event)    # pass the event to the server

    def client_thread_function():

        server_ready_event.wait()  # Wait until the server is ready to accept connections
        start_client()

    server_thread = threading.Thread(target=server_thread_function)
    server_thread.start()

    client_thread = threading.Thread(target=client_thread_function)
    client_thread.start()

    server_thread.join()
    client_thread.join()


if __name__ == "__main__":
    main()
