# Preparing Your New Media Library

In order for your *ARR Media Library Managers and Jellyfin applications to effectively identify the correct titles and meta data for all of your media, its important you follow the recommended file naming conventions for these applications.

The best way to set up your media library, is to allow the *ARR Media Library Managers to be able to add / remove / change all of the file and folder names based on each title (using the Jellyfin formats), then Jellyfin will be able to easily identify each media object and fetch the relevant meta data and artwork.

The *ARR Media Library Managers already do an excellent job of identifying and renaming media files and folders, however, if you are setting up your media libraries for the first time and your current media files are poorly named, it is recommended to use FileBot to scan and rename everything initially and then import the newly organised media files and folders into the *ARR Library Managers, so they can then continue to manager your media.

!!! Tip "Tip: &nbsp; &nbsp; &nbsp; This Section Is Only For New Media Libraries"

    The following steps


!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.


## Prepare / rename media library if needed:
If you are setting up your media server and media libraries for the very first time, or your media is very poorly named, it is recommended you use Filebot with the following naming standards below, to initially sort all of your media. Otherwise the Media Library Managers and Jellyfin may not be able to identify your media titles, media art, and subtitles, if the original filenames are of a poor standard.

Change =="D:/Storage"== to suit your needs, however use the same disk as the original media, so it is renamed quickly in place, rather than copied to a different disk or network; this could take a great deal of time to complete depending on size of the libraries / media you are renaming.

>This can be skipped if you have a well organised / structured media library already.

### Filebot Renaming Preset String for Series / TV Shows

``` powershell
D:/Storage/renamed/series/{ny.colon(' - ').ascii()} [tmdbid-{id}]/Season {s00}/{ny.colon(' - ').ascii()} {s00e00} - {t.ascii()} {" - $hd $vf $vc $ac"}
```

### Filebot Renaming Preset String for Movies / Adult

``` powershell
D:/Storage/renamed/movies/{ny.colon(' - ').ascii()} [imdbid-{imdbid}]/{ny.colon(' - ').ascii()} {" - $hd $vf $vc $ac"}
```

### Filebot Renaming Preset String for Music / Audio

``` powershell
D:/Storage/renamed/music/{artist.upperInitial().ascii()}/{album.upperInitial().ascii()} ({y})/{albumArtist.upperInitial().ascii()} - {album.upperInitial().ascii()} - {pi.pad(3)+' - '} {t.ascii()}
```
