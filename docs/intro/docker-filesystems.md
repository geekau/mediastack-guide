# Docker Filesystems and Folders

## Set up all of the folders / subfolders:
The commands suit the folders defined above in your ENV file for `FOLDER_FOR_CONFIGS` and `FOLDER_FOR_MEDIA`.

## For Linux hosted data folders:
If you used Linux / NAS folders in the ENV file, then use the following commands to create the necessary folders:


!!! note "This is a note code fence"

    Select something below:

    FOLDER_FOR_CONFIGS  
    FOLDER_FOR_MEDIA


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

```
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
