import socket
import sys


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print('Usage: python client.py <hostname> <port>')
    sys.exit()
host = sys.argv[1]
port = int(sys.argv[2])


client_socket.connect((host, port))


from_email = input("From: ")
to_email = input("To: ")
subject = input("Subject: ")
body = input("Body: \n")

message = {"From": from_email, "To": to_email, "Subject": subject, "Body": body}

str_message = str(message)

client_socket.send(str_message.encode())


data = client_socket.recv(1024)
print('Received from server:', data.decode())

client_socket.close()