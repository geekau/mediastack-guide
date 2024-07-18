# DDNS-Updater - Keep Dynamic IP / DNS Mappings Updated

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




## Configuring DDNS-Updater for Reverse Proxy

Reference: [https://hub.docker.com/r/qmcgaw/ddns-updater](https://hub.docker.com/r/qmcgaw/ddns-updater)

If you have a Dynamic IP address, you will need a way to keep your Dynamic IP Address insync with your registered domain name. The DNS-Updater container supports MANY DDNS service providers, however we need to use Cloudflare as part of the Authelia zero trust framework for our multifacture authentication, so it makes sense to use Cloudflare to also host your domain and update it with DDNS-Updater. Head over to Cloudflare and register a free account: [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)

Once you have registered a free account with Cloudflare, you can transfer your existing domain to Cloudflare with "Domain Registration" --> "Transfer Domains", or you can purchase a new domain inside Cloudflare with "Domain Registration" --> "Purchase Domains".

If you don't want to pay for a domain and want to use a free DDNS domain, then check out the DDNS-Updater documenation and follow the DDNS set up for your preferred option.

Configure the DDNS-Updater by editing the "config.json" file with the details and credentials for your DDNS provider.

```
sudo vi FOLDER_FOR_CONFIGS/ddns-updater/config.json

{
  "settings": [
    {
      "provider": "cloudflare",
      "zone_identifier": "zone id",
      "domain": "your-domain-name.com",
      "host": "@",
      "ttl": 600,
      "token": "yourtoken",
      "ip_version": "ipv4"
    }
  ]
}
```

Restart the DDNS-Updater container, then check the status at: [http://localhost:6500](http://localhost:6500)

