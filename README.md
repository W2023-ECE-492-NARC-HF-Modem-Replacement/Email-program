# Email-program

# Server
To run the NARC-server, run the following code

```
python narc_server.py <hostname> <port>
```

server receives info from client and then sends an email using SMTP server to the recipient.

# Client
To run the NARC-client, run the following code

```
python narc_client.py <server hostname> <server port>
```

The client asks the user to input their email, email login password, recipient, subject and body. The client then passes this information on to the server.
