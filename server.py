import os
from socket import *
from file_handler import *
from data_validation import *
from urllib.parse import urlparse

if __name__ == "__main__":
    HOST = gethostname()  # Get local machine name
    PORT = 12345  # reserving a port for your service

    # open a firewall port
    os.system(f"sudo ufw allow {PORT}/tcp")

    with socket() as s:
        print('Server started!')
        print('Waiting for clients...')
        s.bind((HOST, PORT))  # bind to the port
        s.listen(5)  # waiting for client connection
        c, addr = s.accept()  # establish connection with client
        print('Connected with', addr)
        while True:
            clients_site = c.recv(1024).decode('UTF-8')  # getting a message from the remote client machine
            try:
                if clients_site=="exit":
                    c.send("SERVER >> Goodbye!".encode())
                    break
                if address_status_check(clients_site)==200:  # if connection to the http/s server succeed
                    print(addr,' >> ',clients_site)
                    parsed_link = urlparse(clients_site)  # take a part of the url without a protocol mention
                    os.system("traceroute " + str(parsed_link.netloc) + "> traceroute.log")  # traceroute to the website and write the log to the file
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







