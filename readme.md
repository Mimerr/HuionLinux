# Huion Kamvas Pro 16 on Linux

This is a driver of sorts for the Huion Kamvas Pro 16 graphics tablet monitor.

It is highly tailored to my personal setup running Kubuntu on an unconventional monitor arrangement. It is somewhat easy to adapt however, so if you want to fork it and build it up for your tablet and set up, feel free.

The input bindings are directly coded in the python files. For now. If you are looking for a more robust solution, check out [joseluis/huion-linux-drivers](https://github.com/joseluis/huion-linux-drivers) and follow the directions there.

I built this because I was having some trouble with that project. I did go through the setup process there,
so it is possible some steps there are required here and I just didn't realize. But I think this setup process should
be relatively easy and not require much system changes or permissions.

## Install

1. Download/install the dkms deb from: [Here](https://github.com/DIGImend/digimend-kernel-drivers/releases) This more or less takes care of all the pressure and tilt input for the actual pen, which I didn't want to mess with.
2. Add your user to input group. `sudo gpasswd -a username input` Where username is your user name. This is needed so your user can actually see the device events.
3. **Optional** if you want to be able to launch it as a program. Copy the .desktop file to ~/.local/share/applications (may be different on other distros.) Also in the .desktop file The Exec=python /path/to/daemon.py line needs to be changed to whereever you put this project's python files. I usually make an Applications/Huion folder path in my home folder.
4. **Optional** if you want the daemon to be running when you login automatically. Add program to autostart on your distro. In KDE there is an option for this in the system settings, just Add Program and point to the .desktop file. (Of course there are other ways to do this but this seemed to be the easiest and not require any command line or system changes.)
5. Manual configuration. This is where things get a bit 'personal' to you.
    - First, in config.py there are instructions on how to find the needed values for those variables. This is to properly calibrate the position of the monitor for multi-monitor setups and things like that.
    - Second, the actual actions to be taken when buttons/touchstrip inputs occur are in buttons.py and touchstrip.py. In touchstrip there is an up and down variable delcared with command/args values. In buttons there are codes associated with all the buttons on the tablet and pen with the same. The command value needs to correspond to the action you are wanting to occur, e.g. keydown ctrl will hold the ctrl key down when you press that button. Then release it when you let go. Or key ctrl+z will do the undo command in most programs.
6. Dependencies for the project almost definitely exist but sadly I did not really keep track of it. So I cannot say for sure what all will be needed. Python obviously. Pip in evdev might be the only one.

## Future Ideas

I put this together in a weekend and am pretty happy with it really. If time ever permits and other projects don't win my attention, there are plenty of things that can make this better. I'm not going to try to expand it to other tablets (at least it is not in my priorities. See the joseluis project for that.) Instead my plans are to just continue being selfish about it and build on things I want. :D

1. Profile/Workspace system. The joseluis project has this already. I'd like to implement something similar. This would also make configurations be in one place, which would be nice.
2. A GUI to manage the profiles and input mappings. Also to restart the daemon and such. This would probably be a separate project inside this project. So I'd have to organize the files a little better and make a messaging system so the daemon and gui can talk to each other.
3. An OS widget pop up selector for quickly/visually switching between profiles and seeing information about the tablet/daemon/profile. Would probably be a 3rd project that interacts the same way the GUI does but can be installed on KDE and hotkeyed to pop up over the mouse cursor position. Know nothing about plasmoids but guessing that's where I need to start my research for this.
4. Automate as much of the configuration values as possible. Right now the set up is a bit tedious because you have to run commands to get information and such. I think a lot of this info could be automatically deciphered from those commands results with some grepping and string manipulation. Doing this may also prepare it to support more tablets better.

I think if I got to that point I'd pretty much be done with this and have a pretty awesome tablet environment for myself (and anyone else that uses a similar setup!) Then maybe I could work on making it more generic and adapt it to work with other tablets if any interest exists.

## Contributions

If anyone wants to tackle the Future Ideas, feel free to make a pull request. I'll eventually check it out and determine if it is a right fit or at least a good start.

If anyone wants to do things not on the Future Ideas list it may be better to just fork and make your own project. But I won't be totally against merging pull requests for anything that doesn't mess up the ease of use for my personal needs (again so selfish!)

Bug fixes and reports are always welcome.

## License

I don't really know a ton about licenses so I just put the MIT license in there. Pretty sure the libraries I used are also MIT or similar. I want anyone that can get use out of this to do whatever they want with it.
