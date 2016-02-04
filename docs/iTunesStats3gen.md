<h1 id="toc0"><a name="iTunesStats"></a>iTunesStats</h1>
<br>
The <span style="font-family: 'Courier New',Courier,monospace;">iTunesStats</span> file contains information about the usage of your iPod. It will be synced back to iTunes to update its stats regarding the playing and skipping of songs.<br>
<br>
Here's the general layout of an iTunesSD file:<br>
<ul><li>Header<ul><li>Track 1 Stats</li><li>Track 2 Stats</li><li>...</li></ul></li></ul><br>
<strong>Header</strong><br>


<table class="wiki_table">
    <tbody><tr>
        <td><strong>Field</strong><br>
</td>
        <td><strong>Data</strong><br>
</td>
        <td><strong>Hexdump</strong><br>
</td>
    </tr>
    <tr>
        <td>Number of Songs<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">236</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">EC 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>Unknown<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br>
</td>
    </tr>
</tbody></table>

<br>
<strong>Track X Stats</strong><br>


<table class="wiki_table">
    <tbody><tr>
        <td><strong>Field</strong><br>
</td>
        <td><strong>Data</strong><br>
</td>
        <td><strong>Hexdump</strong><br>
</td>
    </tr>
    <tr>
        <td>Length of Entry<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">32</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">20 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>Bookmark Time<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x000AF1AA</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">AA F1 0A 00</span><br>
</td>
    </tr>
    <tr>
        <td>Play Count<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">1</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">01 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>Time of last Play<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0x7C4CE6C7</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">7C 4C E6 C7</span><br>
</td>
    </tr>
    <tr>
        <td>Skip Count<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">1</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">01 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>Time of last Skip<br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">0xBA4DE6C7</span><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">BA 4D E6 C7</span><br>
</td>
    </tr>
    <tr>
        <td>Unknown 1<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br>
</td>
    </tr>
    <tr>
        <td>Unknown 2<br>
</td>
        <td><br>
</td>
        <td><span style="font-family: 'Courier New',Courier,monospace;">00 00 00 00</span><br />
        </td>
    </tr>
    </table>
<p>Original Source: <a href="http://shuffle3db.wikispaces.com/iTunesSD3gen">http://shuffle3db.wikispaces.com/iTunesStats3gen</a> (expired)</p>
