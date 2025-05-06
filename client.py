from socket import *
from data_validation import address_validation


if __name__ == '__main__':
    HOST = gethostname()  # get local machine name
    PORT = 12345  # reserving port for the service
    try:
        with socket() as s:  # creating a socket object
            s.connect((HOST, PORT))  # establishing a new connection to a remote machine
            while True:
               client_input = input("CLIENT >> Please check this website: ")
               s.sendall(client_input.encode())  # send url to the server
               if client_input == "exit":
                   print(s.recv(1024).decode('UTF-8'))  # display goodbye message
                   break
               elif address_validation(client_input):
                   print(s.recv(1024).decode('UTF-8'))  # display site response result

    except ConnectionRefusedError:  # couldn't establish a connection to the remote host
        print("No connection could be made because the target machine refused it")
    except ConnectionResetError:  # the established connection was reset by the remote host
        print("An existing connection was forcibly closed by the remote host")
    except ConnectionAbortedError:  # connection was aborted by remote host
        print("Connection aborted by your host machine")


