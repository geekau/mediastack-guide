# Plex - Media Server

## Heading One

!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.



Basic intro to Docker... embed Docker intro video etc..

Provide steps to install Docker on Windows, Linux, MacOS, Synology NAS and other hosts where possible


## Heading Two

## Heading Three



  
  
\#### Configuring Plex to access all Media Libraries  
  
==Firstly, head over and set up accounts at Fanart and Opensubtitles, so you can enrich your Jellyfin media content. Once you have accounts, you'll need to copy the API Key from each of your account profiles==  
[https://fanart.tv](https://fanart.tv/)  
[https://opensubtitles.com](https://opensubtitles.com/) (opensubtitles.org and opensubtitles.com are the same, but .com is the newer site for accounts)  
  
  

*   Head over to Jellyfin at [http://localhost:8096](http://localhost:8096/) where you will be welcomed to Jellyfin, choose your desired language and select "Next".
*   Create a username / password for the first user account (it will become the admin account) - you can have a blank password if you desire - Select "Next".
*   DO NOT ADD MEDIA at this time, select "Next", as we want to set up Fanart and other plugins first.
*   Select your Metadata Language and Country and select "Next".
*   Set up remote access: Remote connections (Ticked), Enable port mapping (No / Unticked) - Select "Next", the "Finsh".
*   You'll be presented with a signin page, use the username / password entered previously.

  
Press the hamburger icon (3 lines) in top left corner to open the menu, then select "Dashboard", go down the bottom of the menu and open "Plugins", the select "Repositories" up the top, and add the following:  
  
Repository Name: Daniel Adov  
Repository URL: [https://raw.githubusercontent.com/danieladov/JellyfinPluginManifest/master/manifest.json](https://raw.githubusercontent.com/danieladov/JellyfinPluginManifest/master/manifest.json)  
  
Using the "Plugins" -- "Catalogue" menu, add the following plugins to your Jellyfin instance:  
  

*   AniDB
*   AniList
*   Fanart
*   Merge Versions
*   Open Subtitles
*   Playback Reporting
*   Reports
*   Skin Manager
*   TMDb Box Sets
*   Tvmaze
*   TheTVDB

  
These plugins should already be installed by default:  
  

*   AudioDB
*   MusicBrainz - Installed by default
*   OMDb - Installed by default
*   Studio Images
*   TMDb

  
Now that all of the plugins have been installed, go to Docker / Portainer, select the Jellyfin container and restart it. Then come back to Jellyfin config.  
  
Open the hamburger menu in top left corner again and then select "Dashboard", go down the bottom of the menu and open "Plugins", and configure the following plugins:  
  

*   AniDB - Defaults
*   AniList - Defaults
*   Fanart - Add "Personal API Key" from your Fanart.tv account, and save.
*   Merge Versions - Defaults
*   Open Subtitles - Add Username / Password / API Key from your OpenSubtitles.com account, and save.
*   Playback Reporting - Defaults
*   Reports - Defaults
*   Skin Manager - Select a skin of your choosing, however further customisation is outside the scope of this guide.
*   TMDb - Include adult content (Optional), Import season name (Ticked), Max Cast Members (25), Image Scaling (Optional), and save.
*   TMDb Box Sets - Defaults
*   Tvmaze - Nil
*   TheTVDB - If there is no API Key pre-installed, you will need to register at [https://TheTVDB.com](https://thetvdb.com/) to obtain one.

  
"Playback" -- "Transcoding"  
Depending on the computer / NAS you are running Docker / Jellyfin, its possible to use hardware acceleration for transcoding - this configuration has been set up to map /dev/dri from the docker container to the host, so it will work, but will be dependent upon your personal hardware configuration. You will need to seek further advise from the Jellyfin community at Reddit / Discord / Youtube on settings for your hardware.  
  
Refer: [Hardware Acceleration | Jellyfin](https://jellyfin.org/docs/general/administration/hardware-acceleration/)  
DLNA (Digital Living Network Alliance): As this guide and configuration is built around a secure contained network for the entire media docker stack, the ports and services needed to support DLNA have not been mapped and exposed to the host network. The docker configuration can be customised to allow for DLNA, however it is outside the scope of this starter guide. So these settings won't work unless the docker-compose is reconfigured by yourself.  
  
"Libraries" -- "Display"  
Date added behavior for new content: change to "Use date scanned into library".  
  
"Libraries" -- "Metadata"  
Select your language and country prior to setting up libraries and importing metadata.  
  
  
\## Adding Movie Content  
"Libraries" -- "Libraries" and select "Add Media Library"  
Content Type: Movies  
Display Name: Movies  
Folders: Add - /data/media/movies  
Preferred Language: Personal Choice  
Country: Personal Choice, however it is linked to media ratings on IMDB, and will allow restrictions to children and other users depending on the content you have in the library.  
  
Enable real time monitoring: Ticked  
  
Order for Metadata Downloaders:  

*   TheMovieDB
*   The Open Movie Database
*   AniList
*   AniDB

Automatically refresh metadata from the internet: Never  
  
Order for Image Fetchers:  

*   Fanart
*   TheMovieDB
*   The Open Movie Database
*   AniList
*   AniDB
*   Embedded Image Extractor (should be first for dedicated libraries with home video recordings / personal media)
*   Screen Grabber (should be second for dedicated libraries with home video recordings / personal media)

Subtitle Downloads  

*   Language: Personal Choice
*   Subtitle Downloaders - Open Subtitles: Ticked (Disable for libraries with dedicated home video recordings / personal media)

  
NOTE: If you choose to use an adult movie library, use the same process as above to set up a new / separate adult library, so access to be restricted to certain user accounts.  
  
\## Adding Music Content  
"Libraries" -- "Libraries" and select "Add Media Library"  
Content Type: Music  
Display Name: Music  
Folders: Add - /data/media/music  
Preferred Language: Personal Choice  
Country: Personal Choice, however it is linked to media ratings on OMDB, and will allow restricting content to other users.  
  
Enable real time monitoring: Ticked  
  
Order for Metadata Downloaders (Artists):  

*     
    
*   MusicBrainz
*     
    
*   TheAudioDB

  
Order for Metadata Downloaders (Albums):  

*     
    
*   MusicBrainz
*     
    
*   TheAudioDB

  
Order for Image Fetchers (Artists):  

*     
    
*   Fanart
*     
    
*   TheAudioDB

  
Order for Image Fetchers (Albums):  

*     
    
*   Fanart
*     
    
*   TheAudioDB

  
Automatically refresh metadata from the internet: Never  
  
Order for Image Fetchers (Music Videos):  

*     
    
*   Fanart
*     
    
*   Embedded Image Extractor
*     
    
*   Screen Grabber

  
Save artwork into media folders: Ticked  
  
  
\## Adding TV Shows / Series Content  
"Libraries" -- "Libraries" and select "Add Media Library"  
Content Type: Shows  
Display Name: Series  
Folders: Add - /data/media/series  
Preferred Language: Personal Choice  
Country: Personal Choice, however it is linked to the media rating on IMDB,  
and will allow restrictions to children and other users depending on the categorisation you allow other users to access.  
  
Enable real time monitoring: Ticked  
  
Order for Metadata Downloaders (TV Shows):  

*     
    
*   TheTVDB
*     
    
*   Tvmaze
*     
    
*   AniList
*     
    
*   AniDB
*     
    
*   TheMovieDB
*     
    
*   The Open Movie Database
*     
    
*   Missing Episode Fetcher

  
Order for Metadata Downloaders (Seasons):  

*     
    
*   TheTVDB
*     
    
*   AniDB
*     
    
*   TheMovieDB

  
  
Order for Metadata Downloaders (Episodes):  

*     
    
*   TheTVDB
*     
    
*   Tvmaze
*     
    
*   AniDB
*     
    
*   TheMovieDB
*     
    
*   The Open Movie Database

  
Automatically refresh metadata from the internet: Never  
  
Order for Image Fetchers (TV Shows):  

*   Fanart
*   TVmaze
*   TheTVDB
*   AniDB
*   AniList
*   TheMovieDB

Order for Image Fetchers (Seasons):  

*   Fanart
*   TVmaze
*   TheTVDB
*   AniDB
*   AniList
*   TheMovieDB

  
Order for Image Fetchers (Episodes):  

*   TVmaze
*   TheTVDB
*   TheMovieDB
*   The Open Movie Database
*   Embedded Image Extractor
*   Screen Grabber

Subtitle Downloads  

*   Language: Personal Choice
*   Subtitle Downloaders - Open Subtitles: Ticked (Disable for libraries with dedicated home video recordings / personal media)

  
\## Adding Books Content  
"Libraries" -- "Libraries" and select "Add Media Library"  
Content Type: Books  
Display Name: Books  
Folders: Add - /data/media/books  
  
Enable real time monitoring: Ticked  
  
  
\## Adding Comic / Manga Content  
"Libraries" -- "Libraries" and select "Add Media Library"  
Content Type: Books  
Display Name: Comics  
Folders: Add - /data/media/comics  
  
Enable real time monitoring: Ticked  
  
  
\## Adding Photo Content  
"Libraries" -- "Libraries" and select "Add Media Library"  
Content Type: Photos  
Display Name: Photos  
Folders: Add - /data/media/photos  
  
Enable real time monitoring: Ticked  
  
Order for Image Fetchers (Videos):  

*   Embedded Image Extractor
*   Screen Grabber

  
  