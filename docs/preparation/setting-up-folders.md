# Setting Up Application and Media Folders

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



## Set up all of the folders / subfolders:
The commands suit the folders defined above in your ENV file for `FOLDER_FOR_CONFIGS` and `FOLDER_FOR_MEDIA`.

## For Linux hosted data folders:
If you used Linux / NAS folders in the ENV file, then use the following commands to create the necessary folders:





!!! note "Select the correct operating system to execute desired commands:"

    - `FOLDER_FOR_CONFIGS`  
    - `FOLDER_FOR_MEDIA`  
    - `UID`  
    - `GID`  

    === "Linux Shell"

        ``` bash
        export FOLDER_FOR_CONFIGS=/home/geekau/docker
        export FOLDER_FOR_MEDIA=/home/geekau/media-stack

        sudo -E mkdir -p $FOLDER_FOR_CONFIGS/{authelia,bazarr,ddns-updater,gluetun,heimdall,jellyfin,jellyseerr,lidarr,mylar3,portainer,prowlarr,qbittorrent,radarr,readarr,sabnzbd,sonarr,swag,tdarr,tdarr_transcode_cache,unpackerr,whisparr}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/media/{adult,anime,audio,books,comics,movies,music,photos,podcasts,series,software}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/usenet/{adult,anime,audio,books,comics,movies,music,prowlarr,podcasts,series,software}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/torrents/{adult,anime,audio,books,comics,movies,music,prowlarr,podcasts,series,software}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/watch
        sudo -E chmod -R 775 $FOLDER_FOR_CONFIGS $FOLDER_FOR_MEDIA
        sudo -E chown -R geekau:geekau $FOLDER_FOR_CONFIGS $FOLDER_FOR_MEDIA
        ```

    === "Windows PowerShell"

        ``` powershell
        set FOLDER_FOR_CONFIGS=D:\Storage\Docker
        set FOLDER_FOR_MEDIA=D:\Storage\Media-Stack

        FOR /D %I IN (authelia bazarr ddns-updater gluetun heimdall jellyfin jellyseerr lidarr mylar3 portainer prowlarr qbittorrent radarr readarr sabnzbd sonarr swag tdarr tdarr_transcode_cache unpackerr whisparr) DO mkdir %FOLDER_FOR_CONFIGS%\%I
        FOR /D %I IN (adult anime audio books comics movies music photos podcasts series software) DO mkdir %FOLDER_FOR_MEDIA%\media\%I
        FOR /D %I IN (adult anime audio books comics movies music podcasts prowlarr series software) DO mkdir %FOLDER_FOR_MEDIA%\usenet\%I
        FOR /D %I IN (adult anime audio books comics movies music podcasts prowlarr series software) DO mkdir %FOLDER_FOR_MEDIA%\torrents\%I
        mkdir %FOLDER_FOR_MEDIA%\watch
        ```

    === "MacOS Shell"

        ``` bash
        Waiting Testing
        ```

    === "Synology NAS (SSH)"

        ``` bash
        Synology - ADD HERE
        ```




### For Window hosted data folders:
If you used Windows folders in the ENV file, then use the following commands to create the necessary folders:
### Folder mappings between host and Docker containers:
After you run the commands above (Linux or Windows), **this will be your folder structure INSIDE your docker containers**:

!!! note "Folders on Host <--> "

    ``` { .text .no-copy }
    $ tree $FOLDER_FOR_MEDIA

    ⠀⠀⠀⠀⠀Host Computer:⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀Inside Containers:
    ├── /FOLDER_FOR_MEDIA   ⠀       ├── /data
    ⠀⠀⠀⠀⠀├── media                  ⠀⠀⠀⠀├── media        <-- Media is located / managed under this folder
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── adult                 │⠀⠀⠀⠀├── adult
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── anime                 │⠀⠀⠀⠀├── anime
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── audio                 │⠀⠀⠀⠀├── audio
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── books                 │⠀⠀⠀⠀├── books
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── comics                │⠀⠀⠀⠀├── comics
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── movies                │⠀⠀⠀⠀├── movies
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── music                 │⠀⠀⠀⠀├── music
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── photos                │⠀⠀⠀⠀├── photos
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── podcasts              │⠀⠀⠀⠀├── podcasts
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── series                │⠀⠀⠀⠀├── series
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀└── software              │⠀⠀⠀⠀└── software
    ⠀⠀⠀⠀⠀├── torrents               ⠀⠀⠀⠀├── torrents     <-- Downloads for Torrent data
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── adult                 │⠀⠀⠀⠀├── adult
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── anime                 │⠀⠀⠀⠀├── anime
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── audio                 │⠀⠀⠀⠀├── audio
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── books                 │⠀⠀⠀⠀├── books
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── comics                │⠀⠀⠀⠀├── comics
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── movies                │⠀⠀⠀⠀├── movies
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── music                 │⠀⠀⠀⠀├── music
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── podcasts              │⠀⠀⠀⠀├── podcasts
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── prowlarr              │⠀⠀⠀⠀├── prowlarr
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── series                │⠀⠀⠀⠀├── series
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀└── software              │⠀⠀⠀⠀└── software
    ⠀⠀⠀⠀⠀├── usenet                 ⠀⠀⠀⠀├── usenet       <-- Downloads for Usenet data
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── adult                 │⠀⠀⠀⠀├── adult
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── anime                 │⠀⠀⠀⠀├── anime
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── audio                 │⠀⠀⠀⠀├── audio
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── books                 │⠀⠀⠀⠀├── books
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── comics                │⠀⠀⠀⠀├── comics
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── movies                │⠀⠀⠀⠀├── movies
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── music                 │⠀⠀⠀⠀├── music
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── podcasts              │⠀⠀⠀⠀├── podcasts
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── prowlarr              │⠀⠀⠀⠀├── prowlarr
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── series                │⠀⠀⠀⠀├── series
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀└── software              │⠀⠀⠀⠀└── software
    ⠀⠀⠀⠀⠀└── watch                  ⠀⠀⠀⠀└── watch       <-- Add .nzb and .torrent files for manual download

    ```




  
**PART 5 - File Permissions Between Docker Containers and Host Computer**  
  
One of the biggest issues new users face with using Docker and accessing files on the host computer, is the inability of the container applications accessing folders / files due to incorrect permissions. If the container has incorrect permissions to the local filesystem, then access will be denied, and the container applications do not function as expected.  
  
To overcome this issue, Docker can access the folders / files of the local host computer, as a specific user and group which exists on the local system, however its imperative the local user and group which is specified in the ENV file configuration, actually exists and has the correct permissions to the folder and files on the host.  
  
For Synology / Linux users, follow the earlier guide on setting up Docker / Portainer, and create the "docker" user as documented: [Tutorial - Ultimate Starter - Docker, Portainer, Portainer Agents, and Auto-Updating Everything with Watchtower](https://www.synoforum.com/resources/ultimate-starter-docker-portainer-portainer-agents-and-auto-updating-everything-with-watchtower.183/)  
  
When logged into the terminal on Linux and Synology (via SSH), run the following command:  
  

Code:

    sudo id docker

  
This will return an entry similar to:⠀⠀⠀⠀**uid=131(docker) gid=123(docker) groups=123(docker)**  
  
This means the "docker" user has User ID of 131, Group ID of 123, and is in the following groups... just 123, which is docker. If you convert the uid and gid to PUID and PGID respectively, your config should look like this:  
  
**PUID**\=131  
**PGID**\=123  
**UMASK**\=0002 <-- Don't change this unless you know what you're doing  
**TIMEZONE**\=Australia/Brisbane  
  
Update your local Timezone using this list: [List of tz database time zones - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)  
  
**NOTE:** PUID / PGID will vary from system to system, you can't use Docker configurations from the Internet and expect them to work, unless you adjust the PUID / PGID values to match your system.  
  
  
**File Permissions for Synology NAS Users:**  
  
Synology DSM has a very complex set of permissions and folder attributes underneath the DSM web interface, effectively where the shares are located in "File Station", the the underlying folder permissions are "777" (and more), which you don't want to mess with at the command line.  
  

Code:

    drwxrwxrwx+  1 root       root             436 Jan 1 00:10 /volume1/docker

  
This means the root user and root group own the /volume1/docker share, however all of the folders and files have 777 permissions inherited recursively throughout the sub-folder structure.  
  
This might sound a bit complex, but the key point is just to use the DSM File Station web interface, and add the "docker" user to either the main shared folder, such as "/volume1/docker", or just to the selective sub-folders within a shared folder, such as "/volume1/data/torrents", "/volume1/data/usenet", and "/volume1/data/watch". This would mean the "docker" user only has access to the folders (and sub-folders) of torrents, usenet, and watch, inside the shared folder /volume1/data.  
  
Ultimately, you need to ensure the "docker" user has read/write access to whatever folders you are using on the Synology NAS, using DSM Portal.  
  
  
**File Permissions for Linux OS Users:**  
  
When you created the "docker" user for Linux, you also created a "docker" group. Additionally, you added your own Linux user account into the "docker" group, so you want to apply "docker:docker" permissions to folders for the correct access permissions to filter through the file structure.  
  
If you want to be security conscience and only allow members of the "docker" group (and running docker applications) access to for docker and media folders, you can execute the following commands, which also turn on the SetGid bit for the group, so any new folder / file created inside these folders will have full permissions to anyone in the "docker" group; so being a member of the "docker" group is key.  
  

Code:

    sudo chmod -R u+rwx,g+rws,o+rx,o-w /opt/docker /opt/media /opt/usenet /opt/torrents /opt/watch
    sudo chown -R docker:docker /opt/docker /opt/media /opt/usenet /opt/torrents /opt/watch

  

Code:

    drwxrwsr-x+  15 docker       docker             4096 Jan 01 00:10 /opt/docker
    drwxrwsr-x+  12 docker       docker             4096 Jan 01 00:10 /opt/media
    drwxrwsr-x+  12 docker       docker             4096 Jan 01 00:10 /opt/torrents
    drwxrwsr-x+  17 docker       docker             4096 Jan 01 00:10 /opt/usenet
    drwxrwsr-x+   2 docker       docker            53248 Jan 01 00:10 /opt/watch

  
  
If you don't share your Linux host computer with other users and you are having problems with access and permissions, you can always using the following commands, which allow everyone to have absolute access:  
  

Code:

    sudo chmod -R 777 /opt/docker /opt/media /opt/usenet /opt/torrents /opt/watch
    sudo chown -R docker:docker /opt/docker /opt/media /opt/usenet /opt/torrents /opt/watch

  
**NOTE:** If you ever experience issues with file / permission access issues, then rerun both the "chmod" and "chown" commands above, and restart your docker media stack.  
  
  
**File Permissions for Windows OS Users:**  
  
Is this even needed, does Docker run as system or local user account? - needs testing.  
  

