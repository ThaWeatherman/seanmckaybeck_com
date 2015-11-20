Title: Motion Detection for Home Security
Date: 2015-02-12 01:06
Tags: security, arduino, electronics
Summary: Cheap motion detection with Arduino

Have you ever wanted a security system to know when someone breaks into your home? Those systems are so expensive though and buying one is not as fun as making your own. Using an Arduino and a PIR sensor I was able to make my own intruder detection system. 

## Intro
The Arduino is a great platform for small or large electronics projects. It is fairly easy to learn and there are tons of libraries already written to make coding for it simpler. This project utilizes the Arduino and a PIR sensor to make a intruder detection system that emails you when motion is detected.

## Parts
The following is a list of the parts I used to complete this project. Note that soldering is required to put the CC3000 shield together. Adafruit has a [guide](https://learn.adafruit.com/adafruit-cc3000-wifi/cc3000-shield) on how to take care of that. You will also need to update the firmware of the CC3000.

Some of the links below will take you to Radio Shack. If you can, go pick those up ASAP as Radio Shack is selling half of its stores so discounts are substantial. 

* [6 male-to-male wires](https://www.adafruit.com/products/758)
* [1 mini-breadboard](https://www.radioshack.com/modular-ic-breadboard-socket/2760003.html)
* [1 LED](http://www.vetco.net/catalog/product_info.php?products_id=9942&gclid=CMPO3JWL2MMCFdgHgQodTYAA2A)
* [1 Arduino Uno R3](https://www.adafruit.com/product/50)
* [1 Adafruit CC3000 shield](https://www.adafruit.com/product/1491)
* [1 PIR sensor](https://www.radioshack.com/radioshack-passive-infrared-sensor/2760347.html)

You will need the Arduino IDE installed on your computer. You can download it for your system from [here](http://arduino.cc/en/Main/Software). Make sure to download version 1.0.6 as the CC3000 does not get along so well with 1.6.0.  Also note that there are some other things required to complete the install. Use [this](http://arduino.cc/en/Guide/HomePage) as a reference.

Finally the code for this project uses code from Temboo. Temboo makes working with the Arduino easier. Go create an account at https://www.temboo.com. I then used the code found [here](https://www.temboo.com/library/Library/Google/Gmail/SendEmail/) to handle the emailing functionality.

## Wiring
I did my best to get some pictures of the wiring which you can see below. 
![](/content/images/2015/02/above.jpg)
![](/content/images/2015/02/side.jpg)
![](/content/images/2015/02/arduino.jpg)

Plug your PIR sensor into the breadboard. It does not really matter where but it was easier to clump everything together on the end for me. Notice in the following picture of the PIR sensor from left to right the pins are GND, VCC, and OUT. 

![](/content/images/2015/02/PIR.jpg)

Based on where you plug in your sensor you can now use the following diagram to do the wiring. I apologize that my Paint skills are not the best. Please note that the purple wire in the drawing is the white wire in the above pictures. Also note that the short end of the LED is on the left in the diagram even though it looks like the short end is the right (again, crappy Paint skills). 

![](/content/images/2015/02/diagram.jpg)

## Code
The code is MIT licensed so feel free to use it and modify it. Make sure to fill in the necessary values for your wireless connection and your Temboo app profile.

<script src="https://gist.github.com/ThaWeatherman/234dfab2bfd13487d11b.js"></script>

## Working product
You should now have a fully working product. The LED is there to let you know quickly that the circuitry and code is all good. If it lights up when you move in front of the sensor then you are good to go!

<iframe width="1280" height="720" src="https://www.youtube.com/embed/LahtYaoWLso?rel=0" frameborder="0" allowfullscreen></iframe>

###### References
Code for working with the LED and the PIR sensor was taken from [here](https://raw.githubusercontent.com/jedgarpark/Make_PIR_Sensor/master/MAKE_PIR_Sensor.pde). The original idea came from [here](http://makezine.com/projects/pir-sensor-arduino-alarm/) but I took it and made it better. 
