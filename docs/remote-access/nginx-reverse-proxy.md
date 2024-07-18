# Nginx - Reverse Proxy


## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



"Configure Remote Access" Menu and Pages will document steps in order to configure all the applications to allow remote access into your home network / Jellyfin server from the Internet.

These pages to document the integrated of:

- Cloudflare for Domain Name Registration and Hosting (Your Own Internet Address)
- DDNS-Updater to Update DNS Records Hosted on Cloudflare DNS, or Public DDNS Provider
- Authelia for User Authentication / Authorisation - AA Server
- Cloudflare Zero Trust Network Access
- Nginx Reverse Proxy Server (SWAG)
- Automate SSL Install with Let's Encrypt / ZeroSSL Certificate Authorities
- Heimdall (Link Manager) - Configure Links for All Internet Web Services.... Jellyfin / *ARR Apps etc..


## Heading Two

## Heading Three







## For Reverse Proxy into your network (from the Internet):

 Portal | Application | Function
-------- | -------- | --------
[http://your-domain-name.com](http://your-domain-name.com)|SWAG|Reverse Proxy
[https://your-domain-name.com](http://your-domain-name.com)|SWAG|Reverse Proxy

The SWAG container provides Nginx Reverse Proxy and MFA running on ports **5080/HTTP** and **5443/HTTPS**, so they don't conflict with other services running on the Docker host computer. To access your Reverse Proxy from the Internet, you need to set up your gateway / router, to allow Internet ports **80** and **443** into your network, but redirect them to the Docker host IP Address on ports **5080** and **5443** respectively.

Port **80** will be accessible on the Internet and redirected to the Reverse Proxy on port **5080**, however it will redirect to HTTPS protocol using port **443** via the Internet, which will also be redirected to the Reverse Proxy on port **5443**. Reverse Proxy port numbers can be changed as required in the ENV file if required.

The SWAG container requires a resolvable domain name, and will automatically install SSL certificates using either Let's Encrypt or Zero SSL providers, and is also able to provide Multi-Factor Authentication (MFA), to provide strong security for your Internet connected applications.

 - [https://www.linuxserver.io/blog/zero-trust-hosting-and-reverse-proxy-via-cloudflare-swag-and-authelia](https://www.linuxserver.io/blog/zero-trust-hosting-and-reverse-proxy-via-cloudflare-swag-and-authelia)





# THESE ARE ITEMS FOR NOTES ONLY AT THIS POINT



cat /home/geekau/docker/swag/nginx/proxy-confs/sabnzbd.subfolder.conf.sample

/home/geekau/docker/swag/nginx/proxy-confs/sabnzbd.subfolder.conf.sample




$FOLDER_FOR_CONFIGS/swag/
$FOLDER_FOR_CONFIGS/swag/dns-conf/
$FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/
$FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sabnzbd.subfolder.conf.sample
$FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sonarr.subfolder.conf.sample
$FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sonarr.subdomain.conf.sample
$FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sonarr.subfolder.conf.sample
$FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sonarr.subdomain.conf.sample
$FOLDER_FOR_CONFIGS/swag/nginx/
$FOLDER_FOR_CONFIGS/swag/nginx/
$FOLDER_FOR_CONFIGS/swag/nginx/proxy.conf
$FOLDER_FOR_CONFIGS/swag/nginx/nginx.conf



sudo -E cp $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sabnzbd.subfolder.conf.sample     $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sabnzbd.subfolder.conf
sudo -E cp $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sonarr.subfolder.conf.sample      $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/sonarr.subfolder.conf
ls -la $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/*.conf
ls -la $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/

mv /mnt/user/appdata/swag/nginx/proxy-confs/sonarr.subdomain.conf.sample /mnt/user/appdata/swag/nginx/proxy-confs/sonarr.subdomain.conf



audiobookshelf.subdomain.conf.sample
audiobookshelf.subfolder.conf.sample
authelia.subdomain.conf.sample
bazarr.subdomain.conf.sample
bazarr.subfolder.conf.sample
filebot.subdomain.conf.sample
filebot.subfolder.conf.sample
jellyfin.subdomain.conf.sample
jellyfin.subfolder.conf.sample
jellyseerr.subdomain.conf.sample
lidarr.subdomain.conf.sample
lidarr.subfolder.conf.sample
mylar.subdomain.conf.sample
mylar.subfolder.conf.sample
portainer.subdomain.conf.sample
portainer.subfolder.conf.sample
prowlarr.subdomain.conf.sample
prowlarr.subfolder.conf.sample
qbittorrent.subdomain.conf.sample
qbittorrent.subfolder.conf.sample
radarr.subdomain.conf.sample
radarr.subfolder.conf.sample
readarr.subdomain.conf.sample
readarr.subfolder.conf.sample
sabnzbd.subdomain.conf.sample
sabnzbd.subfolder.conf.sample
sonarr.subdomain.conf.sample
sonarr.subfolder.conf.sample
tdarr.subdomain.conf.sample



