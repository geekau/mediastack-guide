# Authelia - Authentication and Authorisation Server

Authelia is an open-source Authentication and Authorization (AA) Server and portal fulfilling the identity and access management (IAM) role of information security in providing multi-factor authentication and single sign-on (SSO) for your applications via a web portal. We will integrate it into the SWAG Nginx Reverse Proxy to manage remote secure access into your home media stack network.

---

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




## Activate Authelia Integration in SWAG Container

How to set up users, passwords and groups in Authelia
[https://www.authelia.com/reference/guides/passwords/](https://www.authelia.com/reference/guides/passwords/)


[https://www.authelia.com/integration/prologue/get-started/](https://www.authelia.com/integration/prologue/get-started/)


```
sudo vi $FOLDER_FOR_CONFIGS/swag/nginx/authelia-server.conf
sudo vi $FOLDER_FOR_CONFIGS/swag/nginx/authelia-location.conf

sudo vi $FOLDER_FOR_CONFIGS/swag/nginx/site-confs/default.conf
include /config/nginx/authelia-server.conf;

sudo cp $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/authelia-server.conf.sample   $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/authelia-server.conf
sudo cp $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/authelia-location.conf.sample $FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs/authelia-location.conf
```

