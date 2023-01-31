# Preparing Your Media Library


!!! Danger "Warning: &nbsp; &nbsp; &nbsp; Page Under Development"

    This page is still under development and may not have accurate information, and should be considered incomplete / inaccurate until this notice is removed.


## Prepare / rename media library if needed:
If you are setting up your media server and media libraries for the very first time, or your media is very poorly named, it is recommended you use Filebot with the following naming standards below, to initially sort all of your media. Otherwise the Media Library Managers and Jellyfin may not be able to identify your media titles, media art, and subtitles, if the original filenames are of a poor standard.

Change =="D:/Storage"== to suit your needs, however use the same disk as the original media, so it is renamed quickly in place, rather than copied to a different disk or network; this could take a great deal of time to complete depending on size of the libraries / media you are renaming.

>This can be skipped if you have a well organised / structured media library already.

## Filebot Renaming Preset String for Series / TV Shows

``` powershell
D:/Storage/renamed/series/{ny.colon(' - ').ascii()} [tmdbid-{id}]/Season {s00}/{ny.colon(' - ').ascii()} {s00e00} - {t.ascii()} {" - $hd $vf $vc $ac"}
```

## Filebot Renaming Preset String for Movies / Adult

``` powershell
D:/Storage/renamed/movies/{ny.colon(' - ').ascii()} [imdbid-{imdbid}]/{ny.colon(' - ').ascii()} {" - $hd $vf $vc $ac"}
```

## Filebot Renaming Preset String for Music / Audio

``` powershell
D:/Storage/renamed/music/{artist.upperInitial().ascii()}/{album.upperInitial().ascii()} ({y})/{albumArtist.upperInitial().ascii()} - {album.upperInitial().ascii()} - {pi.pad(3)+' - '} {t.ascii()}
```
