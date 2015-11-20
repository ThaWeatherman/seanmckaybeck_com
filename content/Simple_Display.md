Title: Simple Display
Date: 2015-03-02 03:21
Tags: electronics, raspberry-pi
Summary: Displaying pictures and words on an LED matrix!

I made a basic setup that displays the current price of silver per ounce.

###### Materials
* 1 Raspberry Pi model B
* [1 16x32 display from Adafruit](https://www.adafruit.com/products/420)
* 13 female/female jumper wires
* [1 5V 2A DC power supply](https://www.adafruit.com/products/276)
* [1 female DC power adapter](https://www.adafruit.com/products/368)

I used the Arch Linux image for the Raspberry Pi's operating system. Follow [this](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/wiring-the-display) guide for wiring the display to the Pi. Once you have the operating system set up you need the proper software. Use [this](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/testing) guide for installing the necessary software for the display. In order to work with my code you need Python 3.4 and you need `libfreetype` installed. On Arch you can install it with `pacman -S freetype2`. You will also need `Pillow` which can be installed with `pip install pillow`. Make sure you install `libfreetype` before `pillow`. The font used in the code is also based on the path on Arch.

###### The Code

Note that this must be saved and run from within the install directory of the matrix code. Every ten minutes it will grab the current price per ounce of silver, create a `ppm` image in the specified font, then display it as a scrolling message on the LED matrix.

<script src="https://gist.github.com/ThaWeatherman/08a4bac104601e8e3fb1.js"></script>

Note that a good chunk of this (the display code) was taken from the Adafruit tutorial.

###### The Result
I can't get the Imgur gifv or Gfycat images to embed properly here so below are the links (higher quality is better!).

http://gfycat.com/GrotesqueImpishDrafthorse
http://i.imgur.com/vXqUxLG.gifv
