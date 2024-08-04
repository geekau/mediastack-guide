# SWAG - Secure Web Application Gateway

## Delete This Section...

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


## What is SWAG



duo_api:
  hostname: api-somenumber.duosecurity.com
  integration_key: SOMESECRETKEY
  secret_key: somelongersecretkey

## Register a DNS / DDNS Address


## Register DUO Security

![alt text](image.png)

## User accounts

sudo docker run authelia/authelia:latest authelia crypto hash generate argon2 --password strong_password_to_hash
Digest: $argon2id$v=19$m=65536,t=3,p=4$aFa+b8r/LFJt9JGb7yiXdw$0ChnAzTQtwNHUTn6fICRJNcbljta/WwNgF29iLENNEM

vi /mediastackdata/authelia/users_database.yml
users:
  john:
    displayname: John Doe
    password: $argon2id$v=19$m=65536,t=3,p=4$/yxpBgUJVmRvq0mMIsFUaQ$pGtxdCaI3qkeVGoU+BGSb0pY1SHDxKkclRK5UINfISQ
    email: john@example.com
    groups: []
  jane:
    displayname: Jane Doe
    password: $argon2id$v=19$m=65536,t=3,p=4$/yxpBgUJVmRvq0mMIsFUaQ$pGtxdCaI3qkeVGoU+BGSb0pY1SHDxKkclRK5UINfISQ
    email: jane@example.com
    groups: []



cp /mediastackdata/authelia/configuration.yml /mediastackdata/authelia/configuration.yml.original



![alt text](image-1.png)

##


##
