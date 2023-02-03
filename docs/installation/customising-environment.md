# Docker Environment File

The docker applications are deployed and configured using an environment file, which ensures all variables and settings are shared consistantly across all of the applications as they are deployed.

The environment file is called `docker-compose.env`, and it is exactly the same file located in each of the folders

!!! note "File: docker-compose.env &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <-- Default Configuration File"

    ```
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ##
    ##  Docker Compose Environment Variable file for Jellyfin Media Stack
    ##
    ##  Update any of the environment variables below as required.
    ##
    ##  It is highly recommended Linux users set up a "docker"
    ##  user, so the applications can access the local filesystem
    ##  with this user's access privileges. Use PUID / PGID to map
    ##  user access between the Docker apps and local filesystem.
    ##
    ###########################################################################
    ###########################################################################
    ###########################################################################

    #Name of the project in Docker
    COMPOSE_PROJECT_NAME=media-stack

    # This is the network subnet which will be used inside the docker "media_network", change as required.
    # LOCAL_SUBNET is your home network and is needed so the VPN client allows access to your home computers.
    DOCKER_SUBNET=172.28.10.0/24
    DOCKER_GATEWAY=172.28.10.1
    LOCAL_SUBNET=10.168.1.0/24
    LOCAL_DOCKER_IP=10.168.1.10

    # Each of the "*ARR" applications have been configured so the theme can be changed to your needs.
    # Refer to Theme Park for more info / options: https://docs.theme-park.dev/theme-options/aquamarine/
    TP_THEME=nord

    # These are the folders on your local host computer / NAS running docker, they MUST exist
    # and have correct permissions for PUID and PGUI prior to running the docker-compose.
    #
    # Use the commands in the Guide to create all the sub-folders in each of these folders.

    # Host Data Folders - Will accept Linux, Windows, NAS folders
    FOLDER_FOR_CONFIGS=/home/geekau/docker
    FOLDER_FOR_MEDIA=/home/geekau/media-stack

    # File access, date and time details for the containers / applications to use.
    # Run "sudo id docker" on host computer to find PUID / PGID and update these to suit.
    PUID=1000
    PGID=1000
    UMASK=0002
    TIMEZONE=Australia/Brisbane

    # Update your own Internet VPN provide details below
    VPN_TYPE=openvpn
    VPN_SERVICE_PROVIDER=VPN provider name
    VPN_USERNAME=<username from VPN provider>
    VPN_PASSWORD=<password from VPN provider>
    SERVER_REGION=<regions supported by VPN provider>
    SERVER_CITIES=
    SERVER_HOSTNAMES=

    # Fill in this item ONLY if you're using a custom OpenVPN configuration
    # Should be inside gluetun data folder - Example: /gluetun/custom-openvpn.conf
    # You can then edit it inside the FOLDER_FOR_CONFIGS location for gluetun.
    OPENVPN_CUSTOM_CONFIG=

    # Fill in these items ONLY if you change VPN_TYPE to "wireguard"
    VPN_ENDPOINT_IP=
    VPN_ENDPOINT_PORT=
    WIREGUARD_PUBLIC_KEY=
    WIREGUARD_PRIVATE_KEY=
    WIREGUARD_PRESHARED_KEY=
    WIREGUARD_ADDRESSES=

    # These are the default ports used to access each of the application in your web browser.
    # You can safely change these if you need, but they can't conflict with other active ports.
    QBIT_PORT_TCP=6881
    QBIT_PORT_UDP=6881
    FLARESOLVERR_PORT=8191

    TDARR_SERVER_PORT=8266
    WEBUI_PORT_TDARR=8265

    WEBUI_PORT_BAZARR=6767
    WEBUI_PORT_DDNS_UPDATER=6500
    WEBUI_PORT_JELLYFIN=8096
    WEBUI_PORT_JELLYSEERR=5055
    WEBUI_PORT_LIDARR=8686
    WEBUI_PORT_MYLAR3=8090
    WEBUI_PORT_PORTAINER=9443
    WEBUI_PORT_PROWLARR=9696
    WEBUI_PORT_QBITTORRENT=8200
    WEBUI_PORT_RADARR=7878
    WEBUI_PORT_READARR=8787
    WEBUI_PORT_SONARR=8989
    WEBUI_PORT_SABNZBD=8100
    WEBUI_PORT_WHISPARR=6969

    # SWAG is configured for Reverse Proxy. Set your Internet gateway to redirect incoming ports 80 and 443
    # to the ports used below (using Docker IP Address), and they will be translated back to 80 and 443 by SWAG.
    # Change these port numbers if you have conflicting services running on the Docker host computer.

    REVERSE_PROXY_PORT_HTTP=5080
    REVERSE_PROXY_PORT_HTTPS=5443

    # SWAG REVERSE PROXY SETTINGS:
    URL=your-domain-name-goes-here.com
    SUBDOMAINS=wildcard
    VALIDATION=dns
    DNSPLUGIN=cloudflare
    CERTPROVIDER=
    PROPAGATION=
    DUCKDNSTOKEN=
    EMAIL=
    ONLY_SUBDOMAINS=false
    EXTRA_DOMAINS=
    STAGING=false
    ```



PART 3 - Configuring the Docker-Compose Environment Settings

This implementation will use a docker-compose configuration file and an accompanying environment file, containing all of the variables for the docker-compose file, so it can be customised to your individual requirements. This allows complex docker builds to be rapidly deployed over and over with relative ease, and minimal input. In fact, it is quicker and easier to delete all of the docker applications and redeploy it again, rather than trying to do any fault finding when errors occur. It is also a simply way to upgrade application versions, by deleting the entire docker stack, and redeploying again using updated images.

Download Docker Compose Media Stack - Yaml file
Download Docker Compose Media Stack - Environment file

Below are some of the planning details / settings you need to consider, which are located inside the Environment File - they should be updated to suit your needs.

Define Docker Stack and Local Network Details:

You can change the subnet / gateway of the network inside docker where these applications will be deployed, if you are not experienced with docker, then leave the subnet / gateway settings alone.

Put your internal home network details into the LOCAL_SUBNET variable, this will tell the VPN client to allow local computers on this network, they are allowed to access each of the applications inside the secure docker stack.

DOCKER_SUBNET=172.28.10.0/24
DOCKER_GATEWAY=172.28.10.1
LOCAL_SUBNET=192.168.1.0/24 <-- your local / home network subnet details here

Once the docker stack has been created and the VPN connection established, Gluetun also allows all computers on the local network, to piggy back off the VPN connection and send all web traffic from your local computer through the secure tunnel. You can change your web proxy to the IP address of your Docker host, using port 8888. A point to remember, if your Docker stack is disabled / turned off, then your web browsers will stop working until you restart the Docker host / stack, or remove the proxy setting in your web browsers.

Set up VPN Connection for Entire Docker Stack:

Its a mandatory requirement you have an active VPN connection, otherwise Gluetun will not establish a VPN tunnel, and there will be no data forwarded to the Internet for the entire docker stack.

A full list of supported VPN / Wireguard providers can be found on the Gluetun wiki on the right hand side menu: Home · qdm12/gluetun Wiki

Gluetun also supports custom VPN configurations if you have alternate VPN setups, the docker-compose file has the necessary variables if you need to set up a custom VPN connection, including Wireguard.

VPN_SERVICE_PROVIDER=VPN provider name
VPN_USERNAME=<username from VPN provider>
VPN_PASSWORD=<password from VPN provider>
SERVER_REGION=<regions supported by VPN provider>

Main Folders For Media and Docker Persistent Configurations:

This is the most important component of your media server, were data is going to be stored, and how all the different Docker applications are going to access the different media / configuration files.

When you set up folders / volumes on the host computer, you need to map them in the Docker configuration, so the applications can access the data. The docker-compose file has already set up all the correct folder mappings between the host computer and docker applications by using environment variables in the YAML file, however you will need to update the variables below so the the docker-compose build knows which folders to map.

When considering media storage, you also need to consider files are going to be downloaded by the Docker applications and moved between folders, which are actually being moved by the underlaying host computer. So you need to consider what happens when moving a 10GB file between two folders inside different Docker applications, may in fact be getting transferred to different HDDs / Filesystems / Volumes, on the host system - this can greatly slow down the performance of disk operations and docker performance.

It is highly recommended the locations you choose for the MEDIA, TORRENTS, USENET, and WATCH folders, are located on the same HDD / Volume / Partition on the local host computer. The Docker stack has been carefully planned, and as long as these host folders are using these principles, then the Docker application will take advantage of Atomic Moves (instant) inside the containers.

FOLDER_FOR_DOCKER_DATA= # Folder to store persistent configuration settings for all the docker applications
FOLDER_FOR_MEDIA= # Folder where root of media library exists
FOLDER_FOR_TORRENTS= # Folder where all torrent files will be downloaded (Transmission)
FOLDER_FOR_USENET= # Folder where all NZB Usenet files will be downloaded (NZBGet)
FOLDER_FOR_WATCH= # Folder to place NZB and Torrent files for manual downloading

The following table provides examples on how the folders located on the Host computer, will be mapped to the folders inside the Docker containers.


Environment Variable:​
Synology Example:​
Linux Example:​
Windows Example:​
Docker Path:​
FOLDER_FOR_DOCKER_DATA	/volume1/docker	/opt/docker	D:\Docker	Differs by container
FOLDER_FOR_MEDIA	/volume1/media	/opt/media	D:\Media	/data/media
FOLDER_FOR_TORRENTS	/volume1/data/torrents	/opt/torrents	D:\Torrents	/data/torrents
FOLDER_FOR_USENET	/volume1/data/usenet	/opt/usenet	D:\Usenet	/data/usenet
FOLDER_FOR_WATCH	/volume1/data/watch	/opt/watch	D:\Watch	/data/watch

You need to define your own folders for Synology / Linux / Windows, however the locations you define in the variables, will be mapped to the docker application as per the Docker Path column.

NOTE: It is recommended the folders you use on the host computer, remain empty until completing the entire guide and setting up all the applications. So if you plan to use folder names that current have media, you should rename the old folders, create new ones, then copy the media into the new folders after completing this guide.






# Docker Media Stack
>You can download these files easily, by going to [https://github.com/geekau/media-stack](https://github.com/geekau/media-stack) then selecting "**Code**" --> "**Download Zip**".

These Docker Compose configurations will help you rapidly deploy all the applications you need in a Docker stack, to operate a Jellyfin, Jellyseerr, Torrent, Usenet, \*ARR Media Library Managers, Reverse Proxy, MFA Authenticated Access, and Tdarr Automated Media Transcoding enabled media stack, and has been thoroughly testing on Linux, Windows and Synology NAS servers.


## 2 - Edit the "docker-compose.env" file, and update variables to suit your environment.


```
DOCKER_SUBNET=172.28.10.0/24
DOCKER_GATEWAY=172.28.10.1
LOCAL_SUBNET=10.168.1.0/24
LOCAL_DOCKER_IP=10.168.1.111
```


### Docker Host Folders Locations:
Add the folder locations to the ENV file, where your docker configurations and media / downloads will be stored:
>Folders need to exist before running "docker-compose" commands. Valid choices are Linux, Windows or NAS folder naming conventions.
```
FOLDER_FOR_CONFIGS=/home/geekau/docker
FOLDER_FOR_MEDIA=/home/geekau/media-stack
```

### At Linux / Synology terminal, use the "id" command to identify user ID and group ID.
```
sudo id geekau
uid=1000(geekau) gid=1000(geekau) groups=1000(geekau)
```
Update the ENV file with these details:
```
PUID=1000     <-- Update this value from "id" command
PGID=1000     <-- Update this value from "id" command
TIMEZONE=Australia/Brisbane
```
Update your local Timezone using this list: [List of Timezone Database - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

### Update your VPN Service Provider details for Gluetun to create VPN tunnel.
Add your VPN service provider details.
>If you don't have a VPN service provider configured, Gluetun will not establish a secure VPN tunnel, and will not allow any network traffic out onto the Internet.
```
VPN_SERVICE_PROVIDER=VPN provider name
VPN_USERNAME=<username from VPN provider>
VPN_PASSWORD=<password from VPN provider>
SERVER_REGION=<regions supported by VPN provider>
```
== **All containers are initally configured to sit behind the VPN connection for security / privacy. If you want the containers to have direct Internet access, follow the steps in each of the YAML files to change the network configuration, and restart the container.** ==





**PART 3 - Configuring the Docker-Compose Environment Settings**  
  
This implementation will use a docker-compose configuration file and an accompanying environment file, containing all of the variables for the docker-compose file, so it can be customised to your individual requirements. This allows complex docker builds to be rapidly deployed over and over with relative ease, and minimal input. In fact, it is quicker and easier to delete all of the docker applications and redeploy it again, rather than trying to do any fault finding when errors occur. It is also a simply way to upgrade application versions, by deleting the entire docker stack, and redeploying again using updated images.  
  
[**Download Docker Compose Media Stack - Yaml file**](https://github.com/geekau/media-stack/blob/main/docker-compose-media-stack.yaml)  
[**Download Docker Compose Media Stack - Environment file**](https://github.com/geekau/media-stack/blob/main/docker-compose-media-stack.env)  
  
Below are some of the planning details / settings you need to consider, which are located inside the Environment File - they should be updated to suit your needs.  
  
**Define Docker Stack and Local Network Details:**  
  
You can change the subnet / gateway of the network inside docker where these applications will be deployed, if you are not experienced with docker, then leave the subnet / gateway settings alone.  
  
Put your internal home network details into the **LOCAL\_SUBNET** variable, this will tell the VPN client to allow local computers on this network, they are allowed to access each of the applications inside the secure docker stack.  
  
**DOCKER\_SUBNET**\=172.28.10.0/24  
**DOCKER\_GATEWAY**\=172.28.10.1  
**LOCAL\_SUBNET**\=192.168.1.0/24 <-- your local / home network subnet details here  
  
Once the docker stack has been created and the VPN connection established, Gluetun also allows all computers on the local network, to piggy back off the VPN connection and send all web traffic from your local computer through the secure tunnel. You can change your web proxy to the IP address of your Docker host, using port 8888. A point to remember, if your Docker stack is disabled / turned off, then your web browsers will stop working until you restart the Docker host / stack, or remove the proxy setting in your web browsers.  
  
**Set up VPN Connection for Entire Docker Stack:**  
  
Its a mandatory requirement you have an active VPN connection, otherwise Gluetun will not establish a VPN tunnel, and there will be no data forwarded to the Internet for the entire docker stack.  
  
A full list of supported VPN / Wireguard providers can be found on the Gluetun wiki on the right hand side menu: [Home · qdm12/gluetun Wiki](https://github.com/qdm12/gluetun/wiki)  
  
Gluetun also supports custom VPN configurations if you have alternate VPN setups, the docker-compose file has the necessary variables if you need to set up a custom VPN connection, including Wireguard.  
  
**VPN\_SERVICE\_PROVIDER**\=VPN provider name  
**VPN\_USERNAME**\=<username from VPN provider>  
**VPN\_PASSWORD**\=<password from VPN provider>  
**SERVER\_REGION**\=<regions supported by VPN provider>  
  
**Main Folders For Media and Docker Persistent Configurations:**  
  
This is the most important component of your media server, were data is going to be stored, and how all the different Docker applications are going to access the different media / configuration files.  
  
When you set up folders / volumes on the host computer, you need to map them in the Docker configuration, so the applications can access the data. The docker-compose file has already set up all the correct folder mappings between the host computer and docker applications by using environment variables in the YAML file, however you will need to update the variables below so the the docker-compose build knows which folders to map.  
  
When considering media storage, you also need to consider files are going to be downloaded by the Docker applications and moved between folders, which are actually being moved by the underlaying host computer. So you need to consider what happens when moving a 10GB file between two folders inside different Docker applications, may in fact be getting transferred to different HDDs / Filesystems / Volumes, on the host system - this can greatly slow down the performance of disk operations and docker performance.  
  
It is highly recommended the locations you choose for the MEDIA, TORRENTS, USENET, and WATCH folders, are located on the same HDD / Volume / Partition on the local host computer. The Docker stack has been carefully planned, and as long as these host folders are using these principles, then the Docker application will take advantage of Atomic Moves (instant) inside the containers.  
  
**FOLDER\_FOR\_DOCKER\_DATA**\= # Folder to store persistent configuration settings for all the docker applications  
**FOLDER\_FOR\_MEDIA**\= # Folder where root of media library exists  
**FOLDER\_FOR\_TORRENTS**\= # Folder where all torrent files will be downloaded (Transmission)  
**FOLDER\_FOR\_USENET**\= # Folder where all NZB Usenet files will be downloaded (NZBGet)  
**FOLDER\_FOR\_WATCH**\= # Folder to place NZB and Torrent files for manual downloading  
  
The following table provides examples on how the folders located on the Host computer, will be mapped to the folders inside the Docker containers.  
  
  

Environment Variable:​

Synology Example:​

Linux Example:​

Windows Example:​

Docker Path:​

FOLDER\_FOR\_DOCKER\_DATA

/volume1/docker

/opt/docker

D:\\Docker

Differs by container

FOLDER\_FOR\_MEDIA

/volume1/media

/opt/media

D:\\Media

/data/media

FOLDER\_FOR\_TORRENTS

/volume1/data/torrents

/opt/torrents

D:\\Torrents

/data/torrents

FOLDER\_FOR\_USENET

/volume1/data/usenet

/opt/usenet

D:\\Usenet

/data/usenet

FOLDER\_FOR\_WATCH

/volume1/data/watch

/opt/watch

D:\\Watch

/data/watch

  
You need to define your own folders for Synology / Linux / Windows, however the locations you define in the variables, will be mapped to the docker application as per the Docker Path column.  
  
**NOTE:** It is recommended the folders you use on the host computer, remain empty until completing the entire guide and setting up all the applications. So if you plan to use folder names that current have media, you should rename the old folders, create new ones, then copy the media into the new folders after completing this guide.  
  
  
  
**PART 4 - Folders for Media Categories and Docker Applications**  
  
Now that you have identified the folders where you are going to locate your media types, download files, and docker configuration settings, you need to set up the sub-folders in each of these areas, so they are consistent between the host computer and each of the docker containers.  
  
Synology Users: Ideally you should create these folders in "File Station", but it will take a while to do them individually, so you can do them using SSH, logged into the Synology OS. Refer to the Docker / Portainer guide if needed, and minimise the amount of unnecessary commands executed while in SSH session: [Tutorial - Ultimate Starter - Docker, Portainer, Portainer Agents, and Auto-Updating Everything with Watchtower](https://www.synoforum.com/resources/ultimate-starter-docker-portainer-portainer-agents-and-auto-updating-everything-with-watchtower.183/)  
  
  
**FOLDER\_FOR\_DOCKER\_DATA Sub-Folders:**  
  
These folders will hold all the persistent configuration settings for each of the docker containers being deployed in the docker-compose file. If one of the containers / applications become corrupt, you can delete it and redeploy it using the same configuration information. If you want to reset the configuration for one of the applications, you just need to delete the contents of the respective folder and restart the container.  
  
Synology NAS Users: Make sure a suitable volume / share is created using DSM before executing by SSH.  

Code:

    cd /volume1/docker
    pwd          # check you're in correct folder before next command
    sudo mkdir gluetun jellyfin jellyseerr lidarr mylar nzbget prowlarr qbittorrent radarr readarr sabnzbd sonarr transmission whisparr

  
Linux Users:  

Code:

    cd /opt/docker
    sudo mkdir gluetun jellyfin jellyseerr lidarr mylar nzbget prowlarr qbittorrent radarr readarr sabnzbd sonarr transmission whisparr

  
Windows Users:  

Code:

    cd D:\Docker
    mkdir gluetun,jellyfin,jellyseerr,lidarr,mylar,nzbget,prowlarr,qbittorrent,radarr,readarr,sabnzbd,sonarr,transmission,whisparr

  
  
**FOLDER\_FOR\_MEDIA **Sub-Folders**:**  
  
Each of the media subfolders will store your media based on the media category... i.e. Anime in the "anime" folder, and Movies in the "movies" folder etc... Each of the \*ARR media libraries which are responsible for managing media types, will be linked to that media folder inside the container.  
  
i.e. Radarr will be linked to managed the movies located in the "/data/movies" folder, which will be mapped back to the "movies" sub-folder inside FOLDER\_FOR\_MEDIA on the host computer.  
  
Synology NAS Users: Make sure a suitable volume / share is created using DSM before executing by SSH.  

Code:

    cd /volume1/media
    pwd          # check you're in correct folder before next command
    sudo mkdir adult anime audio books comics movies music photos podcasts series software

  
Linux Users:  

Code:

    cd /opt/media
    sudo mkdir adult anime audio books comics movies music photos podcasts series software

  
Windows Users:  

Code:

    cd D:\Media
    mkdir adult,anime,audio,books,comics,movies,music,photos,podcasts,series,software

  
  
**FOLDER\_FOR\_TORRENTS **Sub-Folders**:**  
  
The sub-folders inside the Torrent folder, is to handle category downloading by Transmission.  
  
Synology NAS Users: Make sure a suitable volume / share is created using DSM before executing by SSH.  

Code:

    cd /volume1/data/torrents
    pwd          # check you're in correct folder before next command
    sudo mkdir adult anime audio books comics movies music podcasts prowlarr series software

  
Linux Users:  

Code:

    cd /opt/torrents
    sudo mkdir adult anime audio books comics movies music podcasts prowlarr series software

  
Windows Users:  

Code:

    cd D:\Torrents
    mkdir adult,anime,audio,books,comics,movies,music,podcasts,prowlarr,series,software

  
  
**FOLDER\_FOR\_USENET **Sub-Folders**:**  
  
The sub-folders inside the Usenet folder, is to handle category downloading by NZBGet.  
  
Synology NAS Users: Make sure a suitable volume / share is created using DSM before executing by SSH.  

Code:

    cd /volume1/data/usenet
    pwd          # check you're in correct folder before next command
    sudo mkdir adult anime audio books comics movies music podcasts prowlarr series software incomplete intermediate queue tmp scripts

  
Linux Users:  

Code:

    cd /opt/usenet
    sudo mkdir adult anime audio books comics movies music podcasts prowlarr series software incomplete intermediate queue tmp scripts

  
Windows Users:  

Code:

    cd D:\Usenet
    mkdir adult,anime,audio,books,comics,movies,music,podcasts,prowlarr,series,software,incomplete,intermediate,queue,tmp,scripts

  
  
**FOLDER\_FOR\_WATCH **Sub-Folders**:**  
  
Nothing... there are no sub-folders needed for the Watch folder, however whenever you place a .nzb or .torrent file into this folder, it will automatically be picked up by either NZBGet or Transmission and commence downloading the files manually.  
  
Once manual .nzb and .torrent files have been downloaded by NZBGet and Transmission, they will be saved in the FOLDER\_FOR\_USENET and FOLDER\_FOR\_TORRENTS respectively. If they are media files, they will not be imported into any of the \*ARR media libraries / Jellyfin automatically, they will need to be manually imported into the media managers / Jellyfin.  
  
The Watch folder and manual downloading will help users who want to download none media centre oriented files, such as torrents for Ubuntu ISO files etc... then the download clients will do all the work of pulling in the files for you.  