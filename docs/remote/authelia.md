# Authelia

Authelia is an open-source authentication and authorisation (AA) server and portal fulfilling the identity and access management (IAM) role of information security in providing multi-factor authentication and single sign-on (SSO) for your applications via a web portal. It acts as a companion for common reverse proxies, and we will integrate it into the SWAG Nginx Reverse Proxy to manage secure remote access into your home MediaStack network.

!!! Info "Additional Application Information - External Links"  
    - Application Website: &nbsp; &nbsp; &nbsp;[https://www.authelia.com/](https://www.authelia.com/)  
    - Docker Information: &nbsp; &nbsp; &nbsp; [https://hub.docker.com/r/authelia/authelia](https://hub.docker.com/r/authelia/authelia)  

---

## DUO Security (2FA)

Duo Security, a Cisco company, provides multi-factor authentication (MFA) to secure access to applications and data. Duo enhances login security by requiring two or more verification methods - a password and a mobile device or hardware token. This approach protects against unauthorised access and ensures only authorised users access sensitive information. With a user-friendly interface, Duo simplifies MFA implementation across platforms, making it essential for organisations to strengthen security and protect against identity theft and data breaches.  

**Head over to DUO Security, and sign up for a free trial, which allows you to set up 10 users without paying.**

[https://duo.com](https://duo.com)


<figure markdown>
  ![DUO Security - Add User](assets/duo-add-user.png){ width="300" }
  <figcaption>DUO Security - Add User</figcaption>
</figure>



<figure markdown>
  ![DUO Security - Add User](assets/duo-api-integration.png){ width="300" }
  <figcaption>DUO Security - Add User</figcaption>
</figure>


<figure markdown>
  ![DUO Security - Add User](assets/duo-app-store.png){ width="300" }
  <figcaption>DUO Security - Add User</figcaption>
</figure>

<figure markdown>
  ![DUO Security - Add User](assets/duo-app-accounts.png){ width="300" }
  <figcaption>DUO Security - Add User</figcaption>
</figure>



## User Database





Add users into Authelia "users_database.yml" file  
```
vi /mediastackdata/authelia/users_database.yml
```


```
users:
  jane:
    displayname: Jane Doe
    password: $argon2id$v=19$m=65536,t=3,p=4$/yxpBgUJVmRvq0mMIsFUaQ$pGtxdCaI3qkeVGoU+BGSb0pY1SHDxKkclRK5UINfISQ
    email: jane@example.com
    groups: []
  john:
    displayname: John Doe
    password: $argon2id$v=19$m=65536,t=3,p=4$/yxpBgUJVmRvq0mMIsFUaQ$pGtxdCaI3qkeVGoU+BGSb0pY1SHDxKkclRK5UINfISQ
    email: john@example.com
    groups: []
```

```
sudo docker run authelia/authelia:latest authelia crypto hash generate argon2 --password strong_password_to_hash  
```

```
sudo docker run --rm authelia/authelia authelia crypto hash generate --help  
sudo docker run --rm authelia/authelia authelia crypto hash generate --random  
```
Random Password: Lk1rrDRSJjvaZeONRbDvhSL3ObWZnLJWYrFZszTM8l9nptJLt3rjZL84jhYTcHmzJv8bjxiv  
Digest: $argon2id$v=19$m=65536,t=3,p=4$3LNeSdMd8bhnvYkd3v!YhS5ZjQk0qxPait/iagR9PLzfkUHzi6PrYO^0S68Kp6RSiU  




## Configuration File



vi {{ FOLDER_FOR_DATA }}/authelia/configuration.yml

```
###############################################################################
##                           Authelia Configuration                          ##
###############################################################################

server:
  address: tcp://:9091/
  asset_path: /config/assets/
  disable_healthcheck: false
  buffers:
    read: 16384
    write: 16384

log:
  level: debug
  format: json
  file_path: /config/authelia.log

webauthn:
  disable: false
  timeout: 60 seconds
  display_name: Authelia
  user_verification: preferred

duo_api:
  disable: false
  hostname: api-03g6789e.duosecurity.com
  integration_key: D9JNH4FJ236CGHB9OLX
  secret_key: CAffh785efv654vconei5fr7gvTFGJhbUg58ht
  enable_self_enrollment: false

identity_validation:
  reset_password:
    jwt_lifespan: 5 minutes
    jwt_algorithm: HS256
    jwt_secret: Q&QVee1J5gM6XE@SyX4GVMh$Y&!apwQbi0cNWV6N59V2YXWxH2BaYc@hR1v$8RfH
  elevated_session:
    code_lifespan: 5 minutes
    elevation_lifespan: 10 minutes
    characters: 8
    require_second_factor: false
    skip_second_factor: false

authentication_backend:
  password_reset:
    disable: false
  file:
    path: /config/users_database.yml
    watch: false
    search:
      email: false
      case_insensitive: false
    password:
      algorithm: argon2
      argon2:
        variant: argon2id
        iterations: 3
        memory: 65536
        parallelism: 4
        key_length: 32
        salt_length: 16

password_policy:
  standard:
    enabled: true
    min_length: 14
    max_length: 64
    require_uppercase: true
    require_lowercase: true
    require_number: true
    require_special: true
  zxcvbn:
    enabled: true
    min_score: 3


access_control:
  default_policy: deny
  rules:
    - domain:
      - example.com
      - "*.example.com"
      policy: two_factor

session:
  name: authelia_session
  secret: SKQelztd&5QRiig!HNqY35Kw#cimuI^#8hwmXN3DxbI4QaPPDMzW9jf9&CJze%y!
  same_site: strict
  inactivity: 5m
  expiration: 1h
  remember_me: 1M
  cookies:
    - domain: example.com
      authelia_url: https://auth.example.com
      default_redirection_url: https://homepage.example.com
      same_site: strict
      inactivity: 5 minutes
      expiration: 1 hour
      remember_me: 1 month

regulation:
  max_retries: 5
  find_time: 5 minutes
  ban_time: 15 minutes

storage:
  encryption_key: uFGT&Ncg@II6zoG7EZmWNNldP3X3AMAuFfb^@P^OU!4fbfK^r6aXiXJj1lLhWF7D
  local:
    path: /config/db.sqlite3

notifier:
  disable_startup_check: false
#  filesystem:
#    filename: /config/notifications.txt
  smtp:
    address: "smtp://smtp:25"
    timeout: "5 seconds"
    username: "username"
    password: "password"
    sender: "Authelia <admin@EXAMPLE.COM>"
    identifier: localhost
    subject: "[Authelia] {title}"
    startup_check_address: "user@EXAMPLE.COM"
    disable_require_tls: false
    disable_html_emails: false
    tls:
      server_name: smtp
      skip_verify: false
      minimum_version: TLS1.2
      maximum_version: TLS1.3
```


## SWAG Integration




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









