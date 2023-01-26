# Markdown Examples Used Throughout Site

## Copy and Paste These As Needed

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

### Third Heading

This is the third heading.

#### Fourth Heading

This is the fourth heading.

##### Fifth Heading

This is the fifth heading.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

``` mermaid
graph TB
    c1-->a2
    subgraph Download Clients
    a1-->a2
    end
    subgraph two
    b1-->b2
    end
    subgraph three
    c1-->c2
    end
```

``` mermaid
flowchart LR
    subgraph Download Clients
	SABnzbd-->VPN
	qBittorrent-->VPN
    end
    subgraph Internet
	VPN-->gateway[VPN Gateway]
	end
```


<form>
  <label for="FOLDER_FOR_CONFIGS">FOLDER_FOR_CONFIGS:</label>
  <input type="text" id="FOLDER_FOR_CONFIGS" name="FOLDER_FOR_CONFIGS"><br>
  <label for="FOLDER_FOR_MEDIA">FOLDER_FOR_MEDIA:</label>
  <input type="text" id="FOLDER_FOR_MEDIA" name="FOLDER_FOR_MEDIA">
</form>





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




!!! danger

    === "C"

        ``` c
        #include <stdio.h>

        int main(void) {
        printf("Hello world!\n");
        return 0;
        }
        ```

    === "C++"

        ``` c++
        #include <iostream>

        int main(void) {
        std::cout << "Hello world!" << std::endl;
        return 0;
        }
        ```



![Image title](https://dummyimage.com/600x400/eee/aaa){ loading=lazy,align=left }

++ctrl+alt+del++

<figure markdown>
  ![Image title](https://dummyimage.com/600x400/){ width="300" }
  <figcaption>Image caption</figcaption>
</figure>

!!! note

    This is a Note field... copy this example

---

!!! abstract

    This is an Abstract field... copy this example

---

!!! info

    This is an Info field... copy this example

    === "Linux Shell"
        ``` shell
        This is linux code
        ```
    === "Windows Prompt"
        ``` powershell
        This is linux code
        ```
    === "Synology SSH"
        ``` putty
        This is linux code
        ```

---

!!! tip

    This is a Tip field... copy this example

---

!!! success

    This is a Success field... copy this example

---

!!! question

    This is a Question field... copy this example

---

!!! warning

    This is a Warning field... copy this example

---

!!! failure

    This is a Failure field... copy this example

---

!!! danger

    This is a Danger field... copy this example

---

!!! bug

    This is a Bug field... copy this example

---

!!! example

    This is an Example field... copy this example

---

!!! quote

    This is a Quote field... copy this example

---


