# DNS Resolution

## Introduction

Internet-based DNS resolution is a fundamental process that translates human-friendly domain names into machine-readable IP addresses. This process is essential because while humans find it easier to remember domain names, computers and other networked devices rely on IP addresses to communicate. When you enter a URL into your web browser, a DNS query is initiated to find the corresponding IP address. This query travels through various DNS servers until the IP address is returned to your browser, allowing it to connect to the desired web server; in the case of the MediaStack Project, we want to remotely connect to our home network and Docker applications.

Most home-based Internet connections use dynamic IP addresses, which can change periodically. To manage this, DNS and Dynamic DNS (DDNS) services are covered in the MediaStack Project. Traditional DNS maps a consistent domain name to a static IP address, while DDNS services automatically update the domain name when your Internet facing IP address changes on your home network. This makes it easier to access your home network remotely without needing to remember the changing IP addresses.

Using a domain name allows you to conveniently access your home network, with DNS resolution ensuring that your domain name correctly points to your home network IP address. We will use the SWAG Docker container to provide seamless reverse proxy operations, where a reverse proxy server acts as an intermediary for requests from clients seeking resources from servers within your network.

Furthermore, DNS resolution can integrate with security measures to ensure that remote connections are routed through secure channels and authenticated before accessing your home network. This adds a layer of security, protecting your network from unauthorized access. In summary, DNS and DDNS options simplify the connection process, accommodate dynamic IP changes, and facilitate the setup of reverse proxies, thereby enhancing both the functionality and security of your remote connections.

!!! note

    While a free DDNS domain name will allow you to remotely access your home network from the Internet, is it highly recommended you register your own proper DNS domain name, as you will have more control over the DNS entries, and can add more protection by routing your network traffic through additionally security services like Cloudflare Tunnels.... You can't do this with a free DDNS domain name, as you have no control how the DDNS is resolved.

    As DDNS is a free services, it does attract Internet users for nerfarious activities, and some DDNS names are blocked in web browsers, and corporate Gateway / Firewall services.
    

```
Project Name: {{ COMPOSE_PROJECT_NAME }}  
- Project Name: `<span class="COMPOSE_PROJECT_NAME">default_value</span>`
- Docker Subnet: `<span class="DOCKER_SUBNET">default_value</span>`
- Docker Gateway: `<span class="DOCKER_GATEWAY">default_value</span>`
- Local Subnet: `<span class="LOCAL_SUBNET">default_value</span>`
- Local Docker IP: `<span class="LOCAL_DOCKER_IP">default_value</span>`
```

</br>

| <center>Type</center> | <center>Name</center> | <center>Target</center> |  
|---------------|-------------|----------------|  
| A Record &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | example.com &nbsp; &nbsp; &nbsp; &nbsp; | Your External IP Address &nbsp; |  
| CNAME Record    | jellyfin | example.com |  
| CNAME Record    | plex | example.com |  
| CNAME Record    | jellyseerr | example.com |  
| CNAME Record    | radarr | example.com |  
| CNAME Record    | sonar | example.com |  
| CNAME Record    | reader | example.com |  
| CNAME Record    | bazarr | example.com |  
| CNAME Record    | lidarr | example.com |  

FOLDER_FOR_CONFIGS  
FOLDER_FOR_MEDIA

</br>

## DDNS Configuration

If you have a dynamic IP address from your ISP... i.e. the IP address changes often, then you will most likely want to register a free domain from one of the many Dynamic DNS providers.

As we will use **DDNS Updater** to update our DDNS record whenever our IP address changes, then it is recommended to use one of the DDNS providers supported by the DDNS Updater docker application:

List of Supported DDNS Providers: [https://github.com/qdm12/ddns-updater#configuration](https://github.com/qdm12/ddns-updater#configuration)




## Heading Three






## Activate Heimdall Integration in SWAG Container
```
sudo cp $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/heimdall.subfolder.conf.sample $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/heimdall.subfolder.conf
sudo vi $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/heimdall.subfolder.conf

#Enable this line
include /config/nginx/authelia-location.conf;

sudo vi $FOLDER_FOR_CONFIGS/swag/nginx/site-confs/default.conf

```


# THESE ARE ITEMS FOR NOTES ONLY AT THIS POINT

```
Text Editor - Open: 

heimdall.subfolder.conf.sample
sudo vi $FOLDER_FOR_CONFIGS/swag/www/index.html
sudo vi $FOLDER_FOR_CONFIGS/swag/nginx/site-confs/default.conf
sudo vi $FOLDER_FOR_CONFIGS/swag/nginx/site-confs/default.conf
sudo -E vi $FOLDER_FOR_CONFIGS/authelia/
sudo -E vi $FOLDER_FOR_CONFIGS/authelia/

```


[https://www.linuxserver.io/blog/zero-trust-hosting-and-reverse-proxy-via-cloudflare-swag-and-authelia](https://www.linuxserver.io/blog/zero-trust-hosting-and-reverse-proxy-via-cloudflare-swag-and-authelia)

Test...

