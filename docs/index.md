# Welcome to MediaStack.Guide

With many people owning digital media such as CDs, DVD, and Blu-ray disks, home movies, personal photos, personal music collection, its common that people want to build home media servers in order to manage and access their digital libraries from any device within their home network, their mobile devices, and even remotely when they may be away on holidays or having a lunch break at work.

This guide will help you rapidly deploy all the applications you need in a full Docker build media stack, to operate a Jellyfin, Jellyseerr, *ARR Media Library Managers (Prowlarr / Sonarr / Radarr / Lidarr / Readarr etc..) and Tdarr Automated Media Transcoding.

## Why MediaStack.Guide

Building a good home media stack is not an easy task for people who aren't computer savy. Reasearching / picking the right applications for each role you need can be a frustrating activity if you don't know how each of the applications work, and worse, if you need to link them together to build a full home media solution.

While there are many good technical sites on the Internet which discuss how to configure some of the applications, these take time to set up and configure each of the applications one-by-one, before moving on to a different website to configure the next application - there really aren't many sites dedicated to covering a "complete setup" of all the applications needed, and covering the configuration steps for all of the applications so they all work together.

By following MediaStack.Guide, you can essentially have all of the applications downloaded and installed in less than 10 minutes using our customised Docker Compose files, then work through our detailed configuration guides to link all of the applications together, without needing a great technical understanding.

Our approach is "quick and simple" for greater user understanding.

> Download and install times depends on the speed of your Internet link.

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

MediaStack.Guide focuses heavily on privacy for individuals and provides two different security models to cater for your privacy choice:

- Fully secured configuration - where all Internet connections are fully encrypted end-to-end, and
- Partially secured configuration - where only the Internet connections for Usenet / Torrents clients and Meta-Data servers are encrypted.

The external / outbound VPN connection is established using the Gluetun VPN docker container, if the VPN connection fails / drops, or is stopped for any reason, then all outbound traffic is completely restricted until the VPN connection is re-established.

You can also access your home media server from the Internet as the guide will walk you through the configuration needed to establish a Nginx reverse proxy, secured by Cloudflare's Zero Trust Network Access framework, digital SSL certificates, with integrated Multifactor Authentication (MFA) for anyone connecting from the Internet.

!!! note "Note: Remote access from the Internet requires a valid domain name"

    In order to connect to your home network using the Nginx reverse proxy and Cloudflare zero trust infrastructure, you will need a domain name, either one you register and pay for yourself, or you can register with many of the free DDNS providers available on the Internet.

    The domain name is required in order for free SSL certificates to be installed on your external connection, using Let's Encrypt or ZeroSSL certificate providers.

## Disclaimer

### Warranties

MediaStack.Guide pulls together over 20 different open source applications, in order to provide the best components for your home based media stack. While the applications chosen for MediaStack.Guide are all excellent products, they are open source and many of them are developed by volunteers / contributors, and don't come with any warranties or consumer protection, additionally, these applications have been containerised into Docker images so they are easier to download, configure and deploy.

While we have taken great care and time to test all of these applications so they work together to provide the best media guide we can for people to follow, the information on this website is for general informational purposes only. MediaStack.Guide makes no representation or warranty, express or implied. Your use of the site is solely at your own risk. We will provide links to websites and support forums for the applications we discuss throughout this guide, so any expert help outside of the scope of this website can be followed to the application developers.

### Piracy Notice

The intent of MediaStack.Guide is to guide you through the steps needed to setup and configure a home media stack, so you can host your own digital media (movies / picture / music / literature), or other digital media where you have rights to host and view that media. MediaStack.Guide also provides steps on how to access and download digital media from the Internet, where you may need to restore missing / corrupted copies of digital media you have legal rights to do, or replace it with better qualities (resolution / sound).

While you are able to purchase various copies of licensed / copyright digital media and store these in your home media libraries, your legal obligations and right to download, store and view digital media is between you and the owner of the digital media. Your downloading and use of licensed digital media is solely at your own risk.

!!! warning "Warning: Piracy Notice"

    This guide is not about, nor promotes, the illegal piracy of digital media content from their respected / licensed owners.

    This guide assumes no responsibility for users who may access or download digital media content, which they do not have legal rights.
