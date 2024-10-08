# Setting Up Application and Media Folders

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



## Set up all of the folders / subfolders:
The commands suit the folders defined above in your ENV file for `FOLDER_FOR_MEDIA` and `FOLDER_FOR_DATA`.

## For Linux hosted data folders:
If you used Linux / NAS folders in the ENV file, then use the following commands to create the necessary folders:





!!! note "Select the correct operating system to execute desired commands:"

    - `FOLDER_FOR_MEDIA`  
    - `FOLDER_FOR_DATA`  
    - `UID`  
    - `GID`  

    === "Linux Shell"

        The Docker process on most Linux distros run as the "docker" user, and all network shares normally have Group ID as "users", so we only need to declare the User ID which Docker uses to access shares in the "FOLDER_FOR_MEDIA" folder.

        Check your Docker user ID with the command `id docker`, and update the PUID value below.

        ``` bash
        export FOLDER_FOR_MEDIA=/your-media-folder       # Change to where you want your media to be stored
        export FOLDER_FOR_DATA=/your-app-configs         # Change to where you want your container configurations to be stored

        export PUID=1000
        export PGID=1000

        sudo -E mkdir -p $FOLDER_FOR_DATA/{authelia/assets,bazarr,ddns-updater,gluetun,heimdall,homarr/{configs,data,icons},homepage,jellyfin,jellyseerr,lidarr,mylar,plex,portainer,prowlarr,qbittorrent,radarr,readarr,sabnzbd,sonarr,swag,tdarr/{server,configs,logs},tdarr_transcode_cache,unpackerr,whisparr}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/media/{anime,audio,books,comics,movies,music,photos,tv,xxx}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/usenet/{anime,audio,books,comics,complete,console,incomplete,movies,music,prowlarr,software,tv,xxx}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/torrents/{anime,audio,books,comics,complete,console,incomplete,movies,music,prowlarr,software,tv,xxx}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/watch
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/filebot/{input,output}
        sudo -E chmod -R 775 $FOLDER_FOR_MEDIA $FOLDER_FOR_DATA
        sudo -E chown -R $PUID:$PGID $FOLDER_FOR_MEDIA $FOLDER_FOR_DATA
        ```
 
    === "Windows Command Prompt"

        ``` cmd
        set FOLDER_FOR_MEDIA=D:\Your-Media-Folder        # Change to where you want your media to be stored
        set FOLDER_FOR_DATA=D:\Your-App-Configs          # Change to where you want your container configurations to be stored

        FOR /D %I IN (authelia\assets bazarr ddns-updater gluetun heimdall homarr\configs homarr\data homarr\icons homepage jellyfin jellyseerr lidarr mylar plex portainer prowlarr qbittorrent radarr readarr sabnzbd sonarr swag tdarr\server tdarr\configs tdarr\logs tdarr_transcode_cache unpackerr whisparr) DO mkdir %FOLDER_FOR_DATA%\%I
        FOR /D %I IN (anime audio books comics movies music photos tv xxx) DO mkdir %FOLDER_FOR_MEDIA%\media\%I
        FOR /D %I IN (anime audio books comics complete console incomplete movies music prowlarr software tv xxx) DO mkdir %FOLDER_FOR_MEDIA%\usenet\%I
        FOR /D %I IN (anime audio books comics complete console incomplete movies music prowlarr software tv xxx) DO mkdir %FOLDER_FOR_MEDIA%\torrents\%I
        mkdir %FOLDER_FOR_MEDIA%\watch
        mkdir %FOLDER_FOR_MEDIA%\filebot\input %FOLDER_FOR_MEDIA%\filebot\output
        ```

    === "MacOS Shell"

        ``` bash
        Waiting Testing
        ```

    === "Synology NAS (SSH)"

        The Docker process on Synology NAS runs as "root", so user and group permissions for $FOLDER_FOR_DATA will be set as "root". All "Shared Folders" you create manually have Group ID as "users", so we only need to declare the User ID (PUID) which Docker uses to access files inside the "FOLDER_FOR_MEDIA" folder.

        Check your Docker user ID with the command `id docker`, and update the PUID value below.

        ``` bash
        export FOLDER_FOR_MEDIA=/volume1/media               # Change to where you want your media to be stored
        export FOLDER_FOR_DATA=/volume1/docker/appdata       # Change to where you want your container configurations to be stored

        export PUID=1000
        export PGID=users

        sudo -E mkdir -p $FOLDER_FOR_DATA/{authelia/assets,bazarr,ddns-updater,gluetun,heimdall,homarr/{configs,data,icons},homepage,jellyfin,jellyseerr,lidarr,mylar,plex,portainer,prowlarr,qbittorrent,radarr,readarr,sabnzbd,sonarr,swag,tdarr/{server,configs,logs},tdarr_transcode_cache,unpackerr,whisparr}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/media/{anime,audio,books,comics,movies,music,photos,tv,xxx}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/usenet/{anime,audio,books,comics,complete,console,incomplete,movies,music,prowlarr,software,tv,xxx}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/torrents/{anime,audio,books,comics,complete,console,incomplete,movies,music,prowlarr,software,tv,xxx}
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/watch
        sudo -E mkdir -p $FOLDER_FOR_MEDIA/filebot/{input,output}
        sudo -E chmod -R 775 $FOLDER_FOR_MEDIA $FOLDER_FOR_DATA
        sudo -E chown -R $PUID:$PGID $FOLDER_FOR_MEDIA $FOLDER_FOR_DATA
        ```




### For Window hosted data folders:
If you used Windows folders in the ENV file, then use the following commands to create the necessary folders:
### Folder mappings between host and Docker containers:
After you run the commands above (Linux or Windows), **this will be your folder structure INSIDE your docker containers**:

!!! note "Folders on Host <--> "

    ``` { .text .no-copy }
    $ tree $FOLDER_FOR_MEDIA

    ⠀⠀⠀⠀⠀Docker Host Computer:⠀⠀⠀⠀⠀⠀⠀⠀⠀Inside Docker Containers:
    ├── /FOLDER_FOR_MEDIA   ⠀       ├── /data
    ⠀⠀⠀⠀⠀├── media                  ⠀⠀⠀⠀├── media        <-- Media is stored / managed under this folder
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── anime                 │⠀⠀⠀⠀├── anime       <-- Sonarr Media Library Manager
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── audio                 │⠀⠀⠀⠀├── audio       <-- Lidarr Media Library Manager
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── books                 │⠀⠀⠀⠀├── books       <-- Readarr Media Library Manager
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── comics                │⠀⠀⠀⠀├── comics      <-- Mylar Media Library Manager
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── movies                │⠀⠀⠀⠀├── movies      <-- Radarr Media Library Manager
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── music                 │⠀⠀⠀⠀├── music       <-- Lidarr Media Library Manager
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── photos                │⠀⠀⠀⠀├── photos      <-- N/A - Add Personal Photos
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── tv                    │⠀⠀⠀⠀├── tv          <-- Sonarr Media Library Manager
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀└── xxx                   │⠀⠀⠀⠀└── xxx         <-- Whisparr Media Library Manager
    ⠀⠀⠀⠀⠀├── torrents               ⠀⠀⠀⠀├── torrents     <-- Folder for Torrent Downloads Data
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── anime                 │⠀⠀⠀⠀├── anime       <-- Anime Category (Sonarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── audio                 │⠀⠀⠀⠀├── audio       <-- Audio Category (Lidarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── books                 │⠀⠀⠀⠀├── books       <-- Book Category (Readarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── comics                │⠀⠀⠀⠀├── comics      <-- Comic Category (Mylar)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── complete              │⠀⠀⠀⠀├── complete    <-- Completed / General Downloads
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── console               │⠀⠀⠀⠀├── console     <-- Comic Category (Manual DL)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── incomplete            │⠀⠀⠀⠀├── incomplete  <-- Incomplete / Working Downloads
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── movies                │⠀⠀⠀⠀├── movies      <-- Movie Category (Radarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── music                 │⠀⠀⠀⠀├── music       <-- Music Category (Lidarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── prowlarr              │⠀⠀⠀⠀├── prowlarr    <-- Uncategorised Downloads from Prowlarr
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── tv                    │⠀⠀⠀⠀├── tv          <-- TV Series (Sonarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── software              │⠀⠀⠀⠀├── software    <-- Software Category (Manual DL)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀└── xxx                   │⠀⠀⠀⠀└── xxx         <-- Adult / XXX Category (Whisparr)
    ⠀⠀⠀⠀⠀├── usenet                 ⠀⠀⠀⠀├── usenet       <-- Folder for Usenet Downloads Data
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── anime                 │⠀⠀⠀⠀├── anime       <-- Anime Category (Sonarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── audio                 │⠀⠀⠀⠀├── audio       <-- Audio Category (Lidarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── books                 │⠀⠀⠀⠀├── books       <-- Book Category (Readarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── comics                │⠀⠀⠀⠀├── comics      <-- Comic Category (Mylar)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── complete              │⠀⠀⠀⠀├── complete    <-- Completed / General Downloads
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── console               │⠀⠀⠀⠀├── console     <-- Comic Category (Manual DL)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── incomplete            │⠀⠀⠀⠀├── incomplete  <-- Incomplete / Working Downloads
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── movies                │⠀⠀⠀⠀├── movies      <-- Movie Category (Radarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── music                 │⠀⠀⠀⠀├── music       <-- Music Category (Lidarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── prowlarr              │⠀⠀⠀⠀├── prowlarr    <-- Uncategorised Downloads from Prowlarr
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── tv                    │⠀⠀⠀⠀├── tv          <-- TV Series (Sonarr)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀├── software              │⠀⠀⠀⠀├── software    <-- Software Category (Manual DL)
    ⠀⠀⠀⠀⠀│⠀⠀⠀⠀└── xxx                   │⠀⠀⠀⠀└── xxx         <-- Adult / XXX Category (Whisparr)
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
**TIMEZONE**\=Europe/Zurich  
  
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
  
If you want to be security conscience and only allow members of the "docker" group (and running docker applications) access to the docker and media folders, you can execute the following commands, which also turn on the SetGid bit for the group, so any new folder / file created inside these folders will have full permissions to anyone in the "docker" group; so being a member of the "docker" group is key.  
  

Code:

    sudo chmod -R u+rwx,g+rws,o+rx,o-w /mediastack /mediastackdata
    sudo chown -R docker:docker /mediastack /mediastackdata

  

Code:

    drwxrwsr-x+  15 docker       docker             4096 Jan 01 00:10 /mediastack
    drwxrwsr-x+  12 docker       docker             4096 Jan 01 00:10 /mediastackdata

  
  
If you don't share your Linux host computer with other users and you are having problems with access and permissions, you can always use the following commands, which allow everyone to have absolute access:
  

Code:

    sudo chmod -R 777 /mediastack /mediastackdata
    sudo chown -R docker:docker /mediastack /mediastackdata

  
**NOTE:** If you ever experience issues with file / permission access issues, then rerun both the "chmod" and "chown" commands above, and restart your docker media stack.  
  
  
**File Permissions for Windows OS Users:**  
  
Is this even needed, does Docker run as system or local user account? - needs testing.  
  

