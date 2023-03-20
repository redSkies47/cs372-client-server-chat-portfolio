import socket

HOST = 'localhost'        # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows reusing ports
    s.bind((HOST, PORT))
    s.listen(1)
    print('\nServer listening on:', str(HOST), 'on port:', str(PORT))
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        print('Waiting for message...\n')
        while True:

            # Receive data and check for quitting it
            data = conn.recv(4096)
            data_str = data.decode('utf-8')
            if data_str: print(data_str)
            if '/q' in data_str: break

            # Send data from the 'server'
            input_str = input('>')
            input_bin = input_str.encode('utf-8')
            conn.sendall(input_bin)
            if '/q' in input_str: break

# Citation
# Date Accessed: March 17, 2023
# Adapted from:
# URL: https://docs.python.org/3.10/howto/sockets.html#using-a-socket
# Source Title: Socket Programming HOWTO
# Author: Gordon McMillan
# Last Updated Date: March 17, 2023

# Citation
# Date Accessed: March 17, 2023
# Adapted from:
# URL: https://docs.python.org/3.10/library/socket.html
# Source Title: Socket - Low-level networking interface
# Author: Python.org
# Last Updated Date: March 17, 2023

# Citation
# Date Accessed: March 17, 2023
# Adapted from:
# URL: https://realpython.com/python-sockets/
# Source Title: Socket Programming in Python (Guide)
# Author: Nathan Jennings

# Citation:
# Date Accessed: March 17, 2023
# Adapted from:
# URL: https://www.w3schools.com/python/ref_func_input.asp
# Source Title: Python input() Function
# Author: W3 Schools

# Citation
# Date Accessed: March 17, 2023
# Adapted from:
# URL: https://www.digitalocean.com/community/tutorials/python-string-encode-decode
# Source Title: Python String encode() decode()
# Author: Pankaj
# Publish Date: August 3, 2022