# WRS_classifier

The Model to classify the two classes, one is correctly assembled and other one has not the motor pulley.
Firstly, I made a simulation environment using Blender.

Modified conditions
1. Camera information: focal length, sensor width size
2. Existence of the motor pulley

Training samples: 1200 wrs images with motor pulley, 1200 wrs images without motor pulley
1200 samples: 600 images with noise + 600 images without noise

MobileNet will be used to classify, and this is going to be the localization.