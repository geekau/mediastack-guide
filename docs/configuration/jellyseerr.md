# Jellyseerr - Media Request Manager

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Basic intro to Docker... embed Docker intro video etc..

Provide steps to install Docker on Windows, Linux, MacOS, Synology NAS and other hosts where possible


## Heading Two

## Heading Three





  
  
PART 11 - Configuring Jellyseerr  
  
  
[http://localhost:5055](http://localhost:5055) jellyseerr  
  
  
  
When you open Jellyseer for the first time, you'll be asked to sign in… select "Use your Jellyfin Account", and enter the details from your Jellyfin server in order to link it to Jellyseerr.  
  
Jellyfin URL: [http://localhost:8096](http://localhost:8096)  
Email Address: The email address is only used if you want to set up notifications when media has been downloaded, however it is a mandatory field.  
Username: Same username as Jellyfin  
Password: Same password as Jellyfin  
  
After connecting Jellyseerr to Jellyfin, you will need to synchronise the libraries between the two applications.  
  
Select "Sync Libraries", then use the slide toggle to select "Movies" and "Series", However…. DO NOT PRESS "START SCAN", skip the library scan and go straight to "Continue".  
  
**NOTE**: We skip the library scan on initial setup as it can take quite a while to scan the libraries, it is also dependant on Jellyfin having its libraries fully scanned and up to date, so it will be better to scan the libraries after all the configurations are completed.  
  
NOTE: Adult Content - Jellyseerr does not manage Adult content requests, so if you are using Whisparr, the library will appear in "Jellyfin Libraries", however there is no need to activate it for syncing. If the library exists in Jellyfin, it will be seen in Jellyseerr, you just don't need to enable it.  
  
  
Radarr Settings:  
  
Setting up non-4K defaults  
  
Select "Add Radarr Server"  
Default Server: Yes  
4K Server: No  
Server Name: Radarr - FHD 1080P  
Hostname of IP Address: localhost  
Port: 7878  
Use SSL: No  
API Key: Can be found in Radarr application on "Settings" -- "General" page.  
[http://localhost:7878/settings/general](http://localhost:7878/settings/general)  
URL Base: Empty  
Quality Profile: HD-1080p  
Root Folder: /data/media/movies  
Minimum Availability: Released  
Tags: Empty  
External URL: [http://media-server:7878](http://media-server:7878) (Radarr's network address, used in links when sending email notifications)  
Enable Scan: Yes  
Enable Automatic Search: Yes  
  
Test and Save.  
  
Setting up 4K defaults  
Default Server: Yes  
4K Server: Yes  
Server Name: Radarr - UHD 4K  
Hostname of IP Address: localhost  
Port: 7878  
Use SSL: No  
API Key: Can be found in Radarr application on "Settings" -- "General" page.  
[http://localhost:7878/settings/general](http://localhost:7878/settings/general)  
URL Base: Empty  
Quality Profile: Ultra-HD  
Root Folder: /data/media/movies  
Minimum Availability: Released  
Tags: Empty  
External URL: [http://media-server:7878](http://media-server:7878) (Radarr's network address, used in links when sending email notifications)  
Enable Scan: Yes  
Enable Automatic Search: Yes  
  
Test and Save.  
  
  
Sonarr Settings:  
  
Setting up non-4K defaults  
  
Select "Add Sonarr Server"  
Default Server: Yes  
4K Server: No  
Server Name: Sonarr - FHD 1080P  
Hostname of IP Address: localhost  
Port: 8989  
Use SSL: No  
API Key: Can be found in Radarr application on "Settings" -- "General" page.  
[http://localhost:8989/settings/general](http://localhost:8989/settings/general)  
URL Base: Empty  
Quality Profile: HD-1080p  
Root Folder: /data/media/series  
Language Profile: **\* Personal Choice \***  
Tags: Empty  
URL Base: Empty  
Anime Quality Profile: HD-1080p  
Anime Root Folder: /data/media/anime  
Anime Language Profile: **\* Personal Choice \***  
Anime Tags: Empty  
Season Folders: Yes  
External URL: [http://media-server:8989](http://media-server:8989) (Sonarr's network address, used in links when sending email notifications)  
Enable Scan: Yes  
Enable Automatic Search: Yes  
  
Test and Save.  
  
  
  
  
Setting up 4K defaults  
  
Select "Add Sonarr Server"  
Default Server: Yes  
4K Server: No  
Server Name: Sonarr - UHD 4K  
Hostname of IP Address: localhost  
Port: 8989  
Use SSL: No  
API Key: Can be found in Radarr application on "Settings" -- "General" page.  
[http://localhost:8989/settings/general](http://localhost:8989/settings/general)  
URL Base: Empty  
Quality Profile: Ultra-HD  
Root Folder: /data/media/series  
Language Profile: **\* Personal Choice \***  
Tags: Empty  
URL Base: Empty  
Anime Quality Profile: Ultra-4K  
Anime Root Folder: /data/media/anime  
Anime Language Profile: **\* Personal Choice \***  
Anime Tags: Empty  
Season Folders: Yes  
External URL: [http://media-server:8989](http://media-server:8989) (Sonarr's network address, used in links when sending email notifications)  
Enable Scan: Yes  
Enable Automatic Search: Yes  
  
Test and Save.  
  
  
After adding the connectors to Radarr and Sonarr, Jellyseerr will be fully functional, however we want to do some additional configurations before importing users and media information from Jellyfin.  
  
Go to "Settings" -- "General" and make any changes to region and language as needed.  
  
  
Go to "Settings" -- "Users" and make any changes for users, you may want to change the default permissions assigned to new users.  
  
If you want to allow all users to automatically request, approve and download any media type and quality up to 1080P, then you would select "Request", "Auto-Approved", and "Auto-Request". You can select additional permissions and allow automated 4K requests, however the data will quickly add up on the server if is it not controlled, so grant this privilege with due care.  
  
NOTE: These privileges / permissions are applied when new accounts are created or imported from Jellyfin, they do not effect existing user accounts.  
  
  
Go to "Settings" -- "Jellyfin" and select "Start Scan" to commence scanning the Jellyfin libraries for all media.  
  
Go to "Settings" -- "Notifications", you can add any email server settings or integrations if you want to get notifications on the status of your media requests.  
  
Go to the "Users" menu, and you can now create local users, or "Import Jellyfin Users" (preferred). The new users will be granted the privileges / permissions which we set up earlier.


