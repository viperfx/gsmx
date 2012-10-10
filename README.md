gsmx
====

A quick env to convert a mix on designers.mx to grooveshark using scrapy and Tinysong API

Usage
====
`python get_id.py`

Edit `url` in get_id.py variable to get ID's working for a different playlist.
Edit grooveshark.py to add your KEY and SECRET provided to you by grooveshark
Edit get_id.py line 14 to add your own username and password for grooveshark so it can add playlists to your own account.

TODO
====
* To use the grooveshark api to create playlists for any account when logged in using OAuth
* To generalise the script a bit more so that it can be done with any spotify playlist on the web, not just designers.mx

Sample Output
====
from `cat playlist_futureMe_f-a-l-l_1728.json | python -mjson.tool`
```
{
    "AlbumID": 7161817,
    "AlbumName": "Kill for Love",
    "ArtistID": 20984,
    "ArtistName": "Chromatics",
    "SongID": 33463149,
    "SongName": "Kill For Love",
    "Url": "http://tinysong.com/MW2S"
}{
    "AlbumID": 1264393,
    "AlbumName": "Pet Grief",
    "ArtistID": 404316,
    "ArtistName": "The Radio Dept.",
    "SongID": 35362351,
    "SongName": "I Wanted You to Feel the Same",
    "Url": "http://tinysong.com/10VYn"
}{
    "AlbumID": 4380400,
    "AlbumName": "In Evening Air",
    "ArtistID": 698851,
    "ArtistName": "Future Islands",
    "SongID": 25822722,
    "SongName": "Inch Of Dust",
    "Url": "http://tinysong.com/HF8P"
}{
    "AlbumID": 6141745,
    "AlbumName": "Within and Without",
    "ArtistID": 1187703,
    "ArtistName": "Washed Out",
    "SongID": 31337051,
    "SongName": "Soft",
    "Url": "http://tinysong.com/HOgN"
}{
    "AlbumID": 6623112,
    "AlbumName": "Last Night (Original Motion Picture Soundtrack)",
    "ArtistID": 404087,
    "ArtistName": "Bat for Lashes",
    "SongID": 31786679,
    "SongName": "Daniel",
    "Url": "http://tinysong.com/Of6h"
}{
    "AlbumID": 7809227,
    "AlbumName": "Mixed Emotions///eastvillageclub.tumblr.com",
    "ArtistID": 1159528,
    "ArtistName": "Tanlines",
    "SongID": 35530078,
    "SongName": "Abby",
    "Url": "http://tinysong.com/13SLK"
}{
    "AlbumID": 3359329,
    "AlbumName": "Movement (Collector's Edition)",
    "ArtistID": 595,
    "ArtistName": "New Order",
    "SongID": 25940369,
    "SongName": "Ceremony [Alternate 12\" Version]",
    "Url": "http://tinysong.com/vT9L"
}{
    "AlbumID": 7573719,
    "AlbumName": "Passage",
    "ArtistID": 1667162,
    "ArtistName": "Exitmusic",
    "SongID": 36236530,
    "SongName": "The Sea",
    "Url": "http://tinysong.com/17A1g"
}{
    "AlbumID": 2784856,
    "AlbumName": "The Warning",
    "ArtistID": 3821,
    "ArtistName": "Hot Chip",
    "SongID": 9015011,
    "SongName": "So Glad to See You",
    "Url": "http://tinysong.com/iD7O"
}{
    "AlbumID": 7323507,
    "AlbumName": "We All Shine",
    "ArtistID": 1462940,
    "ArtistName": "Team Ghost",
    "SongID": 33940368,
    "SongName": "A Glorious Time",
    "Url": "http://tinysong.com/14BBv"
}
```