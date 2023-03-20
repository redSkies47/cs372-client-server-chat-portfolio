import socket

HOST = 'localhost'        # The remote host
PORT = 50007              # The same port as used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('\nConnected to', HOST, 'on port:', str(PORT))
    print('Type /q to quit')
    print('Enter message to send...\n')
    s.connect((HOST, PORT))
    while True:
        input_str = input('>')
        input_bin = input_str.encode('utf-8')
        s.sendall(input_bin)
        if '/q' in input_str: break
        data = s.recv(4096)
        new_message = data.decode('utf-8')
        if '/q' in new_message: break
        print(new_message)
