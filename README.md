# WRS_classifier

The Model to classify the two classes, one is correctly assembled and other one has not the motor pulley.
Firstly, I made a simulation environment using Blender.
- The difference of between them is the existence of the motor pulley
And it is exported and then used with Rasmus's synth-ml randomization tool.

1. Camera information: focal length 8.5mm, sensor width size 9.2mm
2. The motor pully is located on the motor, and it has some range, -1 mm < x < +1 mm.

Training samples: 1200 wrs images with motor pulley, 1200 wrs images without motor pulley
1200 samples: 600 images with noise + 600 images without noise

MobileNet will be used to classify.

0302: 0.6K datasets
0303: 2K datasets
0305: 5K datasets


To do
- Generating much more datasets
- Customizing mobilenet
- Hyper parameter optimization (maybe Bayesian)
- Classifying unseen image