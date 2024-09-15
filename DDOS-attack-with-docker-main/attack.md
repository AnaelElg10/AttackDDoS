# DDoS Attack Simulation Guide

## Introduction

A Distributed Denial of Service (DDoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic. DDoS attacks achieve effectiveness by utilizing multiple compromised computer systems as sources of attack traffic. Exploited machines can include computers and other networked resources such as IoT devices.


## Command Line Options

# source 
https://www.malekal.com/exemples-utilisation-commande-hping3/
https://github.com/malwaredllc/byob
https://github.com/epsylon/ufonet

```
ping @IP -t -l 65500

hping3 -V -c 100000 -d 100000 -S -p 80 --flood --rand-source @IP
hping3 -1 -p 8080 --flood @IP

- `-c`: Number of packets
- `-d`: Packet size in bytes
- `-S`: Enable SYN attack
- `-p`: Port
- `--flood`: Enable SYN flood attack

## Protection Against DDoS Attacks

To protect against these attacks, you can either block the ICMP protocol or use a cloud service that acts as an intermediary between the client and the server.

## ACK Flood DDoS Attack

### How Does an ACK Flood Attack Work?

ACK flood attacks target devices that must process every packet they receive, such as firewalls and servers. Load balancers, routers, and switches are generally not affected by these attacks.

Legitimate and illegitimate ACK packets look essentially the same, making it difficult to stop ACK floods without using a Content Delivery Network (CDN) to filter out unnecessary ACK packets. Although they appear similar, the packets used in an ACK flood DDoS attack do not contain the main part of a data packet, also known as the payload. To appear legitimate, they only need to include the ACK flag in the TCP header.

ACK floods are Layer 4 (transport layer) DDoS attacks. Learn more about Layer 4 and the OSI model.

### How Does a SYN ACK Flood Attack Work?

A SYN ACK flood DDoS attack is slightly different from an ACK attack, although the basic idea is the same: overwhelm the target with too many packets.

In a typical TCP three-way handshake, the second step is the SYN ACK packet. Usually, a server sends this SYN ACK packet in response to a SYN packet from a client device. In a SYN ACK flood DDoS attack, the attacker floods the target with SYN ACK packets. These packets are not part of any three-way handshake; their sole purpose is to disrupt the target's normal operations.

An attacker can also use SYN packets in a SYN flood DDoS attack.

### How Does Cloudflare Mitigate ACK Flood Attacks?

Cloudflare's CDN routes all traffic to and from a client's origin server. The CDN does not forward any ACK packets that are not associated with an open TCP connection, ensuring that malicious ACK traffic does not reach the origin server. Cloudflare's extensive network of data centers can absorb DDoS attacks of almost any size, rendering ACK floods largely ineffective.

Cloudflare Magic Transit and Cloudflare Spectrum also stop these types of DDoS attacks. Magic Transit proxies Layer 3 traffic, and Spectrum proxies Layer 4 traffic, as opposed to Layer 7 traffic like the CDN. Both products automatically detect attack patterns and block malicious traffic.

Learn more about other types of DDoS attacks.

## HTTP Flood DDoS Attack

### How Does an HTTP Flood Attack Work?

HTTP flood attacks target web servers by sending a large number of HTTP requests, overwhelming the server's ability to respond. This can lead to slow performance or complete downtime for the targeted website.

### Mitigation Strategies

To mitigate HTTP flood attacks, you can use rate limiting, web application firewalls (WAFs), and CDNs to filter and manage incoming traffic.

## Conclusion

This guide provides an overview of various DDoS attack types and their mitigation strategies. Always ensure you have proper security measures in place to protect your infrastructure from such attacks.