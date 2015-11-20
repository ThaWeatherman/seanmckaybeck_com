Title: Choosing a Good Password
Date: 2014-03-10 16:42
Tags: security, passwords
Summary: How to choose and manage good, secure passwords

```
Your password should be at least eight characters
It should contain at least one number
It should contain at least one uppercase letter
It should contain one of the following symbols: !, $, @, %
The upper case letter should not appear at the start
The number should not appear at the end
You should enter the password with your eyes closed while using your nose
```

Have you ever seen rules like these? Of course you have. Do you hate rules like these? Do you hate passwords in general? If you do, I agree with you: they suck. However passwords aren't leaving us anytime soon. Passwords are here to stay. 

## But why?

Because there are **no** better options. Think about it: what else could you use to prove you are you to a website? Nothing. One could argue for some obscure form of [public key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography) but that isn't user-friendly. There has been plenty of [research](https://research.microsoft.com/apps/pubs/?id=161585) in this field and the general consensus is passwords are here to stay.

## But those rules...is there no other way?

Unfortunately some people think forcing users to obey sets of password rules like those shown above makes the users' accounts more safe from being breached. What it really does is make it easier for an attacker to guess your password. Instead of having no idea of how long the password is or what kinds of characters are used in it the attacker knows exactly what to go after. If the website is ever breached and the user account database is dumped, the hacker will be overjoyed with how easy it is to crack your password. 

Restrictive rules like these are more harmful than helpful. The best thing to do if you see them is contact the support team and tell them you don't like the rules. If enough people complain maybe we can cure this disease. 

Despite all of this there are still best practices for choosing a password. 

## Best practices

### Passphrase?

[Some people say](https://xkcd.com/936/) you should use some sort of pneumonic to remember your password. Instead of using a pass*word* you should use a pass*phrase*. An example would be the names of all the cats my family has owned over the years. I disagree!

If I were to choose a passphrase it would be chosen from a pool of things I can easily remember, such as names, places, or favorite things. Most likely these things would be similar in some way or another to increase memorability. Say I comprised my passphrase of the names of my grandparents: clivedixiepauljudy. This is easy for me to remember and long enough that it would take some time to crack. However with a little background knowledge about my life a determined attacker could try phrases like this until s/he found my phrase! It is **not** hard to find out personal information about a person. Facebook connections give away a lot, and most Twitter profiles are public. This makes passphrases weak in practice, unless you choose them to be completely random, such as `nailfishhousetarbush`, thus making them less memorable and defeating the purpose of the phrase entirely. 

### Reuse

[Don't ever reuse a password](https://xkcd.com/792/). __*Never ever ever ever*__. Why? All it takes is me getting your password from one website to get into your account on multiple websites. If `cutekitteh` is my password on Facebook and Chase bank and you get my Facebook password, you now have access to my bank account. Relying on the website to keep your password safeguarded is a poor approach as well, as [many](http://thinkprogress.org/security/2013/12/31/3108661/10-biggest-privacy-security-breaches-rocked-2013/#) services have shown us. Developers aren't geniuses and often make poor choices when it comes to safely storing sensitive information. 

### What then?

A long, completely random password is more effective. `laul@hf8#7ho78q4roa$3hah3^o8r38hr3p*ha3rh` is a good example. What? How will you remember that? You don't. Instead, let something remember it for you. Most websites have a maximum password length, so I typically stick with 30 characters. 

## Solution

So how *do* you create a random 20+ character password and keep track of a different one for each website? Enter the password manager. 

A password manager handles storing all of these passwords for you, tracking what they are for, generating the passwords, and even filling in the details when you access the website! A lot of people use [LastPass](https://lastpass.com/) but I don't so I can't say much about it. LastPass seems to be a nice service, although to use their mobile apps you have to pay. You also have to trust them to store all of your credentials safely, since your password "vault" syncs up to their servers. I personally don't trust any entity enough to give it the keys to all of my personal information, so my recommendation is to avoid LastPass.

I use [KeePass](http://keepass.info/). KeePass lets you categorize your passwords based on what you use them for. It also will generate passwords for you so you don't have to worry about smashing your keyboard every time you want to create a new account somewhere. You do have to manually add the information to KeePass, but that's OK: after the entry is in your database KeePass has some shortcuts for quick copy-pasting so you can login to whatever you want easily. KeePass also stores all these credentials in an encrypted form, so you do have to remember one password. 

There are a classic and professional version of KeePass. However both are completely free to use. The main version is made for Windows, but there are options for other platforms as well. The [download page](http://keepass.info/download.html) has a list of ports to other platforms, including OS X, iOS, Android, and Blackberry. I use [KeePass2Android](https://play.google.com/store/apps/details?id=keepass2android.keepass2android) and it is great. I sync my database from my computer to my phone with Dropbox. Since the database is encrypted with a strong password (mine is 34 characters) I have no worries about Dropbox snooping around my password database. Thanks to Dropbox I can access all of my accounts on my phone, my Linux computers, and my Windows computers. 

You can use whatever password manager you want, but I recommend KeePass. You can use your web browser if you want, but I avoid that as malware is designed specifically to steal passwords from web browsers. If you care about the security of your information you need to start using these kinds of techniques. You will be glad you did. 
