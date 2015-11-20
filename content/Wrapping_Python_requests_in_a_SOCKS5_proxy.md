Title: Wrapping Python requests in a SOCKS5 proxy
Date: 2015-02-09 23:18
Tags: python, how-to
Summary: How to send requests in Python through a proxy

I have run into situations when I wanted to route some of my Python requests out to the internet through a SOCKS5 proxy, specifically through [Tor](https://www.torproject.org/). There are answers out there on Stack Overflow but they are not all extremely clear.

The easiest way to wrap all requests done by a Python module in a SOCKS proxy is to use the SocksiPy library. The project was abandoned by its owner around 2007. Someone made a few modifications after that, but also abandoned it eventually in 2010. Thankfully the code still works! The latest version can be downloaded from [here](https://code.google.com/p/socksipy-branch/).

To install, simply move the `socks.py` file into your Python installation's library directory (`/usr/local/lib/python2.7/dist-packages` for me on Crunchbang).

Using it is also simple. Just import the module, set the proxy information, then wrap the module you want to have proxied. 

```
import smtplib

import socks

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
socks.wrapmodule(smtplib)
```
After this all things done by smtplib will be sent through your proxy. The above code is designed to work with a running local `tor` installation. 

This is a great and simple solution to all your proxy needs (SOCKS4, SOCKS5, or HTTP).
