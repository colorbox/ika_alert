# ika_alert

## USAGE 

### place captured movies 

Save your splatoon2 battle movie under 'data/movies'.

### slice movie into images
make slice movie with ffmpeg
'''
ffmpeg -i ./data/movies/XXX.mp4  -r 1 -f image2 ./data/sliced_movies/XXX/%06d.jpg
'''

### pretreatment with your hand
remove some images from your sliced images like below
 
 - looking map
 - pinch mode
 - before start battle and after end battle

### trim icons

trim icons from sliced image with below command

```
ruby ./ika_triming.rb data/sliced_movies/XXX
```

After that there are icon images in `data/icons/XXX` dir.
