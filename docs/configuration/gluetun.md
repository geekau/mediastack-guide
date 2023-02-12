# Gluetun VPN - Secure Outbound Network Traffic

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Basic intro to Docker... embed Docker intro video etc..

Provide steps to install Docker on Windows, Linux, MacOS, Synology NAS and other hosts where possible

---

## Intro

Gluetun is a "Lightweight swiss-knife-like VPN client to multiple VPN service providers", it has built-in support for many Internet VPN Providers such as NordVPN / Private Internet Access (PIA), and also supports customised configurations that support OpenVPN and Wireguard solutions. 



The Gluetun docker container is the MOST IMPORTANT container in the Media-Guide, as it



The Gluetun docker container will establish a secure VPN tunnel to your choice of VPN service provider, and then it will force all of the other docker applications in the stack to use the VPN tunnel, if they need to communicate out to the Internet. If Gluetun drops the VPN tunnel at any time, for any reason, then all Internet traffic between the docker applications and the Internet are blocked until the VPN connection is re-established. This provides encrypted security to all data transfers, and assurance that unencrypted data will not be sent if there is a network error.  
  
All local data traffic between the applications in the docker stack, use the basic HTTP / unencrypted protocol, as the data in not going out to the Internet. This saves a considerable amount of configuration of digital certificates on portals / data traffic which will only be used internally.  
  
**NOTE:** All network traffic going in and out of the **DOCKER\_SUBNET** goes through the Gluetun security container. Some guides advise to only secure the network traffic for the download clients, this guide takes a more secure approach and secures ALL network going out to the Internet.  




- Gluetun Docker Image: [https://hub.docker.com/r/qmcgaw/gluetun](https://hub.docker.com/r/qmcgaw/gluetun)
- Gluetun Wiki: [https://github.com/qdm12/gluetun/wiki](https://github.com/qdm12/gluetun/wiki)


