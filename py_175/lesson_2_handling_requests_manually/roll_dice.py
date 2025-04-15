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
    split_request = request_line.split(' ')

    http_method = split_request[0]
    path = split_request[1].split('?')[0]

    query_strings = split_request[1].split('?')[1].split('&')

    params = {item.split('=')[0]:item.split('=')[1] for item in query_strings}

    
    response_body = ('<!DOCTYPE html>\n'
                    '<h1>Dice Game</h1>\n'
                    '<body>\n'
                    f'<p><strong>Request Line:</strong>Request Line: {request_line}</p>\n'
                    f'<p><strong>Request Line:</strong>HTTP Method: {http_method}</p>\n'
                    f'<p><strong>Request Line:</strong>Path: {path}</p>\n'
                    f'<p><strong>Request Line:</strong>Parameters: {params}</p>\n'
                    '<ul>'
                    )

    for _ in range(int(params["rolls"])):
        roll = random.randint(1,int(params["sides"]))
        response_body += f"<li>Roll: {roll}</li>\n"
    
    response_body += '</ul>\n'
    response_body += '</body>\n'

    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}\n")

    #The encode method converts the response string to bytes for transmission, then sendall sends the response to the client.
    client_socket.sendall(response.encode())
    client_socket.close()

    #run and go to http://localhost:3003 in your browser.