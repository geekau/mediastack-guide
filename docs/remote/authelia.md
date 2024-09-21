# Authelia  

Authelia is an open-source authentication and authorisation (AA) server and portal fulfilling the identity and access management (IAM) role of information security in providing multi-factor authentication and single sign-on (SSO) for your applications via a web portal. It acts as a companion for common reverse proxies, and we will integrate it into the SWAG Nginx Reverse Proxy to manage secure remote access into your home MediaStack network.  

We will link Authelia with DUO Security, so anyone logging into your home MediaStack, will be authenticated with username / password, and MFA Push Notification to their mobile phone application.  

!!! Info "Additional Application Information - External Links"  
    - Application Website: &nbsp; &nbsp; &nbsp;[https://www.authelia.com/](https://www.authelia.com/)  
    - Docker Information: &nbsp; &nbsp; &nbsp; [https://hub.docker.com/r/authelia/authelia](https://hub.docker.com/r/authelia/authelia)  

---

</br>

## User Database  

When we set up DUO Security in the Admin portal, would have created several users, and sent them an enrollment email from inside the portal.  

We now need to create a "User Database" in Authelia, so it knows which usernames / passwords to use, in the first round of authentication.  

We need to add each username, as it is written in DUO Admin portal.  

<figure markdown>  
  ![DUO Security - User Accounts in Portal](assets/duo-portal-users.png){ width="300" }  
  <figcaption>DUO Security - User Accounts in Portal</figcaption>  
</figure>  


Add users into Authelia `users_database.yml` file.  

``` bash  
cd FOLDER_FOR_DATA/authelia  
vi users_database.yml  
```  

Add the following into the `users_database.yml` file in the authelia configuration folder, you can update their `displayname` and `email` fields as needed.  

``` yaml  
users:  
  jane:  
    displayname: Jane Doe  
    password: $argon2id$v=19$m=65536,t=3,p=4$/yxpBgUJVmRvq0mMIsFUaQ$pGtxdCaI3qkeVGoU+BGSb0pY1SHDxKkclRK5UINfISQ  
    email: jane.doe@example.com  
    groups: []  
  john:  
    displayname: John Doe  
    password: $argon2id$v=19$m=65536,t=3,p=4$/yxpBgUJVmRvq0mMIsFUaQ$pGtxdCaI3qkeVGoU+BGSb0pY1SHDxKkclRK5UINfISQ  
    email: john.doe@example.com  
    groups: []  
```

</br>

## Generating Secure Passwords  

The Authelia Docker image, as well as being an AA server, also has powerful commands / hash algorithms in order to generate secure passwords and encryption strings.  

So if we want to set john with a password of `MediaStackForever`, you would type the following command:  

``` bash
sudo docker run authelia/authelia authelia crypto hash generate argon2 --password MediaStackForever  
```

This will produce the following Digest hash:

```  
Digest: $argon2id$v=19$m=65536,t=3,p=4$GqcdgEzg6VEstG63xLC8EQ$QfA7ttd/9l6WmIvZKm5Z8x+cqGBygHjz/I8brZpiDsg
```

Therefore, the password string for Jane's account would be changed to suit the following. The password is still `MediaStackForever`, it is just converted to a Digest hash so people can't read it if they have access to the `users_database.yml` file.

``` yaml  
users:  
  jane:  
    displayname: Jane Doe  
    password: $argon2id$v=19$m=65536,t=3,p=4$GqcdgEzg6VEstG63xLC8EQ$QfA7ttd/9l6WmIvZKm5Z8x+cqGBygHjz/I8brZpiDsg  
    email: jane.doe@example.com  
    groups: []  
```

The Authelia Docker image, can also be used to generate long random passwords, which will be needed in the main configuration file below, they can be generated with the following command:

``` bash
sudo docker run --rm authelia/authelia authelia crypto hash generate --random  
```

The output will be a long "Random Passowrd", and the "Digest" hash of the randomly generated password:

```
Random Password: Lk1rrDRSJjvaZeONRbDvhSL3ObWZnLJWYrFZszTM8l9nptJLt3rjZL84jhYTcHmzJv8bjxiv  
Digest: $argon2id$v=19$m=65536,t=3,p=4$3LNeSdMd8bhnvYkd3v!YhS5ZjQk0qxPait/iagR9PLzfkUHzi6PrYO^0S68Kp6RSiU  
```

For further help in Authelia Docker commands, type the following:

``` bash
sudo docker run --rm authelia/authelia authelia crypto hash generate --help  
```

</br>

## Authelia Configuration File

First, we will make a copy of the original configuration.yml file, as we are going to replace all of the settings:

``` bash
cd FOLDER_FOR_DATA/authelia
cp configuration.yml configuration.yml.original
```

We will now replace the contents of the Authelia `configuration.yml` will the settings below.

``` bash
cd FOLDER_FOR_DATA/authelia
vi configuration.yml
```

Copy and paste the entire "Authelia Configuration" below, into the Authelia `configuration.yml` file.

``` yaml
###############################################################################
##                           Authelia Configuration                          ##
###############################################################################

server:
  address: tcp://:9091/authelia
  asset_path: /config/assets
  disable_healthcheck: false
  buffers:
    read: 8192
    write: 8192

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
  hostname: api-0535f56e.duosecurity.com
  integration_key: D9JJNEKXY8675GB2S76F
  secret_key: CAffh785efv654vconei5fr7gvTFGJhbUg58htd3
  enable_self_enrollment: false

identity_validation:
  reset_password:
    jwt_lifespan: 5 minutes
    jwt_algorithm: HS256
    jwt_secret: 9WCRufdGU036x1YK6EnVfsqq6stWa7IviITINYsuWICL4wSdQkPIBo7GhqNtHHynnRY3juj6F1bOGsghOavBGKJkEwAWjSoD
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
    max_length: 128
    require_uppercase: true
    require_lowercase: true
    require_number: true
    require_special: true
#  zxcvbn:
#    enabled: true
#    min_score: 3

access_control:
  default_policy: deny
  rules:
    - domain:
      - "auth.example.com"
      policy: bypass
    - domain:
      - "*.example.com"
      policy: two_factor

session:
  name: authelia_session
  secret: LBRbU9cEAAoR0SjtQf3QHUCbNWeMPiJfMLIO5rHW13HqDYNYgXTwhEqm0DfzSjAvI1fKljkOBUeV95HuFdKqcOjfaE0W7yFW
  same_site: strict
  inactivity: 5m
  expiration: 1h
  remember_me: 1M
  cookies:
    - domain: example.com
      authelia_url: https://auth.example.com
      default_redirection_url: https://example.com
      same_site: strict
      inactivity: 5 minutes
      expiration: 1 hour
      remember_me: 1 month

regulation:
  max_retries: 5
  find_time: 5 minutes
  ban_time: 15 minutes

storage:
  encryption_key: u02IiIfGlhS0y5YnAfaDaYqMxaFPqc0ajwBvqxTlflXvX65FSoeEXzgs8o64lKD5OnVl3w9H7PbW88z9aGOCfZlZvdMT4glK
  local:
    path: /config/db.sqlite3

notifier:
  disable_startup_check: false
  filesystem:
    filename: /config/notifications.txt
#  smtp:
#    address: "smtp://localhost:587"
#    timeout: "5 seconds"
#    username: "username"
#    password: "password"
#    sender: "Authelia <admin@example.com>"
#    identifier: localhost
#    subject: "[Authelia] {title}"
#    startup_check_address: "test@authelia.com"
#    disable_require_tls: false
#    disable_html_emails: false
#    tls:
#      server_name: smtp
#      skip_verify: false
#      minimum_version: TLS1.2
#      maximum_version: TLS1.3
```

## Customise Your Settings

Now that you have copied the working configuration above into your own Authelia configuration.yml file, you will need to customise it slightly to your needs:

1. Replace all domains (example.com), with your own domain name - (there are 7 entries).

2. Update DUO Security API connection details.

``` YAML
duo_api:
  disable: false
  hostname: api-0535f56e.duosecurity.com                  # <-- Copy from DUO Security Admin Portal
  integration_key: D9JJNEKXY8675GB2S76F                   # <-- Copy from DUO Security Admin Portal
  secret_key: CAffh785efv654vconei5fr7gvTFGJhbUg58htd3    # <-- Copy from DUO Security Admin Portal
```

3. Generate new secret values to protect your Authelia instance.

``` bash
sudo docker run --rm authelia/authelia authelia crypto rand --length 96
```

 - **jwt_secret**: Protects the integrity of JWT tokens, ensuring session tokens are secure and valid.
 - **session secret**: Encrypts session data stored in cookies, preventing tampering or session hijacking.
 - **encryption_key**: Encrypts sensitive data stored in the database, ensuring it remains safe even if the storage backend is compromised.


4. Update the Authelia Password Policy if needed, refer to: [https://www.authelia.com/configuration/security/password-policy/](https://www.authelia.com/configuration/security/password-policy/){:target="_blank"}

5. Update the SMTP settings so Authelia users can follow the "forgot password" process, and be sent password reset links to their configured email address.

```
  smtp:
    address: "smtp://smtp:587"      # <-- Configured for local SMTP Docker Container - see docker-compose.env config file
    timeout: "5 seconds"
    username: "username"            # <-- If using SMTP Docker - username / password must match in docker-compose.env config
    password: "password"            # <-- If using SMTP Docker - username / password must match in docker-compose.env config
```

Additional info: [https://www.authelia.com/configuration/notifications/smtp/](https://www.authelia.com/configuration/notifications/smtp/){:target="_blank"}

6. Redeploy Authelia with new configuration settings:

```
sudo docker container stop authelia
sudo docker container rm authelia
sudo docker compose --file docker-compose-authelia.yaml --env-file docker-compose.env up -d  
```
</br>

## SWAG and Authelia

As SWAG is a NGINX proxy with curated configurations, integration of Authelia with SWAG is very easy and you only need to enabled two includes.

Enable the auth.subdomain.conf for Authelia:

```
cd FOLDER_FOR_CONFIGS/swag/nginx/proxy-confs
vi authelia.subdomain.conf.sample
```

Find the line which says `server_name` and change `authelia.*`  to `auth.*` as shown below.

```
 server_name authelia.*;     <-- Change this line
 server_name auth.*;         <-- To this line
```

At this stage, Authelia is now fully configured, however we still need to enable some of the SWAG Nignx Reverse Proxy servers to use Authelia, however we will do this in the next section, to ensure correct workflow.

CAN THIS BE DELETED BELOW... ???



```
NOTHING TO DO TO HERE....

cd $FOLDER_FOR_CONFIGS/swag/nginx/site-confs
vi default.conf
include /config/nginx/authelia-server.conf;


cp authelia-server.conf.sample   authelia-server.conf
cp authelia-location.conf.sample authelia-location.conf

```



How to set up users, passwords and groups in Authelia  

[https://www.authelia.com/reference/guides/passwords/](https://www.authelia.com/reference/guides/passwords/){:target="_blank"}


[https://www.authelia.com/integration/prologue/get-started/](https://www.authelia.com/integration/prologue/get-started/){:target="_blank"}





