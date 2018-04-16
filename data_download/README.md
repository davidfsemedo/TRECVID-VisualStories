# TRECVID-Social-media Video Storytelling Linking
TRECVID 2018 - Social-media Video Storytelling Linking Development Kit


Bash scripts to download data.

## Images

The dataset contains four files of the form *_image-urls.out, one for each event, with and without spam content. 
These files contain a command call to wget for each image.                      

To download images run the following command:                                                                                                                                           

```console
foo@bar:~$ cat visualstories_edfest_2017_nospam_twitter_image-urls.out  | xargs -I {} sh -c {}                                                                                          
```

The filename of each image will the Tweet ID of the corresponding image. You can download images in parallel by passing the option `-P <number processes>` to xargs.



## Videos
Videos are hosted in multiple source platforms (e.g. Youtube, Twitter, Vimeo, etc.).
To this end, we can use the `youtube-dl` tool which supports most platforms.

Pre-requisites:
* youtube-dl tool [Link](https://rg3.github.io/youtube-dl/download.html)

The dataset contains four files of the form *_video-urls.out, one for each event, with and without spam content. 
These files contain a command call to youtube-dl for each video.

To download videos run the following command:

```console
foo@bar:~$ cat visualstories_edfest_2017_nospam_twitter_video-urls.out  | xargs -I {} sh -c {}
```

The filename of each video will be the Tweet ID of the corresponding video.
NOTE: We do not recommend downloading videos in parallel with youtube-dl.


---
##### Contact:

If you have any question regarding the dataset, please contact:
David Semedo - Email: df.semedo@campus.fct.unl.pt

The NOVASEARCH Team.
