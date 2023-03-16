import socket
import sys
import smtplib
from narc_email_client import send_email



def server_program():
    # get the hostname
    if len(sys.argv) != 3:
        print('Usage: python client.py <hostname> <port>')
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    data_dict = {}
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        else:
            data_dict = eval(str(data))
        print("from connected user: " + str(data))
        return_data = "ack"
        conn.send(return_data.encode())  # send data to the client

    conn.close()  # close the connection
    return data_dict

if __name__ == '__main__':
    data = server_program()
    send_email(data)
