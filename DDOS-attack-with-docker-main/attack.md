## Ping (ICMP) flood or Ping of death

source : https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack/

- Une simple DDOS avec le ping en augmentant la taille du paquet, un paquet
- ping par defaut sa taille est de 32 bytes. Nous on l'augmente à 65500 bytes
- Cette attaque consomme la bande passante
- On peut utiliser un botnet pour lancer cette attack ou bien sur le même 
- ordinateur en lançant plusieurs terminal.

# source 
https://www.malekal.com/exemples-utilisation-commande-hping3/
https://github.com/malwaredllc/byob
https://github.com/epsylon/ufonet

```
ping @IP -t -l 65500

hping3 -V -c 100000 -d 100000 -S -p 80 --flood --rand-source @IP
hping3 -1 -p 8080 --flood @IP

-c = nombre de paquet
-d = taille de paquet en byte
-S = pour activer le sync attack
-p = port
--flood = pour activer le syck flood attack

```

- Pour se proteger de cette attaque il y a deux méthodes, soit en bloquant 
- le protocole ICMP ou bien un cloud qui se positionne entre le client et le server.

## ACK flood DDoS attack

Comment fonctionne une attaque par inondation ACK ?

Les attaques par inondation ACK ciblent les appareils qui doivent traiter chaque paquet qu'ils reçoivent. Les pare-feu et les serveurs sont les cibles les plus probables d'une inondation d'ACK. Les équilibreurs de charge, les routeurs et les commutateurs ne sont pas sensibles à ces attaques.

Les paquets ACK légitimes et illégitimes se ressemblent essentiellement, ce qui rend difficile l'arrêt des inondations ACK sans utiliser un réseau de diffusion de contenu (CDN) pour filtrer les paquets ACK inutiles. Bien qu'ils se ressemblent, les paquets utilisés dans une attaque DDoS ACK ne contiennent pas la partie principale d'un paquet de données, également appelé charge utile. Pour paraître légitimes, il leur suffit d'inclure l'indicateur ACK dans l'en-tête TCP.

Les inondations ACK sont des attaques DDoS de couche 4 (couche de transport). Découvrez la couche 4 et le modèle OSI.
Comment fonctionne une attaque par inondation SYN ACK ?

Une attaque DDoS SYN ACK Flood est légèrement différente d’une attaque ACK, bien que l’idée de base soit toujours la même : submerger la cible avec trop de paquets.

Rappelez-vous comment fonctionne une négociation à trois voies TCP : la deuxième étape de la négociation est le paquet SYN ACK. Habituellement, un serveur envoie ce paquet SYN ACK en réponse à un paquet SYN provenant d'un périphérique client. Lors d'une attaque DDoS SYN ACK, l'attaquant inonde la cible de paquets SYN ACK. Ces paquets ne font pas du tout partie d’une négociation à trois ; leur seul objectif est de perturber les opérations normales de la cible.

Il est également possible pour un attaquant d'utiliser des paquets SYN dans une attaque DDoS par inondation SYN.
Comment Cloudflare arrête-t-il les attaques DDoS par inondation ACK ?

Le CDN Cloudflare transmet tout le trafic vers et depuis le serveur d'origine d'un client Cloudflare. Le CDN ne transmet aucun paquet ACK non associé à une connexion TCP ouverte. Cela garantit que le trafic ACK malveillant n’atteint pas le serveur d’origine. Le réseau de centres de données Cloudflare est suffisamment vaste pour absorber les attaques DDoS de presque toutes les tailles, de sorte que les inondations ACK ont également peu ou pas d'effet sur Cloudflare.

Cloudflare Magic Transit et Cloudflare Spectrum stoppent également ce type d'attaques DDoS. Magic Transit proxy le trafic de couche 3 et Spectrum le trafic de couche 4, au lieu du trafic de couche 7 comme le CDN. Les deux produits bloquent les inondations ACK en détectant automatiquement les modèles d'attaque et en bloquant le trafic d'attaque.

Découvrez d’autres types d’attaques DDoS.



## HTTP flood DDoS attack

Les attaques HTTP Flood sont un type d’attaque DDoS de « couche 7 ». La couche 7 est la couche d'application du modèle OSI et fait référence aux protocoles Internet tels que HTTP. HTTP est la base des requêtes Internet basées sur un navigateur et est couramment utilisé pour charger des pages Web ou pour envoyer le contenu de formulaires sur Internet. L'atténuation des attaques au niveau de la couche application est particulièrement complexe, car le trafic malveillant est difficile à distinguer du trafic normal.

# Il existe deux types d'attaques par inondation HTTP :
 
- Attaque HTTP GET : dans cette forme d'attaque, plusieurs ordinateurs ou autres appareils sont coordonnés pour envoyer plusieurs demandes d'images, de fichiers ou d'autres actifs à partir d'un serveur ciblé. Lorsque la cible est inondée de demandes et de réponses entrantes, un déni de service se produira pour des demandes supplémentaires provenant de sources de trafic légitimes.

- Attaque HTTP POST : généralement lorsqu'un formulaire est soumis sur un site Web, le serveur doit gérer la demande entrante et transférer les données dans une couche de persistance, le plus souvent une base de données. Le processus de gestion des données du formulaire et d'exécution des commandes de base de données nécessaires est relativement intensif par rapport à la quantité de puissance de traitement et de bande passante requise pour envoyer la requête POST. Cette attaque exploite la disparité dans la consommation relative des ressources, en envoyant de nombreuses requêtes de publication directement à un serveur ciblé jusqu'à ce que sa capacité soit saturée et qu'un déni de service se produise.

# Comment atténuer une inondation HTTP ?

Comme mentionné précédemment, l’atténuation des attaques de couche 7 est complexe et souvent multiforme. Une méthode consiste à implémenter un défi à la machine requérante afin de tester s'il s'agit ou non d'un bot, un peu à la manière d'un test captcha couramment utilisé lors de la création d'un compte en ligne. En donnant une exigence telle qu'un défi informatique JavaScript, de nombreuses attaques peuvent être atténuées.

D'autres moyens d'arrêter les inondations HTTP incluent l'utilisation d'un pare-feu d'application Web (WAF), la gestion d'une base de données de réputation IP afin de suivre et de bloquer sélectivement le trafic malveillant, ainsi que l'analyse à la volée par des ingénieurs. Avoir un avantage d'échelle avec plus de 20 millions de propriétés Internet permet à Cloudflare d'analyser le trafic provenant de diverses sources et d'atténuer les attaques potentielles avec des règles WAF rapidement mises à jour et d'autres stratégies d'atténuation pour éliminer le trafic DDoS de la couche application.

Il existe 4 étapes pour atténuer une attaque DDoS à l’aide d’un fournisseur basé sur le cloud :

- Détection : afin de stopper une attaque distribuée, un site Web doit être capable de distinguer une attaque d'un volume élevé de trafic normal. Si le lancement d'un produit ou toute autre annonce fait en sorte qu'un site Web est inondé de nouveaux visiteurs légitimes, la dernière chose que le site souhaite faire est de les limiter ou de les empêcher de consulter le contenu du site Web. La réputation IP, les modèles d’attaque courants et les données antérieures contribuent à une détection appropriée.

- Réponse : au cours de cette étape, le réseau de protection DDoS répond à une menace identifiée entrante en supprimant intelligemment le trafic de robots malveillants et en absorbant le reste du trafic. En utilisant les règles de page WAF pour les attaques de la couche application (L7), ou un autre processus de filtrage pour gérer les attaques de niveau inférieur (L3/L4) telles que Memcached ou l'amplification NTP, un réseau est en mesure d'atténuer les tentatives de perturbation.
    
- Routage : en acheminant intelligemment le trafic, une solution efficace d'atténuation des attaques DDoS divisera le trafic restant en morceaux gérables empêchant tout déni de service.

- Adaptation - Un bon réseau analyse le trafic à la recherche de modèles tels que la répétition de blocs IP incriminés, des attaques particulières provenant de certains pays ou des protocoles particuliers utilisés de manière inappropriée. En s'adaptant aux modèles d'attaque, un service de protection peut se renforcer contre de futures attaques.

## Choisir un service d'atténuation DDoS

Les solutions traditionnelles d’atténuation des attaques DDoS impliquaient l’achat d’équipements qui resteraient sur place et filtreraient le trafic entrant. Cette approche implique l’achat et la maintenance d’équipements coûteux, et s’appuie également sur un réseau capable d’absorber une attaque. Si une attaque DDoS est suffisamment importante, elle peut détruire l'infrastructure réseau en amont, empêchant toute solution sur site d'être efficace. Lors de l’achat d’un service d’atténuation DDoS basé sur le cloud, certaines caractéristiques doivent être évaluées.

- Évolutivité : une solution efficace doit être capable de s'adapter aux besoins d'une entreprise en croissance et de répondre à l'ampleur croissante des attaques DDoS. Des attaques supérieures à 2 térabits par seconde (Tbps) ont eu lieu, et rien n’indique que la tendance de la taille du trafic d’attaque soit à la baisse. Le réseau de Cloudflare est capable de gérer des attaques DDoS considérablement plus importantes que jamais.
    
- Flexibilité : être capable de créer des politiques et des modèles ad hoc permet à une propriété Web de s'adapter aux menaces entrantes en temps réel. La possibilité de mettre en œuvre des règles de page et de renseigner ces modifications sur l'ensemble du réseau est une fonctionnalité essentielle pour maintenir un site en ligne pendant une attaque.

- Fiabilité : tout comme une ceinture de sécurité, la protection DDoS est quelque chose dont vous n'avez besoin que lorsque vous en avez besoin, mais le moment venu, il vaut mieux qu'elle soit fonctionnelle. La fiabilité d’une solution DDoS est essentielle au succès de toute stratégie de protection. Assurez-vous que le service bénéficie de taux de disponibilité élevés et que les ingénieurs en fiabilité du site travaillent 24 heures sur 24 pour maintenir le réseau en ligne et identifier les nouvelles menaces. La redondance, le basculement et un vaste réseau de centres de données devraient être au cœur de la stratégie de la plateforme.

- Taille du réseau : les attaques DDoS suivent des modèles qui se produisent sur Internet à mesure que des protocoles et des vecteurs d'attaque particuliers évoluent au fil du temps. Disposer d'un vaste réseau avec un transfert de données étendu permet à un fournisseur d'atténuation DDoS d'analyser et de répondre aux attaques rapidement et efficacement, les arrêtant souvent avant qu'elles ne se produisent. Le réseau de Cloudflare exécute des requêtes Internet pour des millions de sites Web, créant ainsi un avantage dans l'analyse des données provenant du trafic d'attaques dans le monde entier.

## What is a Web Application Firewall (WAF)?

source : https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/

Qu'est-ce qu'un pare-feu d'applications Web (WAF) ?

Un WAF ou un pare-feu d'application Web aide à protéger les applications Web en filtrant et en surveillant le trafic HTTP entre une application Web et Internet. Il protège généralement les applications Web contre les attaques telles que la contrefaçon intersite, le cross-site-scripting (XSS), l'inclusion de fichiers et l'injection SQL, entre autres.
Un WAF est une défense de couche 7 du protocole (dans le modèle OSI) et n'est pas conçu pour se défendre contre tous les types d'attaques. Cette méthode d’atténuation des attaques fait généralement partie d’une suite d’outils qui, ensemble, créent une défense globale contre une gamme de vecteurs d’attaque.

En déployant un WAF devant une application web, un bouclier est placé entre l'application web et Internet. Alors qu'un serveur proxy protège l'identité d'un ordinateur client en utilisant un intermédiaire, un WAF est un type de proxy inverse, protégeant le serveur de toute exposition en faisant passer les clients par le WAF avant d'atteindre le serveur.

Un WAF fonctionne selon un ensemble de règles souvent appelées politiques. Ces politiques visent à se protéger contre les vulnérabilités de l'application en filtrant le trafic malveillant. La valeur d'un WAF vient en partie de la rapidité et de la facilité avec lesquelles les modifications de politique peuvent être mises en œuvre, permettant une réponse plus rapide aux différents vecteurs d'attaque ; lors d'une attaque DDoS, la limitation du débit peut être rapidement mise en œuvre en modifiant les politiques WAF.
DDOS Comment fonctionne un WAF



## Common DDoS Attack Tools

Many DDoS attack tools such as HTTP Unbearable Load King (HULK), Slowloris, PyLoris, DAVOSET, GodenEye, Open Web Application Security Project (OWASP) HTTP Post, Low Orbit ION Cannon (LOIC), High Orbit ION Cannon (HOIC), Xoic, Tor’s Hammer, DDoSSIM (DDoS Simulator) and RUDY (R-U-Dead-Yet) are freely available.


