import socket
import random

#create TCP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#AF_INET: Specifies the address family (IPv4 in this case). IPv4 uses 4-byte addresses and is the most widely used version of the Internet Protocol.
#SOCK_STREAM: Indicates that we are using a TCP socket, designed for continuous streams of data.

#We need to tell our server where to listen for requests. We'll use 'localhost' and port 3003 for this purpose. I
server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

#An infinite loop alone will allow us to continue to listen for connections
while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    #With the connection established, we can read the incoming data:
    request = client_socket.recv(1024).decode()

    #Browsers often automatically request a site's favicon (the little icon in a tab). We're not handling such requests in our simple server, so we skip them. 
    if (not request) or ('favicon.ico' in request):
        client_socket.close()
        continue

    #Finally, we want to grab the first line of the request, construct a valid HTTP response, and send it to the client.
    request_line = request.splitlines()[0]


    roll = random.randint(1,6)
    response_body = f"{request_line}\n{roll}\n"

    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}\n")

    #The encode method converts the response string to bytes for transmission, then sendall sends the response to the client.
    client_socket.sendall(response.encode())
    client_socket.close()

    #run and go to http://localhost:3003 in your browser.