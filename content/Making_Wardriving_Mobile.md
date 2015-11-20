Title: Making Wardriving Mobile
Date: 2014-04-03 04:45
Tags: security, electronics
Summary: A project I made for using Kismet on-the-go for wardriving

Holding a laptop in your lap seems fun and all while you wardrive, but in reality it isn't very convenient. The ideal wardriving setup is small and mobile so you can shove it in a backpack and have it with you not just when you are driving, but also when you are biking or walking. 

The obvious choice for something like this is a Raspberry Pi. I use my phone typically, but it is only good for biking and walking. However the Pi does not make seeing a screen easy unless I want to carry around a monitor. I do want to see statistics on the networks I discover while I am wardriving after all. The higher the number of networks the more exciting it becomes!

Adafruit to the rescue! Adafruit sells an [LCD plate](https://www.adafruit.com/products/1109) that works with the Raspberry Pi. They also have conveniently open sourced their [Python code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code) for it so it is easy to work with the LCD. After a decent amount of soldering I had a working LCD.

For actual war driving software I use Kismet and gpsd. Kismet does the heavy lifting of discovering networks via the wireless card (I use the Alfa AWUS036H) and thankfully it has protocols clients can use to gather information about discovered networks.

I spent about an hour and a half writing the code that interfaces with the LCD and communicates with Kismet (but I spend a lot more than that actually finding out how to communicate with Kismet). I also have made it [open source](https://github.com/ThaWeatherman/KismetPiDisplay) with a description of how to get everything set up and working. It uses other open source software made by [Paul McMillan](https://github.com/PaulMcMillan/kismetclient) to communicate with Kismet. Feel free to browse the code and see how it works. It is licensed under the GNU Public License version 3 so you are free to change it. Improvements are of course welcome. 

## See it in Action

Starting up the code is simple.

<iframe width="640" height="360" src="//www.youtube.com/embed/C2a5YFlhnfo?rel=0" frameborder="0" allowfullscreen></iframe>

Sorry about the poor quality, but here is the LCD code in action.

<iframe width="640" height="360" src="//www.youtube.com/embed/Cq7il6wo5so?rel=0" frameborder="0" allowfullscreen></iframe>
