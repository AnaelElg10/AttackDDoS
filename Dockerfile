FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install -y hping3 && rm -rf /var/lib/apt/lists/*

WORKDIR AttackDDoS

COPY server.py && botnet.py

CMD ["python3", "server.py", "botnet.py"]
