# Individual Docker Compose Installation

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Basic intro to Docker... embed Docker intro video etc..

Provide steps to install Docker on Windows, Linux, MacOS, Synology NAS and other hosts where possible


## Heading Two

## Heading Three



## 4 - Install the Docker applications individually as you need them.

**NOTE: Gluetun MUST be installed as the first container**, as it sets up the VPN and the internal Bridge network the other containers will join (**media_network**).


### Deploy VPN and Internal Docker Bridge "media_network":
```
sudo docker compose --file docker-compose-gluetun.yaml --env-file docker-compose.env up -d
```
**NOTE - Windows users:** Do not use the "**sudo**" at the front of the commands.

==**NOTE:**  "WARNING: Found orphan containers (gluetun, qbittorrent, sabnzbd, prowlarr, prowlarr) for this project"==

This ==WARNING== can be safely ignored, as we're loading the project apps one at a time, rather than all in one YAML file.

## Deploy Media Server and Content Request Manager:
```
sudo docker compose --file docker-compose-jellyfin.yaml     --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-jellyseerr.yaml   --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-plex.yaml         --env-file docker-compose.env up -d
```


## Deploy Index Manager and Media Library Managers:
```
sudo docker compose --file docker-compose-prowlarr.yaml --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-lidarr.yaml   --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-mylar3.yaml   --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-radarr.yaml   --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-readarr.yaml  --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-sonarr.yaml   --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-whisparr.yaml --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-bazarr.yaml   --env-file docker-compose.env up -d
```


## Deploy Download Clients:
```
sudo docker compose --file docker-compose-qbittorrent.yaml --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-sabnzbd.yaml     --env-file docker-compose.env up -d
```


## Deploy Archive Unpacker and Automatic Video Re-encoding:
```
sudo docker compose --file docker-compose-unpackerr.yaml --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-tdarr.yaml     --env-file docker-compose.env up -d
```


## Deploy Reverse Proxy (with SSL Certbot) and Cloudflare Proxy
```
sudo docker compose --file docker-compose-swag.yaml         --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-authelia.yaml     --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-heimdall.yaml     --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-ddns-updater.yaml --env-file docker-compose.env up -d
sudo docker compose --file docker-compose-flaresolverr.yaml --env-file docker-compose.env up -d
```
>The "your-domain-name.com" / IP Address validation is performed when the container is started for the first time. Nginx won't be up and start the web server, until ssl certs are successfully generated and installed.

## Deploy Portainer-CE to View Docker via GUI
```
sudo docker compose --file docker-compose-portainer.yaml    --env-file docker-compose.env up -d
```







  
**PART 6 - Deploying the Docker Compose Media Stack**  
  
  
When you deploy the docker compose build, it will download 12 Docker images from the public DockerHub repository before building the Docker containers and secure network. As its the first time you've deployed the docker compose stack, it will take a few minutes to download the necessary Docker images. If you need to redeploy the docker compose due to customisation, or fixing a fault, the containers will be instantly, as the images will still be available on your host computer.  
  
You can deploy the docker compose build two ways, either via the Linux terminal (PowerShell for Windows), or via Portainer if you installed it as part of the earlier Docker / Portainer guide: [Tutorial - Ultimate Starter - Docker, Portainer, Portainer Agents, and Auto-Updating Everything with Watchtower](https://www.synoforum.com/resources/ultimate-starter-docker-portainer-portainer-agents-and-auto-updating-everything-with-watchtower.183/)  
  
If you have issues loading the YAML file, whether its corrupt, or you've made changes, you can copy and paste the entire YAML file contents to an online YAML Validation Tool, and it will advise if, and where, there are errors in the YAML code, so you can fix it.  
  
**Online YAML Validator:** [Validate YAML - Online YAML Tools](https://onlineyamltools.com/validate-yaml)  
  
**NOTE:** Don't add any of your current media files into the folders you created above, we'll add all the media at the end in a structured process / format.  
  
  
**Deployment via Synology SSH / Linux Terminal / Windows** **PowerShell****:**  
  
Deploying the docker compose media stack is exactly the same process using Synology SSH / Linux Terminal / Windows PowerShell, as the only difference between these systems is the paths for each Operating System, however we've added the paths for the relevant Operating Systems into the Environment file, so Docker will just pick this up during the build and map the local folders you've already declared.  
  
Execute the following command to build the docker compose media stack:  
  

Code:

    sudo docker compose --file docker-compose-mediastack.yaml --project-name media_stack --env-file docker-compose-mediastack.env up

  
You will notice all of the images being downloaded from DockerHub, then all of the containers will display their log output on the screen, which is an easy way to identify if any errors occur.  
  
Press "CTRL+ C" to exit the docker console, if you're happy there were no errors and you want it to run in "detached mode" (i.e. in the background), the run the command again with the "-d" (detached) argument.  
  

Code:

    sudo docker compose --file docker-compose-mediastack.yaml --project-name media_stack --env-file docker-compose-mediastack.env up -d

  
NOTE: While you now have a running media stack in Docker, you will need to manage all changes / executions from the terminal window / PowerShell from now on, and that's OK, however if you want the flexibility and ease of use to change / save settings in an easy to use GUI, then Portainer may be the way to load and manage your docker compose media stake.  
  