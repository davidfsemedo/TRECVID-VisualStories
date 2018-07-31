# TRECVID-Social-media Video Storytelling Linking
TRECVID 2018 - Social-media Video Storytelling Linking Development Kit

Bash scripts to download data.

**NOTE**: All *.out files can be found in the folder "data_download/".

## Option 1 - Download using the provided script
We provide a bash script (```download.sh```) to download videos, images and Tweets metadata. 

#### Pre-requisites
The script was tested on Linux (Ubuntu and CentOS). Windows users should be able to run the script using Linux Bash Shell.

First, make the script executable:
```console
foo@bar:~$ chmod +x download.sh 
```
Install the following tools:
* youtube-dl - [Link](https://rg3.github.io/youtube-dl/download.html)
* TWARC - [Link](https://github.com/DocNow/twarc)

We recommend the use of pip to install both tools:
```console
foo@bar:~$ pip install youtube_dl
foo@bar:~$ pip install twarc
```

The version 1.4.6 of TWARC was used (pip install twarc==1.4.6). TWARC is a Twitter API Wrapper. Before using TWARC you will need to register an application at [apps.twitter.com](https://apps.twitter.com/). Once you've created your application, generate an access token and access token secret. Setup TWARC with the generated token:
```console
foo@bar:~$ twarc configure
```
More detailed instructions on how to configure TWARC can be found in the TWARC [repository](https://github.com/DocNow/twarc).

#### Downloading data
The (```download.sh```) script automatically downloads videos, images and tweets metadata, for each event. Videos, images and metadata are stored each in a separate folder, per event. 
You can check which options ara available with:
```console
foo@bar:~$ ./download.sh --help
Event data download tool.
Usage: ./download.sh [-e|--event <arg>] [-s|--(no-)with_spam] [--(no-)only_images] [--(no-)only_videos] [--(no-)only_tweets] [--(no-)only_users] [-d|--data_prefix <arg>] [-h|--help]
	-e,--event: Event name (e.g. edfest2016) (no default)
	-s,--with_spam,--no-with_spam: boolean optional argument help msg (off by default)
	--only_images,--no-only_images: Download only images (off by default)
	--only_videos,--no-only_videos: Download only videos (off by default)
	--only_tweets,--no-only_tweets: Download only Tweets' metadata (off by default)
	--only_users,--no-only_users: Download only Tweet Users metadata (off by default)
	-d,--data_prefix: URLs data prefix path. (default: '.')
	-h,--help: Prints help
```

The tool takes as input the target event. Available events are: ```edfest_2016, tdf_2016, edfest_2017, tdf_2017```. Thus, to download content from each event, just pass the event prefix as argument:
```console
foo@bar:~$ ./download.sh --event edfest_2016 --data_prefix=<path_to_data_download_lists>
foo@bar:~$ ./download.sh --event edfest_2017 --data_prefix=<path_to_data_download_lists>
foo@bar:~$ ./download.sh --event tdf_2016 --data_prefix=<path_to_data_download_lists>
foo@bar:~$ ./download.sh --event tdf_2017 --data_prefix=<path_to_data_download_lists>
```
The data_prefix option should receive the path of the folder with all the *.out files. The tool will create 3 different folders for each event: edfest_2017_videos, edfest_2017_images, edfest_2017_tweets_metadata, etc.

**NOTE**: We advise you to run the download script for each event more than once, to ensure that all content that is available is downloaded. Videos and Images already downloaded are skipped.

##### Additional options
You can opt to download only images, videos, tweets metadata or users metadata using the options --only_images, --only_videos, --only_tweets and only_users, respectively.

Additionally, you can download ALL content (including content marked as SPAM) by passing the option --with_spam. Note that spam detection was done *automatically* and there may be some false negatives and false positives.

#### Content format

The filename of each image and video will be the Tweet ID of the corresponding image/video. For some videos, youtube-dl will add the video extension.

Tweets and user metadata files, tweets.jsonl and users.jsonl, respectively, consist of a json lines file, with a json per line. These will be stored in the folder ```<event_prefix>_tweets_metadata```. For a complete description of each json line, check the Twitter REST API documentation [Link](https://developer.twitter.com/en/docs).

#### Issues

A list of videos and images for which the download failed (file failed.out) will be created in the corresponding folders. Note that some images/videos may no longer be available.

In case you encounter any errors you can check the logs for the problem. The tool will write logs to each type of content folder (videos, images and metadata folders). Feel free to contact us if you need any help/clarification.

## Option 2 - Alternative Method (Old)

### Tweets and users
The dataset contains four files of the form *_twitter_tweets.out (Tweet ids), and four files of the form *_twitter_users.out" (User ids), one for each event. Each file consists of a list of ids, one per line.
To obtain the tweets and user metadata, you have to use the Twitter API. To keep it straightforward, we suggest the use of a Twitter API Wrapper. The Python [TWARC](https://github.com/DocNow/twarc) command-line tool can be used for this purpose. Namely, check methods `hydrate` and `users` of TWARC. 


### Images

The dataset contains four files of the form *_image-urls.out, one for each event, with and without spam content. 
These files contain a command call to wget for each image.                      

To download images run the following command:                                                                                                                                           

```console
foo@bar:~$ cat visualstories_edfest_2017_twitter_nospam_image-urls.out  | xargs -I {} sh -c {}                                                                                          
```

The filename of each image will the Tweet ID of the corresponding image. You can download images in parallel by passing the option `-P <number processes>` to xargs.



### Videos
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

If you have any question regarding the dataset, please contact:
David Semedo - Email: df.semedo@campus.fct.unl.pt

The NOVASEARCH Team.