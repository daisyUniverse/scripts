# clipdl

Download everything from your clipboard

![](clipdlg.gif)

### How to use:

**Step 1.** Copy a link to something you want to download. Supported links are:

- Direct image links: .png, .jpg, .jpeg, .gif
- Twitter: Full tweet url for video, direct image links work too
- Youtube: Full length url to download audio (mp3) or shortlink for Video
- Soundcloud
- Github

**Step 2**. run `./clipdl '[dir you want your downloads to go]'`

Options:
 `-e` to open the file in an editor that is best for the downloaded file 
 ( Gimp for Images, Audacity for Audio, kdenlive for Videos, Opens Dir in Konsole for Github repos )

 `-o` to open the file in a viewer best for the file type 
 ( gthumb for Images, vlc for Audio and Video, Opens Dir in file browser for Github repos )

( You need to be in the same directory as the script for this to work )
( the specific programs used for each type of file can be changed in lines 20-40 of the script )

( made with the intention of binding it to a hotkey on my mouse )


### Requirements:

[**youtube-dl**, **notify-osd**, **wget**, **xclip**]