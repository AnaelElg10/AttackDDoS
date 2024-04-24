#---------------------------------------------------------------------------#
#                              Build the containers                         # 
#---------------------------------------------------------------------------#

# Build the attacker image
docker build -t attacker attack-with-slowloris
# Build the victime-nginx image
docker build -t victime-apache-server victime-apache-server
# Build the victime-nginx image
docker build -t victime-nginx-server victime-nginx-server

#---------------------------------------------------------------------------#
#                              Run the containers                           # 
#---------------------------------------------------------------------------#

# Run the container for apache server
docker run -dti --rm --name apache-server victime-apache-server 
# Run the container for nginx server
docker run -dti --rm --name nginx-server  victime-nginx-server
# Run the attacker container 
docker run -dti --rm --name attacker-DDOS attacker

#---------------------------------------------------------------------------#
#                       Get containers ip addresses                         # 
#---------------------------------------------------------------------------#

docker network inspect bridge
