# Welcome to MediaStack.Guide

With many people owning digital media such as CDs, DVD, and Blu-ray disks, home movies, personal photos, personal music collection, its common that people want to build home media servers in order to manage and access their digital libraries from any device within their home network, their mobile devices, and even remotely when they may be away on holidays or having a lunch break at work.

This guide will help you rapidly deploy all the applications you need in a full Docker build, to operate a Jellyfin, Jellyseerr, *ARR Media Library Managers (Prowlarr / Sonarr / Radarr / Lidarr / Readarr etc..) and Tdarr Automated Media Transcoding enabled media stack, and has been thoroughly tested on Linux, Windows and Synology NAS servers.


Fully encrypted outbound network - The guide establishes a full VPN encrypted Internet connection for all outbound communications, so all network traffic to Torrent / Usenet and meta-data servers are fully encrypted as they leave your network, in order to provide you full privacy. If the VPN connection fails / drops, or is stopped for any reason, then all outbound traffic is completely restricted, until the VPN connection is re-established.



Fully encrypted inbound - This guide will also establish an inbound Nginx reverse proxy into your network, using 


 Jellyfin, Jellyseerr, NZBGet, Transmission and *ARR media stack using this docker-compose guide in approximately 30 - 60 minutes, on Linux, Windows or Synology NAS, and potentially more Docker enabled environments.

This guide will cover all the steps needed to initially install and configure a secure docker hosted media environment, with all the applications needed to download torrents and Usenet content which you have a right to use in your media library, and allow you to stream the media via a simple web browser, and even stream the media to your Smart TV / Apple TV apps around the house.

This guide ensures all network traffic is securely hidden using a VPN, and encrypting ALL traffic in / out of your home network. It can also be used on your Synology NAS, or any other Linux / Windows / MacOS machine running the Docker environment.

With many people owning CDs, DVD, and Blu-ray disks, there is demand to make people's media content more transferrable in their home media systems, so it can be viewed on their personal devices. People also want to be able to put their own home movies / photos onto their media servers, so it too can be freely shared between their devices.

NOTE: 

NOTE: It is highly recommended not adding any of your own media files or libraries into the Docker folders / applications, until after setting up the entire media stack, then you can add your media in a structured manner.


!!! warning "Piracy Notice"

    This guide is not about, nor promotes, the illegal piracy of digital media content from their respected / licensed owners.
    
    This guide assumes no responsibility for users who may access or download digital media content, which they do not have legal rights.



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



