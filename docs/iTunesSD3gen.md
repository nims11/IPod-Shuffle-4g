<h1 id="toc0"><a name="iTunesStats"></a>iTunesSD3gen</h1>
Here it is. The reason for this wiki. The third generation shuffle iTunesSD format.<br>
Just like in the iTunesDB the default size for integer numbers seems to be 32 bit. In earlier iTunesSD files it was a rather odd 24 bit.<br>
Like the iTunesDB new third generation shuffle's iTunesSD is little endian. Earlier iTunesSD files were big endian.<br>
<br>
Little endian means that the numbers start with the lowest byte. So a value of 0x12345678 (decimal 305419896) will be written in the iTunesSD file as 78 56 34 12.<br>
Apparently the apple developers liked to look at their files with a hex viewer to. At least they choose the magic numbers for their headers in a way that their ASCII representation tells you its purpose. So the database header starts with a magic number 0x73686462 (dec. 1936221282). Not an easy number to remember. But translating those bytes one by one into ASCII you get "s" "h" "d" "b", which to me looks like "shuffle database". The little endian storage format changes the byte order so that the first characters of the new iTunesSD are in fact "bdhs", but now you know how we came up with the names for those separate elements.<br>
<br>
Here's the general layout of an iTunesSD file:<br>
<ul><li><span style="color: #800000; font-family: 'Courier New',Courier,monospace;"><strong>bdhs</strong></span> Shuffle Database<ul><li><span style="color: #800000; font-family: 'Courier New',Courier,monospace;"><strong>hths</strong></span> Tracks Header<ul><li><span style="color: #800000; font-family: 'Courier New',Courier,monospace;"><strong>rths</strong></span> Track1</li><li><span style="color: #800000; font-family: 'Courier New',Courier,monospace;"><strong>rths</strong></span> Track2</li><li>...</li></ul></li><li><span style="color: #800000; font-family: 'Courier New',Courier,monospace;"><strong>hphs</strong></span> Playlists Header<ul><li><span style="color: #800000; font-family: 'Courier New',Courier,monospace;"><strong>lphs</strong></span> Playlist1</li><li><span style="color: #800000; font-family: 'Courier New',Courier,monospace;"><strong>lphs</strong></span> Playlist2</li><li>...</li></ul></li></ul></li></ul><br>
<h2 id="toc0"><a name="x-bdhs Shuffle Database"></a>bdhs Shuffle Database</h2>
 

<table class="wiki_table">
    <tbody><tr>
        <th><strong>Field</strong><br>
</th>
        <th><strong>Size</strong><br>
</th>
        <th>Description<br>
</th>
        <th><strong>Data</strong><br>
</th>
        <th><strong>Hexdump</strong><br>
</th>
    </tr>
    <tr>
        <td>header_id<br>
</td>
        <td>4<br>
</td>
        <td>Header<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">shdb</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">62 64 68 73</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_1<br>
</td>
        <td>4<br>
</td>
        <td>Version number?<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x03000002<br>
        Old values:<br>0x02010001<br>Gen 2:<br>0x010600<br>0x010800<br></span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">03 00 00 02</span><br>
</td>
    </tr>
    <tr>
        <td>header_length<br>
</td>
        <td>4<br>
</td>
        <td>size of this header<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">64</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">40 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>total_no_of_tracks<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">126</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">7e 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>total_no_of_playlists<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">10</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0a 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_2<br>
</td>
        <td>8<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000 0000 0000 0000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00 00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>max_volume<br>
</td>
        <td>1<br>
</td>
        <td>0x00 do not limit the volume<br>
0x03 is the min setting<br>
0x20 is the max setting<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00</span><br>
</td>
    </tr>
    <tr>
        <td>voiceover_enabled<br>
</td>
        <td>1<br>
</td>
        <td>Turns on any track voiceover feedback<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">1</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">01</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_3<br>
</td>
        <td>2<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00</span><br>
</td>
    </tr>
    <tr>
        <td>total_no_of_tracks2<br>
</td>
        <td>4<br>
</td>
        <td>Does not include podcasts or audiobooks in the count.<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">126</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">7e 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>track_header_chunk_offset<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00000040</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">40 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>playlist_header_chunk_offset<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000b964</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">64 b9 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_4<br>
</td>
        <td>20<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000 0000 0000 0000 0000</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 0000 0000 0000 0000 0000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00</span><br>
</td>
    </tr>
</tbody></table>

<br>
<h3 id="toc1"><a name="x-bdhs Shuffle Database-Tracks Header"></a>Tracks Header</h3>
 

<table class="wiki_table">
    <tbody><tr>
        <td><strong>Field</strong><br>
</td>
        <td><strong>Size</strong><br>
</td>
        <td><strong>Data</strong><br>
</td>
        <td><strong>Hexdump</strong><br>
</td>
    </tr>
    <tr>
        <td>header_id<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">shth</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">68 74 68 73</span><br>
</td>
    </tr>
    <tr>
        <td>total_length<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">524</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0c 02 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>number_of_tracks<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">126</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">7e 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_1<br>
</td>
        <td>8<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000 0000 0000 0000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00 00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>offset_of_track_chunk_0<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000024c</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">4c 02 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>offset_of_track_chunk_1<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x000003c0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">c0 03 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>offset_of_track_chunk_2<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00000534</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">34 05 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>offset_of_track_chunk_3<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x000006a8</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">a8 06 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>offset_of_track_chunk_4<br>
</td>
        <td>4<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000081c</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">1c 08 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>...<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">...</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">...</span><br>
</td>
    </tr>
</tbody></table>

<br>
<br>
<h3 id="toc2"><a name="x-bdhs Shuffle Database-TrackX"></a>TrackX</h3>
 <br>


<table class="wiki_table">
    <tbody><tr>
        <th><strong>Field</strong><br>
</th>
        <th><strong>Size</strong><br>
</th>
        <th><strong>Description</strong><br>
</th>
        <th><strong>Data</strong><br>
</th>
        <th><strong>Hexdump</strong><br>
</th>
    </tr>
    <tr>
        <td>header_id<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">shtr</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">72 74 68 73</span><br>
</td>
    </tr>
    <tr>
        <td>total_length<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">372</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">74 01 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>start_at_pos_ms<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>stop_at_pos_ms<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">112169</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">29 b6 01 00</span><br>
</td>
    </tr>
    <tr>
        <td>volume_gain<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00000000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>filetype<br>
</td>
        <td>4<br>
</td>
        <td>Type 1 are mpeg, mp3 files<br>
Type 2 arere aac, mp4, m4a files<br>
Type 4 are wav files<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">1 (MP3)</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">01 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>filename<br>
</td>
        <td>256<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">/iPod_Control/Music/F02/NNCN.mp3</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">2f 69 50 6f 64 5f 43 6f 6e 74 72 6f 6c 2f 4d 75</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 73 69 63 2f 46 30 32 2f 4e 4e 43 4e 2e 6d 70 33</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>Bookmark<br>
</td>
        <td>4<br>
</td>
        <td>In milliseconds<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00000000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>dont_skip_on_shuffle<br>
</td>
        <td>1<br>
</td>
        <td>If all songs in a playlist don't have this bit set the playlist is skipped when the ipod is set to shuffle and a playlist is being chosen.<br>
It seems to be ignored when shuffling within a playlist!<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">1</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">01</span><br>
</td>
    </tr>
    <tr>
        <td>remember_playing_pos<br>
</td>
        <td>1<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00</span><br>
</td>
    </tr>
    <tr>
        <td>part_of_uninterruptable_album<br>
</td>
        <td>1<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_1<br>
</td>
        <td>1<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00</span><br>
</td>
    </tr>
    <tr>
        <td>pregap<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x240 = 576</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">40 02 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>postgap<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0xc9c= 3228</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">9c 0c 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>number_of_samples<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x4b6c24 = 4942884</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">24 6c 4b 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_file_related_data1<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>gapless_data<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x24a2a2 = 2400930</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">a2 a2 24 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_file_related_data2<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>Album ID<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000007f</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">7f 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>track_number<br>
</td>
        <td>2<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">1</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">01 00</span><br>
</td>
    </tr>
    <tr>
        <td>disc_number<br>
</td>
        <td>2<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_2<br>
</td>
        <td>8<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000 0000 0000 0000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00 00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>dbid<br>
</td>
        <td>8<br>
</td>
        <td>Serves as the filename for the voiceover<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0xdfa209b7ce6f2db9</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">b9 2d 6f ce b7 09 a2 df</span><br>
</td>
    </tr>
    <tr>
        <td>Artist ID<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00000146</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">46 01 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_3<br>
</td>
        <td>32<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x0000 0000 0000 0000 0000 0000 0000 0000</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 0000 0000 0000 0000 0000 0000 0000 0000</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
<span style="font-family: 'Courier New',Courier,monospace;"> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
</td>
    </tr>
</tbody></table>

<br>
<h3 id="toc3"><a name="x-bdhs Shuffle Database-Playlist Header"></a>Playlist Header</h3>
 <br>


<table class="wiki_table">
    <tbody><tr>
        <th><strong>Field</strong><br>
</th>
        <th><strong>Size</strong><br>
</th>
        <th><strong>Description</strong><br>
</th>
        <th><strong>Data</strong><br>
</th>
        <th><strong>Hexdump</strong><br>
</th>
    </tr>
    <tr>
        <td>header_id<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">shph</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">68 70 68 73</span><br>
</td>
    </tr>
    <tr>
        <td>total_length<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">20 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>number_of_playlists<br>
</td>
        <td>4?<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">3</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">03 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>number_of_playlists_1<br>
</td>
        <td>2<br>
</td>
        <td>The number of non-podcast playlists, 0xffff if all playlists are not podcast playlists.<br>
</td>
        <td>0xffff<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">ff ff </span><br>
</td>
    </tr>
    <tr>
        <td>number_of_playlists_2<br>
</td>
        <td>2<br>
</td>
        <td>The number of master playlists, 0xffff if all playlists are not master playlists.<br>
</td>
        <td>0x0100<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">01 00</span><br>
</td>
    </tr>
    <tr>
        <td>number_of_playlists_3<br>
</td>
        <td>2<br>
</td>
        <td>The number of non-audiobook playlists, 0xffff if all playlists are not audiobook playlists.<br>
</td>
        <td>0xffff<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">ff ff</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_2<br>
</td>
        <td>2<br>
</td>
        <td><br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00</span><br>
</td>
    </tr>
    <tr>
        <td>offset_of_playlist_1<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00015b14</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">14 5b 01 00</span><br>
</td>
    </tr>
    <tr>
        <td>offset_of_playlist_2<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x00015ef0</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">f0 5e 01 00</span><br>
</td>
    </tr>
    <tr>
        <td>...<br>
</td>
        <td><br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">...</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">...</span><br>
</td>
    </tr>
</tbody></table>

<br>
<h3 id="toc4"><a name="x-bdhs Shuffle Database-PlaylistX"></a>PlaylistX</h3>
 <br>


<table class="wiki_table">
    <tbody><tr>
        <th><strong>Field</strong><br>
</th>
        <th><strong>Size</strong><br>
</th>
        <th><strong>Description</strong><br>
</th>
        <th><strong>Data</strong><br>
</th>
        <th><strong>Hexdump</strong><br>
</th>
    </tr>
    <tr>
        <td>header_id<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">shpl</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">6c 70 68 73</span><br>
</td>
    </tr>
    <tr>
        <td>total_length<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">dc 03 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>number_of_songs<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">236</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">ec 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>number_of_songs2<br>
</td>
        <td>4<br>
</td>
        <td>Number of non podcast or audiobook songs.<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">236</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">ec 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>dbid<br>
</td>
        <td>8<br>
</td>
        <td>Serves as the filename for the voiceover<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">6bed</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">48 4d 19 eb 4e 34 ed 6b</span><br>
</td>
    </tr>
    <tr>
        <td>type<br>
</td>
        <td>4<br>
</td>
        <td>1 is the master playlist<br>
2 is a normal playlist<br>
3 is a podcast playlist<br>
4 is a audiobook playlist<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">2</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">02 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>unknown_1<br>
</td>
        <td>16<br>
</td>
        <td><br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>playlist_track_1<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">118</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">76 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>playlist_track_2<br>
</td>
        <td>4<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">119</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">77 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>...<br>
</td>
        <td><br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">...</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">...</span><br>
</td>
    </tr>
</tbody></table>

A dbid of all zeros yields a voiceover of All songs. Also playlist dbids without a corresponding voiceover file will yield a voiceover of playlist n or audiobook n where n is the playlist number. The shuffle assumes the podcast playlist is last.<br>
<br>
The <a class="wiki_link" href="iTunesStats3gen.md">iTunesStats</a> file is also different in the 3gen iPod.
<p>Original Source: <a href="http://shuffle3db.wikispaces.com/iTunesSD3gen">http://shuffle3db.wikispaces.com/iTunesSD3gen</a> (expired)</p>
  </div>
