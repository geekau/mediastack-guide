# MediaStack Applications

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.

List of all Media-Stack applications used in this guide and their roles

## Heading Two





## Heading Three



## Application Portals:

 Portal | Application | Function
-------- | -------- | --------
[https://localhost:9443](https://localhost:9443)|Portainer|GUI Interface for Docker Management
[http://localhost:6767](http://localhost:6767)|Bazarr|Subtitle Manager for Radarr / Sonarr
[http://localhost:8191](http://localhost:8191)|FlareSolverr|Provides status message only
[http://localhost:8096](http://localhost:8096)|Jellyfin|(Media Player)
[http://localhost:5055](http://localhost:5055)|Jellyseerr|(Content Request Management)
[http://localhost:8686](http://localhost:8686)|Lidarr|(Library Manager - Music)
[http://localhost:8090](http://localhost:8090)|Mylar3|(Library Manager - Comics)
[http://localhost:9696](http://localhost:9696)|Prowlarr|(Index and Search Management)
[http://localhost:7878](http://localhost:7878)|Radarr|(Library Manager - Movies)
[http://localhost:8787](http://localhost:8787)|Readarr|(Library Manager - Books)
[http://localhost:8100](http://localhost:8100)|SABnzbd|(Library Manager - TV Shows)
[http://localhost:8989](http://localhost:8989)|Sonarr|(Library Manager - TV Shows)
[http://localhost:8265](http://localhost:8265)|Tdarr|Automatic Audio/Video Library Transcoding
[http://localhost:6969](http://localhost:6969)|Whisparr|(Library Manager - XXX)
[http://localhost:8200](http://localhost:8200)|qBittorrent|(Downloader - Torrents)
[http://localhost:5080](http://localhost:5080)|SWAG - Nginx|Web Server for Reverse Proxy HTTP
[http://localhost:5433](http://localhost:5433)|SWAG - Nginx|Web Server for Reverse Proxy HTTPS
[http://localhost:6500](http://localhost:6500)|DDNS-Updater|Web Portal - DDNS-Updater Status

**Default qBittorrent Portal Access:**     Username: **admin**     Password: **adminadmin**



  
**PART 2 - Docker Media Applications and Their Roles / Functions**  
  
This guide will focus on Jellyfin and the \*ARR media libraries in order to manage your media libraries and make your media accessible across your home network and devices.  


  
The table below shows the docker applications which will be installed, their default port numbers and what function they perform:  
  
  

Portal URL:​

Application:​

Role / Function:​

No Portal -->

Gluetun

VPN Client - Supports extensive Internet providers and protocols

[http://localhost:6789](http://localhost:6789)

NZBGet

Download client - Used to download NZB from Usenet groups

[http://localhost:9091](http://localhost:9091)

Transmission

Download Client - Used to download torrent files

[http://localhost:8096](http://localhost:8096)

Jellyfin

Media Library / Player - Organise, manage, and share digital media files to networked devices

[http://localhost:5055](http://localhost:5055)

Jellyseerr

Request management and media discovery tool (Overseerr Fork for Jellyfin)

[http://localhost:9696](http://localhost:9696)

Prowlarr

Index and Search Management for "\*ARR" applications below

[http://localhost:8686](http://localhost:8686)

Lidarr

Library Manager for Music content management

[http://localhost:8090](http://localhost:8090)

Mylar3

Library Manager for Comic content management

[http://localhost:7878](http://localhost:7878)

Radarr

Library Manager for Movie content management

[http://localhost:8787](http://localhost:8787)

Readarr

Library Manager for Book / Epub content management

[http://localhost:8989](http://localhost:8989)

Sonarr

Library Manager for TV Show / Series / Anime content management

[http://localhost:6969](http://localhost:6969)

Whisparr  
(see note)

Library Manager for Adult movie content management

  
**NOTE:** This guide also includes Whisparr which is a Library Manager for movies from the Adult entertainment industry. It is included as its part of the \*ARR product family, we don't judge what people do / don't watch, but we do urge the use of access controls / security on adult content, so minors and other groups are not exposed to this content if they are not of legal age under your regional laws.  
  
In order to deploy the docker-compose file and host the applications, Docker must be installed as a prerequisite on your Linux, Windows, or Synology hosting environment. The following guide will help set up your Docker environment, and help manage the applications once they are installed:  
  
[Tutorial - Ultimate Starter - Docker, Portainer, Portainer Agents, and Auto-Updating Everything with Watchtower](https://www.synoforum.com/resources/ultimate-starter-docker-portainer-portainer-agents-and-auto-updating-everything-with-watchtower.183/)  
  
**NOTE:** This guide assumes you have installed Docker, and Portainer for managing your docker environment.  


