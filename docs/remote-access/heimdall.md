# Heimdall - Website Link Manager

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

