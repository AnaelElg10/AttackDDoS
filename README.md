
# Botnet Simulator with Docker and Python

This project utilizes Docker to create a secure testing environment for simulating a botnet for educational purposes. The simulator consists of three main components: a Docker image configured with Kali Linux and hping3, a server script in Python (server.py), and a bot script in Python (botnet.py). This project is intended for educational use to understand how botnets work and strategies to mitigate them.

## Components

- **Dockerfile**: Creates a Docker image based on kalilinux/kali-rolling with hping3 installed.
- **botnet.py**: Bot script that connects to the Command and Control (C&C) server to execute commands.
- **server.py**: C&C server script to manage connected bots and send commands.
- **LICENSE**: Details of the license under which this project is distributed.
- **README.md**: This file, providing documentation on the project.

## Prerequisites

- Docker installed on your machine.
- Python 3 installed on your machine (to run the botnet and server scripts).

## Setup
### Building the Docker Image

To build the Docker image from the Dockerfile:

```bash
docker build -t kali-hping3 .
```

### Running the Docker Environment

To run a container from this image:

```bash
docker run -it kali-hping3
```

You will then be in a shell inside the container, with hping3 ready to be used.

### Running the C&C Server

To start the C&C server, run:

```bash
python server.py
```

Ensure the `server.py` script is configured to listen on the appropriate interface and port.

### Connecting the Bots

On each bot, run:

```bash
python botnet.py
```

Ensure `botnet.py` is configured to connect to the correct IP address and port of the C&C server.

## Usage
### C&C Server

The server will wait for connections from bots and will be able to send them arbitrary commands to execute.

### Botnet

Each bot connected to the server will execute the received commands and send the results back to the server.

## Security and Ethics

This project is solely for educational purposes and should only be used in a secure testing environment. Never use it on networks or systems without explicit authorization.

## Contribution

Your contributions are welcome. If you have suggestions for improvements or corrections, please submit a pull request or an issue on GitHub.
