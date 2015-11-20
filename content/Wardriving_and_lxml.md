Title: Wardriving and lxml
Date: 2014-04-05 02:47
Tags: python, security
Summary: Playing with data from a wardriving run

## What is wardriving?

Wardriving is not as scary as it sounds. It involves using a wireless card to collect data on wireless networks as you drive. Using a few special tools we can collect data on all sorts of wireless networks, in this case 4579 of them. This data includes the network's names (SSID and BSSID), the type of encryption it uses if any, the channel it operates on, and all sorts of other information. This kind of data is actually quite useful. It gives insight into the kinds of wireless routers people buy and also if they are using the right kind of encryption. We can even hook up a GPS transmitter and track the exact location of each network to map them out on a service called [WiGLE](https://wigle.net/). It really is quite fun. It also draws a lot of odd looks. 

## The setup

My friend JJ and I decided to go wardriving. It required a few tools. The first thing we needed was the right software. We used a live USB stick with Kali linux. This gave us access to a tool called Kismet which handled all the dirty work in collecting information about the wireless networks. Normally this would be enough. However the wireless card in my laptop does not have as good of a range as something like [this](http://image.dhgate.com/albu_355651168_00-1.0x0/usb-wireless-adapter-ac-wifi-adapte-alfa.jpg). Luckily my lab has a long antenna like that one, and I have a wireless card it is compatible with, so we used that and got better results than we would have otherwise. 

![](/content/images/2014/Mar/2014_03_22_11_31_45.jpg)

As you can see it is quite large. We also wanted to use GPS but could not get a bluetooth connection between Kali and my phone to do so. 

## The experiment

After plugging everything in and booting up Kali we hopped in JJ's truck and drove around the greater Brigham Young University area. We tried to focus on areas where there are apartment complexes, but we drove through some residential areas as well. 

![](/content/images/2014/Mar/wardrive.png)

That is what Kismet looks like when running. As we drove it spit out names of wireless networks it discovered and gave a running count of the total number of networks discovered. 

![](/content/images/2014/Mar/textsecure505519296.jpeg)

We looked quite sketchy as we drove around. I held the wireless card with the antenna straight in the air while we drove for an hour through various neighborhoods. We got lots of goofy and perplexed looks. Those people probably thought we were trying to communicate with aliens. 

## The data

The wardrive produced a 20 megabyte XML file for us to enjoy. The XML files Kismet produces are not the easiest to go through, but where there is a will there is a way.

### Analyzing the metadata

Python is great for going through this kind of data. I had not used `lxml` before so I decided to try it out. 

The obvious data to look at is how many networks were discovered and of those networks how many used certain kinds of encryption. After browsing through the XML I noticed that some of the `wireless-network` elements did not have an `SSID` child, and if they did that child sometimes had more than one `encryption` child. The multiple `encryption` elements occured when the network used WPA. I was not concerned with the specific ciphers used in the WPA handshake so I only needed one of those children. But how could I parse it correctly and get all of the text nodes I wanted? Thankfully someone came up with `xpath` which comes in handy for parsing XML. 

```
$ python
Python 2.7.3 (default, Feb 27 2014, 19:58:35) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from lxml import etree
>>> doc = etree.parse('wardrive.netxml')
>>> nodes = doc.xpath('//wireless-network/SSID/encryption[1]/text()')
>>> len(nodes)
4579
>>> wpa = wep = none = 0
>>> for node in nodes:
...     if 'None' in node:
...             none += 1
...     elif 'WPA' in node:
...             wpa += 1
...     elif 'WEP' in node:
...             wep += 1
... 
>>> wpa
3699
>>> wep
76
>>> none
804
```

We can load our XML document with `lxml`'s `etree`. We can then parse the different nodes using `xpath()` on the `doc` variable. The `xpath` is constructed based on the layout of the elements in the document. The one I used only wants the first child element named `encryption` and it gathers all of the actual text from those nodes. The result is stored in a variable that can be treated like a list even though it is not a list. From this we can gather the total number of networks (4579) and we can count the different number of networks using `WEP`, `WPA`, or no encryption. Thankfully the number of `WPA` networks is by far the highest. However the number of open networks is slightly disturbing. Because we drove through mostly residential areas the number of open networks should be much lower. Normally I would attribute this to passing by a large number of businesses with open networks for customers, but that was not the case here. `WEP` is basically dead, although it has unfortunately not been fully stamped out. 

If you use the development version of Kismet you can also track the number of networks using `WPS`. If you are not aware, `WPS` is horribly flawed yet its use is widespread. 

There are plenty of other statistics you could get from these XML log files. I personally am only interested in encryption statistics. So go out wardriving, maybe use a [Raspberry Pi](https://seanmckaybeck.com/making-wardriving-easier/), and start parsing those log files with `xpath`!
