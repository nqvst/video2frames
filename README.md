# A simple video to images extraction tool

```sh
$ git clone git@github.com:nqvst/video2frames.git && cd video2framse
$ pipenv install 
$ pipenv shell

# extract every 9th frame starting at frame 32 end stopping at frame 64 
$ python extract_frames.py -f video.mp4 -r 9 -o output_frames -s 32 -e 64 

```
## options
```sh
options:
    -h --help               show this help message and exit
    -f --file               the name of the video to extract.
    -r --framereduction     how many frames should be skipped between captures.
    -o --output             output folder name
    -s --start              start from a specific frame
    -e --end                stop at a specific frame
```
