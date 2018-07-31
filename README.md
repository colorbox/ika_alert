# ika_alert


## USAGE 

read this
https://www.tensorflow.org/hub/tutorials/image_retraining

After train data, in this directory.

```
mv /tmp/output_graph.pb ./
mv /tmp/output_labels.txt ./
```

you can recognize images like below.
```
python label_image.py --graph=./output_graph.pb --labels=./output_labels.txt --input_layer=Placeholder --output_layer=final_result --image=./../ika_icons/special/000209-2.jpg
```
image option take icon image.
