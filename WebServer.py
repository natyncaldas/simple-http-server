import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:

    try:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        print(request)
        filename = request.split()[1][1:]
        if (filename == '' or filename == 'favicon.ico'):
            f = open("index.html", encoding="utf8")
        else:
            f = open(filename, encoding="utf8") 
            
        data = f.read()
        f.close()

        # Send HTTP response
        response = 'HTTP/1.1 200 OK\n\n' + data
        client_connection.send(response.encode())

        # Close the client connection socket
        client_connection.close()

    except IOError:
        f = open("not_found.html", encoding="utf8")
        not_found = f.read()
        response = 'HTTP/1.1 404 Not Found\n\n' + not_found
        client_connection.send(response.encode())   
        # Close the client connection socket
        client_connection.close()
    except:
        f = open("error.html", encoding="utf8")
        server_error = f.read()
        response = 'HTTP/1.1 500 Internal Server Error\n\n' + server_error
        client_connection.send(response.encode()) 
        # Close the client connection socket
        client_connection.close()


# Close socket
server_socket.close()