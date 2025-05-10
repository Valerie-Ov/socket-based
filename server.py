import os
from socket import *
from file_handler import *
from data_validation import *
from write_tracelog import *
from urllib.parse import urlparse

def handle_port_num(chosen_port):
    env_path: str = ".env"
    with open(env_path, "w") as f:
        f.write(f"SERVICE_PORT={chosen_port}\n")

if __name__ == "__main__":
    HOST = gethostname()  # Get local machine name

    with socket() as s:
        print('Server started!')
        print('Waiting for clients...')

        s.bind((HOST, 0))  # bind to the free port
        handle_port_num(s.getsockname()[1])

        s.listen(5)  # waiting for client connection
        c, addr = s.accept()  # establish connection with client
        print('Connected with', addr)
        while True:
            clients_site = c.recv(1024).decode('UTF-8')  # getting a message from the remote client machine
            print(f"Received from client: {clients_site}")

            try:
                if clients_site=="exit":
                    c.send("SERVER >> Goodbye!".encode())
                    break
                if address_status_check(clients_site)==200:  # if connection to the http/s server succeed
                    print(addr,' >> ',clients_site)
                    write_logs(clients_site)
                    c.send(get_file_contents().encode())

            except PermissionError:
                c.send("SERVER >> You don't have permission to work with the file".encode())
            except FileNotFoundError:
                c.send("SERVER >> The file doesn't exist on the server".encode())
            except error.HTTPError:   # connection to the website failed
                c.send("SERVER >> Wrong URL format".encode())
            except error.URLError:  # website not reached
                c.send("SERVER >> Address not found".encode())
            except ValueError:
                c.send("SERVER >> Invalid web address".encode())







