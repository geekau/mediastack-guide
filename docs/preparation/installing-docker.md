# Installing Docker on Host Computer

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly, without interferring with the applications on the host system.

When you build a Virtual Machine, you need to install an operating system, and then install all of the applications inside each virtual computer. With Docker, you only need to virtualise the application, and the Docker environment manages all the connectivity between applications, access to your local hard drives or access to the Internet. Docker allows you to containerise each application, rather than installing all applications into a Virtual Machine.

As Docker can be installed on many different Operating Systems and NAS devices, its extremely easy to deploy the same Docker applications across all of these systems, which means the MediaStack.Guide can be easily used by many people with different systems and configurations. MediaStack.Guide is each to deploy and support, even for beginners.



## Installing Docker

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Basic intro to Docker... embed Docker intro video etc..

Provide steps to install Docker on Windows, Linux, MacOS, Synology NAS and other hosts where possible



Radarr is a movie collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new movies and will interface with clients and indexers to grab, sort, and rename them. It can also be configured to automatically upgrade the quality of existing files in the library when a better quality format becomes available.

!!! Info "Additional Application Information - External Links"
    - Local WebUI Address: &nbsp; &nbsp;[http://localhost:7878](http://localhost:7878)
    - Application Website: &nbsp; &nbsp; &nbsp;[https://wiki.servarr.com/en/radarr](https://wiki.servarr.com/en/radarr)
    - Docker Information: &nbsp; &nbsp; &nbsp; [https://docs.linuxserver.io/images/docker-radarr](https://docs.linuxserver.io/images/docker-radarr)



https://www.coretechnologies.com/products/AlwaysUp/Apps/StartDockerDaemonAsAWindowsService.html

If your are using the fully secure media stack configuration and routing all outbound network traffic via the Gluetun VPN container, you can check whether the secure VPN tunnel has been established with the following Docker commands:

!!! Note "Checking if Docker Container is Connected / Hidden behind Secure VPN"

    === "Linux Shell"

        ``` bash
        sudo docker exec -it radarr bash
        ```

    === "Windows PowerShell"

        Open PowerShell and "Run as Administrator"

        ``` powershell
        wsl --install
        dism /online /enable-feature /featurename:microsoft-windows-subsystem-linux /all /norestart
        dism /online /enable-feature /featurename:virtualmachineplatform /all /norestart
        dism /online /enable-feature /featurename:hypervisorplatform /all /norestart
        wsl --set-default-version 2
        ```

        <figure markdown>
          ![Windows - Install Windows Subsystem for Linux](/img/windows-install-wsl.png){ width="300" }
          <figcaption>Windows - Install Windows Subsystem for Linux</figcaption>
        </figure>

        > You MUST reboot your Windows computer before proceeding with WSL / Docker setup.

        After rebooting, Ubuntu for WSL will commence installing, accept all defaults and set a basic username and password. The username and password don't need to be the same you use to log into Windows, they can be different, but you will need to remember these.

        After installing Ubuntu for WSL, update WSL and check it is set to run as version 2:

        ``` powershell
        wsl --update
        wsl --status
        ```

        Download and install the Microsoft "WSL2 Linux kernel update package for x64 machines" update:

        - [https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)


        <figure markdown>
          ![Windows - Install WSL2 Linux Kernel Update](/img/windows-install-wsl-update.png){ width="300" }
          <figcaption>Windows - Install WSL2 Linux Kernel Update</figcaption>
        </figure>


        <figure markdown>
          ![Windows - WSL2 Installed](/img/windows-wsl-installed.png){ width="300" }
          <figcaption>Windows - WSL2 Installed</figcaption>
        </figure>

        Download and install Docker Desktop for Windows:

        - [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)

        > You MUST select: "Use WSL 2 instead of Hyper-V" during installation


        <figure markdown>
          ![Windows - Docker Desktop Installed](/img/windows-docker-installed.png){ width="300" }
          <figcaption>Windows - Docker Desktop Installed</figcaption>
        </figure>


        <figure markdown>
          ![Windows - WSL2 Installed](/img/windows-wsl-installed.png){ width="300" }
          <figcaption>Windows - WSL2 Installed</figcaption>
        </figure>


        To install Docker Daemon as a native Windows Service, run the following command in Administrative PowerShell prompt:


        ```
        cd "C:\Program Files\Docker\Docker\resources"
        ./dockerd --register-service
        ```

        SETUP DOCKER DAEMON: https://www.coretechnologies.com/products/AlwaysUp/Apps/StartDockerDaemonAsAWindowsService.html


    === "MacOS Shell"

        ``` bash
        docker exec -it radarr bash
        ```

    === "Synology NAS (SSH)"

        ``` bash
        sudo docker exec -it radarr bash
        ```

    === "Portainer GUI"

        From the Portainer WebUI, find the container you wish to connect to, then select the `>_ Console` link.



> If the Docker container is configured to connect to the Internet through the Gluetun VPN container and there is no active VPN connection, then no network traffic will be passed out to the Internet. The Gluetun VPN connection is a safeguard for secure network transfers and activates a "hard block" when there is no VPN connection established.




<figure markdown>
  ![Windows - Install Windows Subsystem for Linux](/img/windows-install-wsl.png){ width="300" }
  <figcaption>Windows - Install Windows Subsystem for Linux</figcaption>
</figure>


## Set Up Docker User / Access


## Set up Docker App Folders


## Basic Docker Commands

## Extra Docker Resources






