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
        Mylar3 --- Gluetun
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
    style Mylar3 stroke:green,stroke-width:2px
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
        Mylar3 -.-> NIC
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
    style Mylar3 stroke:orange,stroke-width:2px
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

## Remote Network Access

## Heading