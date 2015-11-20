Title: Running Terraria on Linux
Date: 2015-03-11 19:57
Tags: how-to
Summary: In which I try to help get Terraria running on Linux

After a significant amount of issues I finally was able to get Terraria running on Linux using `wine-staging`. `wine-staging` is `wine` with more bugfixes. It is not a stable version of `wine` but it is stable enough and has improved features.

I use Arch Linux so instructions will apply to my particular installation. I cannot guarantee this will work on other distros, although I hope it will. 

![screenfetch](/content/images/2015/03/Screenshot-from-2015-03-11-15-33-26.png)

First you need to install `winetricks` and `wine-staging`. 

```
$ wget http://winetricks.org/winetricks
$ chmod +x winetricks
$ sudo cp winetricks /usr/bin
```

For `wine-staging` follow the [documented installation steps](https://github.com/wine-compholio/wine-staging/wiki/Installation) for your distribution. Then add it to your path.

```
$ PATH=$PATH:/opt/wine-staging/bin
```

Now we need to install dependencies for Terraria. Please follow these steps exactly. Assuming you followed the prior steps correctly this will work.

```
$ WINEPREFIX=~/.wine32 WINEARCH=win32 winetricks dotnet40
$ WINEPREFIX=~/.wine32 winetricks xna40
```

Now download and install the [Windows version of Steam](http://media.steampowered.com/client/installer/SteamSetup.exe).

```
$ WINEPREFIX=~/.wine32 wine path/to/steam/executable/SteamSetup.exe
```

When it is finished don't run Steam. If you do run Steam it won't have any text. To run Steam do the following:

```
$ WINEPREFIX=~/.wine32 wine ~/.wine32/drive_c/Program\ Files/Steam/Steam.exe -no-dwrite
```

Now download and install Terraria within Steam. After this is done you can play Terraria! If you are used to playing on Windows the game content is saved to `My Games/Terraria`. With wine this `My Games` folder is in your user's home directory (`~/My\ Games`), so if you want to fiddle with world or character files that is the place to check. 

I have not tried running Terraria from within Steam. I have been running it directly through wine.

```
$ WINEPREFIX=~/.wine32 wine ~/.wine32/drive_c/Program\ Files/Steam/steamapps/common/Terraria/Terraria.exe
```

If you did everything correctly it should be working! Make sure to ALWAYS use `WINEPREFIX=~/.wine32` when working with this wine installation. It makes it work on a 64-bit system. `winetricks` uses `wine` under the hood so make sure to specify the `WINEPREFIX` there as well.

### Other issue

Currently I have no sound from the game. This is a known issue. See [this](https://appdb.winehq.org/objectManager.php?sClass=version&iId=24915) post and look for the issue called "No sound". There are possible fixes but they have not worked for me. If you run into this same issue please check that link and follow the possible fixes there.
