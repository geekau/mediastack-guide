# Cloudflare - Domain Management

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





## Configuring SWAG HTTP / DNS
In order for the Certbot tool inside SWAG to be able to request / issue a digital SSL certificate from Let's Encrypt or ZeroSSL, you need to set up the validation type in ENV.
```
sudo vi docker-compose.env
VALIDATION=dns
DNSPLUGIN=cloudflare
```
If you're using "dns" as the validation process, select the DNS plugin that suits your environment, and make appropriate updates.

DNS plugins are located: "**FOLDER_FOR_CONFIGS/swag/dns-conf/**"

>The domain name you used in "**URL**" MUST resolve back to your Internet IP address, and your Internet Router / Firewall be set up to forward the ports **80** and **443** to your Docker host IP address, on ports **5080** and **5443** respectively.

Refer to:

- [https://docs.linuxserver.io/general/swag#cert-provider-lets-encrypt-vs-zerossl](https://docs.linuxserver.io/general/swag#cert-provider-lets-encrypt-vs-zerossl)
- [https://docs.linuxserver.io/general/swag#web-hosting-examples](https://docs.linuxserver.io/general/swag#web-hosting-examples)
- [https://docs.linuxserver.io/general/swag#reverse-proxy](https://docs.linuxserver.io/general/swag#reverse-proxy)
- [https://docs.linuxserver.io/general/swag#authorization-method](https://docs.linuxserver.io/general/swag#authorization-method)

SWAG has many different plugins available to help validate your "your-domain-name.com" / IP address, via DNS, they are located in the $FOLDER_FOR_CONFIGS/swag/dns-conf folder.
For example, to set up the Cloudflare plugin, edit the following:
```
sudo vi $FOLDER_FOR_CONFIGS/swag/dns-conf/cloudflare.ini
```
**You can then update the ENV file, delete the SWAG container and re-deploy it, to build a new container with the updated configurations.**

###Once your SWAG Server has validated "your-domain-name.com" / IP address, and installed an SSL certificate, the Nginx web server will start working.

###If you have forwarded ports 80 and 443 to the Docker host on 5080 and 5443, then you should be able to access the Nginx web server welcome page from the Internet.

You can use an online remote web browser to check if your site is accessible from the Internet. Go to [https://www.browserling.com](https://www.browserling.com) and put in your domain name to test.

>NOTE: All HTTP traffic on port 80 is automatically redirected to HTTPS on port 443, so it helps to have both ports open and redirected.












