# qBittorent - Torrent Download Client

qBittorrent is a well established open-source BitTorrent client. qBittorrent features a light footprint, whilst providing all the features you may need. It uses the high-tech libtorrent-rasterbar library, which means greater download and upload speed, as well as excellent support of the latest features in the BitTorrent protocol qBittorrent is fast, stable and provides unicode support as well as many features.

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Basic intro to Docker... embed Docker intro video etc..

Provide steps to install Docker on Windows, Linux, MacOS, Synology NAS and other hosts where possible


## Heading Two

## Heading Three



**NOTE: If the qBittorrent portal fails to load with an error message**, it may be due to the themepark module, this can be resolved by editing "FOLDER_FOR_CONFIGS/qbittorrent/qBittorrent/qBittorrent.conf" and changing "WebUI\AlternativeUIEnabled=true" to "false" and restarting qBittorrent.




**PART 7 - Configuring Your Torrent / NZB Download Clients  
  
  
Validating The Security of Your VPN Network Connection:**  
  
As the Gluetun container is providing full VPN encryption for the entire Docker stack, its important to first check the VPN is providing obscurity for your Internet connection.  
  
From any computer in your network, you will be able to see what the IP Address for your Internet connection is by going to [ifconfig.io](http://ifconfig.io)  
  
Now open Portainer, and go to the Transmission and NZBGet containers and connect to "Console", then type the following into the terminal window:  
  

Code:

    curl ifconfig.io

  
This will show the IP Address being used by your Transmission and NZBGet containers, which is being provided by the Gluetun VPN connection.  
  
You can check the location of the IP Address at [IP Location](https://iplocation.com)  
  
**NOTE:** If the Gluetun container is not running, or does not have an active VPN connection, then no traffic from the other containers (Transmission / NZBGet etc…) will be allowed to go out to the Internet; it is all blocked unless a secure VPN tunnel is active.  
  
**NOTE:** If you are using an active VPN account and are not able to secure a VPN connection, you should seek assistance before progressing. Synology users may need to check VPN / TUN prerequisite details in this article, and seek guidance from the Synology community: [Synology prerequisites · qdm12/gluetun Wiki](https://github.com/qdm12/gluetun/wiki/Synology-prerequisites)  
  
  
**Transmission - Torrent Download Client:**  
  
Transmission connects to trackers, seeders and peers in the torrent network in order to access content which has been uploaded to torrent groups.  
  
1\. Open Transmissions Portal: [http://localhost:9091](http://localhost:9091)  
  
2\. Press the "Spanner" icon in the bottom left corner to open "Preferences Menu"  
  
3\. Torrents Tab - Downloading to… Change this to: **/data/torrents**  
  
4\. You can adjust Torrent, Speed, Peer, and Network settings in this section. Only adjust these if you know what you're doing. Don't change the download path or peering port, as these a relative to the Transmission Docker container, not your local file or network settings - adjust these in the ENV docker-compose file.  
  
5\. If you need to manually download torrent files, they can be placed into your **FOLDER\_FOR\_WATCH** folder, and Transmission will start to download the file.  
  
6\. Completed manual file downloads will be placed into **FOLDER\_FOR\_TORRENT** folder.  
  
  
**NZBGet - Usenet Download Client:**  
  
1\. Open NZBGet Portal: [http://localhost:6789](http://localhost:6789)  

*   Default Username: nzbget
*   Default Password: tegbzn6789

2\. Go to the Settings page: [http://localhost:6789/#ConfigTab](http://localhost:6789/#ConfigTab)  
  
3\. "PATHS" menu, change these paths only:  

*   MainDir: /data/usenet
*   DestDir: /data/usenet
*   NzbDir: /data/watch

  
4\. "NEWS-SERVERS" menu: Use this page to configure all your Usenet News Servers - Gaining access to Usenet News Servers is out of scope for this guide - sorry.  
  
5\. "SECURITY" menu: Leave these as default. However, you can empty both ControlUsername and ControlPassword fields if you want to remove username and password prompts each time you access the NZBGet portal.  
  
6\. "CATEGORIES" menu: DELETE ALL THE DEFAULT CATEGORIES  
  
7\. Add the following new category names, destdirs, and aliases for each of the "ARR" applications:  
  
**NOTE:** They must be in LOWERCASE only.  
  
  

**ARE THESE THE CORRECT CATEGORIES FOR STARTERS?  
  
ARE THE CATEGORY ALIASES ALLOCATED CORRECTLY?**​

  
  
  

Category.Name:​

Category.DestDir​

Category.Aliases​

adult

adult

xxx,\*hentai

anime

anime

audio

audio

audible

books

books

epub

comics

comics

manga

movies

movies

music

music

podcasts

podcasts

prowlarr

prowlarr

series

series

tv\*

software

software

console,pc

  
**NOTE:** You should now have 11 categories.... all in lowercase.  
  
8\. "RSS FEEDS" menu: Leave these as default  
  
9\. "INCOMING NZBS" menu: Change "NzbDirFileAge" to 5 seconds  
  
11\. "DOWNLOAD QUEUE" menu: Leave these as default  
  
12\. "CONNECTION" menu: Leave these as default  
  
13\. "LOGGING" menu: Leave these as default  
  
14\. "SCHEDULER" menu: Leave these as default  
  
15\. "CHECK AND REPAIR" menu: Leave these as default  
  
16\. "UNPACK" menu: Leave these as default  
  
17\. "EXTENSION SCRIPTS" menu: Leave these as default  
  
18\. Save all your changes and allow NZBGet to restart  
  
  
.
