# TRECVID-Social-media Video Storytelling Linking
TRECVID 2018 - Social-media Video Storytelling Linking Development Kit


Bash scripts to download data.

**NOTE**: All *.out files can be found in the folder "data_download/".

## Tweets and users
The dataset contains four files of the form *_twitter_tweets.out (Tweet ids), and four files of the form *_twitter_users.out" (User ids), one for each event. Each file consists of a list of ids, one per line.
To obtain the tweets and user metadata, you have to use the Twitter API. To keep it straightforward, we suggest the use of a Twitter API Wrapper. The Python [TWARC](https://github.com/DocNow/twarc) command-line tool can be used for this purpose. Namely, check methods `hydrate` and `users` of TWARC. 


## Images

The dataset contains four files of the form *_image-urls.out, one for each event, with and without spam content. 
These files contain a command call to wget for each image.                      

To download images run the following command:                                                                                                                                           

```console
foo@bar:~$ cat visualstories_edfest_2017_twitter_nospam_image-urls.out  | xargs -I {} sh -c {}                                                                                          
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
foo@bar:~$ cat visualstories_edfest_2017_twitter_nospam_video-urls.out  | xargs -I {} sh -c {}
```

The filename of each video will be the Tweet ID of the corresponding video.
NOTE: We do not recommend downloading videos in parallel with youtube-dl.


---
##### Contact:

If you have any question or if you find any issue, please contact:
David Semedo - Email: df.semedo@campus.fct.unl.pt

The NOVASEARCH Team.
