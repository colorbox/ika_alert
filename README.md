# ika_alert

This soft watch icons and alert you for numerical advantage or disadvantage.

## USAGE

![Usage](sample.gif)

### SETUP

At first connect capture board to your mac or something, and execute command below.

```
python3 ./image_from_camera_try.py
```

And you will get alert like sample.

![Usage](sample.gif)

It alerts you when you get numerical advantage/disadvantage with green/red image.

## Create your own learned data

### place captured movies 

Save your splatoon2 battle movie under `data/movies`.

### slice movie into images
make slice movie with ffmpeg

```
ffmpeg -i ./data/movies/XXX.mp4  -r 1 -f image2 ./data/sliced_movies/XXX/%06d.jpg
```

### pretreatment with your hand
remove some images from your sliced images like below.

 - looking map
 - pinch mode
 - before start battle and after end battle

### trim icons

Trim icons from sliced image with below command.

```
ruby ./ika_triming.rb data/sliced_movies/XXX
```

After that there are icon images in `data/icons/XXX` dir.

### clustering icons

Let's classify with k-means. 

```
python ./ika_k-means.py
```

After classification clustered icons distributed into `data/grouped_icons`.
They may be clustered as below.
 - enemy team
 - friendly team
 - dead
 - special
 

### generate learned model

You can generate learned data with below command.
```
python3 ./create_svm_classifyier.py
```

And alsp, you can test your model with below command.

```
python3 ./test_created_svm_machine.py
```
