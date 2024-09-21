# SWAG - Secure Web Application Gateway




!!! Info "Additional Application Information - External Links"  
    - Application Website: &nbsp; &nbsp; &nbsp; [https://www.authelia.com/](https://www.authelia.com/)  
    - Docker Information: &nbsp; &nbsp; &nbsp; [https://hub.docker.com/r/authelia/authelia](https://hub.docker.com/r/authelia/authelia)  
---

</br>

## SWAG Will Not Start

!!! Warning "SWAG WILL NOT START"  
    This is a notice to advise that SWAG WILL NOT START until all of the following items have been completed:  

    - All domain applications have been configured in `FOLDER_FOR_DATA/swag/proxy-conf` directory.  
    - Your DNS Provider has been configured in the `FOLDER_FOR_DATA/swag/dns-conf` directory.  
    - DNS is correctly pointing your domain name to your Internet IP address.  
    - Certbot has successfully installed a valid SSL digital certificate.  
    - Port forwarding has been enabled on your home router / gateway.  

    This is a safety / security feature and is built by design to function this way.  
---

</br>

## SWAG Configuration

The following settings in the `docker-compose.env` file are passed through the SWAG when the container is deployed.

If any of the settings below are changed after SWAG has been deployed in Docker, then the running container must be removed, and SWAG redeployed again so the new settings are picked up.

``` conf
# NGINX WEB PORTS (Adjustable)
REVERSE_PROXY_PORT_HTTP=80
REVERSE_PROXY_PORT_HTTPS=443

# SWAG REVERSE PROXY SETTINGS:
DOMAINNAME=your-domain-name-goes-here.com
SUBDOMAINS=wildcard
VALIDATION=dns
DNSPLUGIN=cloudflare
CERTPROVIDER=letsencrypt
PROPAGATION=
DUCKDNSTOKEN=
EMAIL=
ONLY_SUBDOMAINS=false
EXTRA_DOMAINS=
STAGING=false

# Cloudflare Tunnel for SWAG
CF_ZONE_ID=6ad4f87ae98717e76c221k75a1e0b6f2
CF_ACCOUNT_ID=67a350ae5a9756k803e9c607eec9f4j9
CF_API_TOKEN=1u90r5BPQ7o5tAzqr1gZalHC9VlaZa45dUG56GIi
CF_TUNNEL_NAME=
CF_TUNNEL_TOKEN=
```

## Check DNS Configuration

In order for SWAG to get a valid SSL digital certificate from Let's Encrypt or ZeroSSL, the domain name you registered in Cloudflare / Authelia, needs to also be configured in SWAG.

``` bash
cd FOLDER_FOR_DATA/swag/dns-confs
vi cloudflare.ini
```

Add you Cloudflare API Token to the cloudflare.ini, and comment the other two lines cloudflare lines

``` yaml
#dns_cloudflare_email = cloudflare@example.com                            # Add "#" at start of line
#dns_cloudflare_api_key = 0123456789abcdef0123456789abcdef01234567        # Add "#" at start of line
dns_cloudflare_api_token = YourCloudflareToken                            # Enable this line with API Token
```

> NOTE: May need to check your respective DNS provider to ensure Certbot is configured and can register an SSL digital certificate.



## Enable Domain Configurations

``` bash
cd FOLDER_FOR_DATA/swag/nginx/proxy-confs

cp authelia.subdomain.conf.sample      authelia.subdomain.conf
cp bazarr.subdomain.conf.sample        bazarr.subdomain.conf
cp ddns-updater.subdomain.conf.sample  ddns-updater.subdomain.conf
cp filebot.subdomain.conf.sample       filebot.subdomain.conf
cp flaresolverr.subdomain.conf.sample  flaresolverr.subdomain.conf
cp gluetun.subdomain.conf.sample       gluetun.subdomain.conf
cp heimdall.subdomain.conf.sample      heimdall.subdomain.conf
cp homarr.subdomain.conf.sample        homarr.subdomain.conf
cp homepage.subdomain.conf.sample      homepage.subdomain.conf
cp jellyfin.subdomain.conf.sample      jellyfin.subdomain.conf
cp jellyseerr.subdomain.conf.sample    jellyseerr.subdomain.conf
cp lidarr.subdomain.conf.sample        lidarr.subdomain.conf
cp mylar.subdomain.conf.sample         mylar.subdomain.conf
cp plex.subdomain.conf.sample          plex.subdomain.conf
cp portainer.subdomain.conf.sample     portainer.subdomain.conf
cp prowlarr.subdomain.conf.sample      prowlarr.subdomain.conf
cp qbittorrent.subdomain.conf.sample   qbittorrent.subdomain.conf
cp radarr.subdomain.conf.sample        radarr.subdomain.conf
cp readarr.subdomain.conf.sample       readarr.subdomain.conf
cp sabnzbd.subdomain.conf.sample       sabnzbd.subdomain.conf
cp sonarr.subdomain.conf.sample        sonarr.subdomain.conf
cp tdarr.subdomain.conf.sample         tdarr.subdomain.conf
cp whisparr.subdomain.conf.sample      whisparr.subdomain.conf
```

In all of the new `.conf` files we copied, we need to enable the Authelia

```
#include /config/nginx/authelia-location.conf;     <-- Change these lines
#include /config/nginx/authelia-server.conf;       <-- Change these lines
```

```
include /config/nginx/authelia-location.conf;     <-- To these lines
include /config/nginx/authelia-server.conf;       <-- To these lines
```

## Active Authelia in all Nginx configurations
However, that's a lot of files we need to edit manually, so run the following script to automatically remove the `#` from the authelia include line.

```
cd FOLDER_FOR_DATA/swag/nginx/proxy-confs
sed -i 's/^\(\s*\)#\(\s*include \/config\/nginx\/authelia.*\)/\1\2/' *.conf
```

## Output all lines which are edited correctly in all of the Nginx configurations

```
grep -Hn '^\s*include /config/nginx/authelia' *.conf
```




```
sudo docker container stop swag
sudo docker container rm swag
sudo docker-compose --file docker-compose-swag.yaml --env-file docker-compose.env up -d
```


```
sudo docker logs swag
```




```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/example.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/example.com/privkey.pem
This certificate expires on 2024-12-19.
These files will be updated when the certificate renews.
NEXT STEPS:
- The certificate will need to be renewed before it expires. Certbot can automatically renew the certificate in the background, but you may need to take steps to enable that functionality. See https://certbot.org/renewal-setup for instructions.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
If you like Certbot, please consider supporting our work by:
 * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
 * Donating to EFF:                    https://eff.org/donate-le
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
New certificate generated; starting nginx
The cert does not expire within the next day. Letting the cron script handle the renewal attempts overnight (2:08am).
[custom-init] No custom files found, skipping...
[ls.io-init] done.
Server ready
```




## Certbot


## cloudflare Zone ID stuff




```
$FOLDER_FOR_CONFIGS/swag/
$FOLDER_FOR_CONFIGS/swag/dns-conf/
$FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/
$FOLDER_FOR_CONFIGS/swag/nginx/
$FOLDER_FOR_CONFIGS/swag/nginx/
$FOLDER_FOR_CONFIGS/swag/nginx/proxy.conf
$FOLDER_FOR_CONFIGS/swag/nginx/nginx.conf
```

```
cd /$FOLDER_FOR_DATA/swag/nginx
```

```
cd /$FOLDER_FOR_DATA/swag/nginx/site-confs
```


## Port Forwarding From Internet



sudo netstat -tulpn -4 | grep -E '80|443'

sudo netstat -tulpn -4 | grep -E '5080|5443'

```
username@vm1:/volume1/docker/appdata/swag/dns-conf$ sudo netstat -tulpn -4 | grep -E '5080|5443'
tcp        0      0 0.0.0.0:5443            0.0.0.0:*               LISTEN      24790/docker-proxy
tcp        0      0 0.0.0.0:5080            0.0.0.0:*               LISTEN      24819/docker-proxy
```

Static IP is a MUST when port forwarding from the Internet.

REVERSE_PROXY_PORT_HTTP=80
REVERSE_PROXY_PORT_HTTPS=443
LOCAL_DOCKER_IP=192.168.1.10




.
