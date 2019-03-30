# Hacky Easter 2019 Solution

After a bit of quick discussion on our Slack channel, one member (bruton.gaster) had the thought of each frame of the video being a single pixel of an image. We calculated that there were 230,400 total frames in the video. That would be exactly enough pixels for a 480px x 480px image (480 x 480 = 230,400).

Using **ffmpeg**, we were able to export each frame into it's individual PNG files using the following command:

``
ffmpeg -i he2019_teaser.mp4 image-%08d.png
``

From that point, we had a few different approaches to stitching the frames into a complete image.

- mothersuperior : egg-builder.py
  - Uses the PIL library in Python to read the RGB value of each image then sets the corresponding pixel on a new image to that color. At the end, it outputs a file called "out-egg.png"
