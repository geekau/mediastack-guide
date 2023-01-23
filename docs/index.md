# Welcome to MediaStack.Guide

With many people owning digital media such as CDs, DVD, and Blu-ray disks, home movies, personal photos, personal music collection, its common that people want to build home media servers in order to manage and access their digital libraries from any device within their home network, their mobile devices, and even remotely when they may be away on holidays or having a lunch break at work.

This guide will help you rapidly deploy all the applications you need in a full Docker build media stack, to operate a Jellyfin, Jellyseerr, *ARR Media Library Managers (Prowlarr / Sonarr / Radarr / Lidarr / Readarr etc..) and Tdarr Automated Media Transcoding.

## Features

- Host your media stack using Docker on any Operating System or NAS Device (Windows / Linux / Synology)
- Rapidly deploy full media stack with Docker Compose files in matter of minutes
- Stream your full media library to any media device on your home network
- Full network encryption for all services connecting via the Internet (VPN and Zero Trust)
- Dedicated *ARR (starr) media library managers for your movies, tv shows, anime, music, comics, and books
- Access all of your media stack applications from the Internet with Nginx Reverse Proxy
- Internet access to your full media library using your own DDNS or DNS address
- Internet access secured by Cloudflare Zero Trust Network Access and Multifactor Authentication

## Security

This guide provides two different security models to cater for your privacy choice:

- Fully secured configuration - where all Internet connections are fully encrypted end-to-end, and
- Partially secured configuration - where only the Internet connections for Usenet / Torrents clients and Meta-Data servers are encrypted.

The external / outbound VPN connection is established using the Gluetun VPN docker container, if the VPN connection fails / drops, or is stopped for any reason, then all outbound traffic is completely restricted until the VPN connection is re-established.

You can also access your home media server from the Internet as the guide will walk you through the configuration needed to establish a Nginx reverse proxy, secured by Cloudflare's Zero Trust Network Access framework, digital SSL certificates, with integrated Multifactor Authentication (MFA) for anyone connecting from the Internet.

!!! note "Note: Remote access from the Internet requires a valid domain name"

    In order to connect to your home network using the Nginx reverse proxy and Cloudflare zero trust infrastructure, you will need a domain name, either one you register and pay for yourself, or you can register with many of the free DDNS providers available on the Internet.

    The domain name is required in order for free SSL certificates to be installed on your external connection, using Let's Encrypt or ZeroSSL certificate providers.




This guide will cover all the steps needed to initially install and configure a secure docker hosted media environment, with all the applications needed to download torrents and Usenet content which you have a right to use in your media library, and allow you to stream the media via a simple web browser, and even stream the media to your Smart TV / Apple TV apps around the house.

## Disclaimer





, and has been thoroughly tested on Linux, Windows and Synology NAS servers


With many people owning CDs, DVD, and Blu-ray disks, there is demand to make people's media content more transferrable in their home media systems, so it can be viewed on their personal devices. People also want to be able to put their own home movies / photos onto their media servers, so it too can be freely shared between their devices.

!!! warning "Warning: Piracy Notice"

    This guide is not about, nor promotes, the illegal piracy of digital media content from their respected / licensed owners.

    This guide assumes no responsibility for users who may access or download digital media content, which they do not have legal rights.
