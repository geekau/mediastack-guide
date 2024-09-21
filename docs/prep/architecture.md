# Networking Architecture

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Describe the network architecture of the two different Docker network deployment options, the secure VPN connection, and how to change docker containers between the direct connection mode and VPN container mode.

Also describe the incoming / remote network connectivity from the Internet (using a DNS entry), to access Jellyfin and all other Media-Stack portals via the Reverse Proxy.

External / Remote connectivity to be discussed lightly here, and broken down into more detail in the "Configure Remote Access" menu stack

## Full VPN Network Security

A fully encrypted VPN network architecture routes all network traffic from various containers through the Gluetun Docker container before it reaches the internet. This setup ensures that all data packets are encrypted, providing robust privacy and security. The primary benefit of this approach is the comprehensive protection of data, safeguarding against eavesdropping, and maintaining user privacy.  

However, this heightened security comes with trade-offs. Encrypting and decrypting all traffic can lead to increased latency and reduced network speeds. This can particularly impact applications requiring high bandwidth or low latency, such as media streaming or real-time communication tools. Nonetheless, for users prioritizing privacy and security over speed, this setup is ideal.  

``` mermaid
graph TD
    subgraph Docker Host Network Stack
        Jellyfin ---- Gluetun
        Plex --- Gluetun
        Jellyseerr ---- Gluetun
        Prowlarr --- Gluetun
        Radarr ---- Gluetun
        Readarr --- Gluetun
        Sonarr ---- Gluetun
        Mylar --- Gluetun
        Whisparr ---- Gluetun
        Bazarr --- Gluetun
        Lidarr ---- Gluetun
        Tdarr --- Gluetun
        Unpackerr ---- Gluetun
        SABnzbd --- Gluetun
        NIC[Host Network Interface]
        qBittorrent ---- Gluetun
    end
    Gluetun ==>| Secure VPN | NIC
    NIC ==>| Secure VPN | Gateway[<center>Home</p>Gateway</center>]
    Gateway ==>|Secure VPN |VPN{<center>VPN Server</p>Anchor Point</center>}
    
    style Bazarr stroke:green,stroke-width:2px
    style Lidarr stroke:green,stroke-width:2px
    style Mylar stroke:green,stroke-width:2px
    style Prowlarr stroke:green,stroke-width:2px
    style Radarr stroke:green,stroke-width:2px
    style Readarr stroke:green,stroke-width:2px
    style Sonarr stroke:green,stroke-width:2px
    style Tdarr stroke:green,stroke-width:2px
    style Unpackerr stroke:green,stroke-width:2px
    style Whisparr stroke:green,stroke-width:2px
    style Jellyfin stroke:green,stroke-width:2px
    style Plex stroke:green,stroke-width:2px
    style qBittorrent stroke:green,stroke-width:2px
    style Jellyseerr stroke:green,stroke-width:2px
    style SABnzbd stroke:green,stroke-width:2px
    style Gluetun stroke:green,stroke-width:2px
    style NIC stroke:green,stroke-width:2px
    style Gateway stroke:green,stroke-width:2px
    style VPN stroke:green,stroke-width:2px
```

<br><br><br>

## Minimal VPN Network Security

In a minimal encrypted VPN network, only specific containers, like those handling BitTorrent traffic, route their network traffic through the Gluetun container to the VPN server. This approach ensures that sensitive or high-risk activities are encrypted, while other containers operate with unencrypted traffic. The advantage here is that it maintains higher network performance for most applications, avoiding the latency and bandwidth reductions associated with full encryption.  

However, this comes at the cost of leaving some network traffic potentially exposed to interception or monitoring. This setup is suitable for users who require high performance for certain applications but still want to protect specific, sensitive activities.  

``` mermaid
graph TD
    subgraph Docker Host Network Stack
        Jellyfin -..-> NIC
        Plex -.-> NIC
        Jellyseerr -..-> NIC
        Prowlarr -.-> NIC
        Radarr -..-> NIC
        Readarr -.-> NIC
        Sonarr -..-> NIC
        Mylar -.-> NIC
        Whisparr -..-> NIC
        Bazarr -.-> NIC
        Lidarr -..-> NIC
        Tdarr -.-> NIC
        Unpackerr -..-> NIC
        SABnzbd -.-> NIC
        NIC[Host Network Interface]
        qBittorrent --- Gluetun
    end
    Gluetun ==>| Secure VPN | NIC
    NIC -.->| Insecure Data | Gateway[<center>Home</p>Gateway</center>]
    NIC ==>| Secure VPN | Gateway[<center>Home</p>Gateway</center>]
    Gateway -.->| Insecure Data |Internet{<center>General</p>Internet</center>}
    Gateway ==>|Secure VPN |VPN{<center>VPN Server</p>Anchor Point</center>}
    
    style Bazarr stroke:orange,stroke-width:2px
    style Lidarr stroke:orange,stroke-width:2px
    style Mylar stroke:orange,stroke-width:2px
    style Prowlarr stroke:orange,stroke-width:2px
    style Radarr stroke:orange,stroke-width:2px
    style Readarr stroke:orange,stroke-width:2px
    style Sonarr stroke:orange,stroke-width:2px
    style Tdarr stroke:orange,stroke-width:2px
    style Unpackerr stroke:orange,stroke-width:2px
    style Whisparr stroke:orange,stroke-width:2px
    style Jellyfin stroke:orange,stroke-width:2px
    style Plex stroke:orange,stroke-width:2px
    style qBittorrent stroke:green,stroke-width:2px
    style Jellyseerr stroke:orange,stroke-width:2px
    style SABnzbd stroke:orange,stroke-width:2px
    style Gluetun stroke:green,stroke-width:2px
    style Internet stroke:orange,stroke-width:2px
    style VPN stroke:green,stroke-width:2px
```

<br><br><br>

## Secure Remote Network Access  

All of the Docker configurations are set up to allow you to remotely access your Docker applications while you're away from home. The network diagram illustrates a secure remote access architecture utilising a combination of Docker applications, SWAG (Secure Web Application Gateway), Authelia, Heimdal, and Cloudflare Zero Trust. This setup ensures that only authenticated and trusted users that you grant permissions to, can access the internal Docker-based services over the Internet.

At the core of the network is the Docker infrastructure, operating on the subnet 172.28.10.0/24 (adjustable). Within this network, multiple applications are hosted in Docker containers. Once a remote user is successfully authenticated, they are granted access to Heimdall, which serves as a landing page portal provding users with easy access to the other Docker applications. To securely manage and route incoming connections, SWAG functions as both a reverse proxy and web server, and uses a valid SSL Digital Certificate to encrypt the remote HTTPS session. It intercepts requests from remote users and forwards them to the appropriate internal services.  

Cloudflare plays a crucial role in enhancing security. It acts as the initial point of contact for remote Internet users, offering a robust proxy service that filters and manages traffic before it reaches SWAG. Cloudflare Zero Trust provides an additional layer of security by enforcing authentication and access policies. This means that any request must pass through Cloudflare's security checks, ensuring only authorised traffic reaches the internal Docker network.  

Authelia, integrated with both SWAG and Cloudflare Zero Trust, handles user authentication. It provides two-factor authentication (2FA) and single sign-on (SSO) capabilities, ensuring that users must verify their identities before gaining access. This integration ensures that even if an attacker bypasses the Cloudflare security checks, they still face robust authentication challenges from Authelia.  

By combining these technologies, the setup ensures a secure, scalable, and manageable remote access solution. The network protects against unauthorized access while providing legitimate users with seamless access to the necessary applications, thus balancing security with user convenience.  

</br>
<center>

``` mermaid  
graph
    subgraph DockerNet[<center>Docker Networking - 172.28.10.0/24</center>]
        Authelia
        SMTP[SMTP</br>Relay]
        SWAG
        NIC[Docker Host</br>Network Bridge]
        Homepage
        Docker{Docker</br>Applications}
        Apps{Internal Network</br>Access}
    end
    subgraph Internet[<center>Internet Zone</center>]
        Remote[ Remote</br>Internet Users ]
        Tunnel{<center>Cloudflare</br>Tunnel</center>}
        DUO{<center>DUO Security</br>2FA</center>}
    end
    Gateway[Home Gateway]
    Remote <-.->   | Push</br>Notifications             | DUO
    Authelia -.->  | Password</br>Resets                | SMTP
    Homepage ==>   | Remote</br>Access                  | Docker
    Homepage ==>   | Remote</br>Access                  | Apps
    Gateway -.->   | Password</br>Resets                | Remote
    Tunnel ==>     | Remote Access</br>HTTPS to SWAG    | Gateway
    Remote ==>     | Remote Access</br>HTTPS to SWAG    | Tunnel
    Gateway ==>    | Remote</br>Access                  | NIC
    NIC ==>        | Remote</br>Access                  | SWAG
    Authelia <-.-> | Auth                               | NIC
    Authelia <-.-> | Auth                               | SWAG
    NIC <-.->      | Auth                               | Gateway
    Gateway <-.->  | Auth                               | DUO
    SWAG ==>       | Authenticated Users                | Homepage
    SMTP -.->      | Password</br>Resets                | NIC
    NIC -.->       | Password</br>Resets                | Gateway

    style Authelia stroke:green ,stroke-width:2px
    style SWAG stroke:green     ,stroke-width:2px
    style SMTP stroke:green     ,stroke-width:2px
    style Homepage stroke:green ,stroke-width:2px
    style Remote stroke:green   ,stroke-width:2px
    style Gateway stroke:green  ,stroke-width:2px
    style DUO stroke:green      ,stroke-width:2px
    style Tunnel stroke:green   ,stroke-width:2px
    style Apps stroke:green     ,stroke-width:2px
    style Docker stroke:green   ,stroke-width:2px
    style NIC stroke:green      ,stroke-width:2px

    linkStyle 0 stroke:#FFA500  ,stroke-width:2px
    linkStyle 1 stroke:#0088FF  ,stroke-width:2px
    linkStyle 4 stroke:#0088FF  ,stroke-width:2px
    linkStyle 9 stroke:#FFA500  ,stroke-width:2px
    linkStyle 10 stroke:#FFA500 ,stroke-width:2px
    linkStyle 11 stroke:#FFA500 ,stroke-width:2px
    linkStyle 12 stroke:#FFA500 ,stroke-width:2px
    linkStyle 14 stroke:#0088FF ,stroke-width:2px
    linkStyle 15 stroke:#0088FF ,stroke-width:2px
```  

</center>
<br><br>
