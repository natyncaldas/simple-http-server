import socket
import os
from datetime import datetime

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('\033[1;32;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m Starting '+os.path.basename(__file__)+' ...')
print('\033[1;32;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m Listening on port %s' % SERVER_PORT)

while True:

    try:
        # Wait for client connections
        client_connection, client_address = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        
        filename = request.split()[1][1:] if request else ''
        
        if filename == '' or filename == 'favicon.ico':
            f = open("index.html", encoding="utf8")
        else:
            f = open(filename, encoding="utf8") 
            print('\033[1;32;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m' + request)
            
        data = f.read()
        f.close()

        # Send HTTP response
        response = 'HTTP/1.1 200 OK\n\n' + data
        client_connection.send(response.encode())

        # Close the client connection socket
        client_connection.close()

    except IOError:
        f = open("error404.html", encoding="utf8")
        not_found = f.read()
        response = 'HTTP/1.1 404 Not Found\n\n' + not_found
        client_connection.send(response.encode())  
        print('\033[1;31;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m 404 Not Found\n')
        # Close the client connection socket
        client_connection.close()

    except UnicodeDecodeError:
        f = open("error415.html", encoding="utf8")
        media_error = f.read()
        response = 'HTTP/1.1 415 Unsupported Media Type\n\n' + media_error
        client_connection.send(response.encode()) 
        print('\033[1;31;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m 415 Unsupported Media Type\n')
        # Close the client connection socket
        client_connection.close()

    except (KeyboardInterrupt, SystemExit):
        print ('\033[1;33;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m Keyboard Interrupt')
        print ('\033[1;33;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m Stopping server...')

        # Close the client connection socket
        client_connection.close()
        break
    
    except:
        f = open("error500.html", encoding="utf8")
        server_error = f.read()
        response = 'HTTP/1.1 500 Internal Server Error\n\n' + server_error
        client_connection.send(response.encode()) 
        print('\033[1;31;40m['+datetime.now().strftime("%H:%M:%S") +'] \033[0;37;40m 500 Internal Server Error\n')
        # Close the client connection socket
        client_connection.close()
        raise

# Close socket
server_socket.close()