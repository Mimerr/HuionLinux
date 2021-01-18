# Huion Kamvas Pro 16 on Linux

This is a driver of sorts for the Huion Kamvas Pro 16 graphics tablet monitor.

It is highly tailored to my personal setup running Kubuntu on an unconventional monitor arrangement. It is somewhat easy to adapt however, so if you want to fork it and build it up for your tablet and set up, feel free.

If you are looking for a more robust solution, check out [joseluis/huion-linux-drivers](https://github.com/joseluis/huion-linux-drivers) and follow the directions there.

I built this because I was having some trouble with that project. I did go through the setup process there,
so it is possible some steps there are required here and I just didn't realize. But I think this setup process should
be relatively easy and not require much system changes or permissions.

## Install

1. Download/install the dkms deb from: [Here](https://github.com/DIGImend/digimend-kernel-drivers/releases) This more or less takes care of all the pressure and tilt input for the actual pen, which I didn't want to mess with.
2. Add your user to input group. `sudo gpasswd -a username input` Where username is your user name. This is needed so your user can actually see the device events.
3. Put the config, gui, and src folders where you want them to be run from (you can put everything there but that is the minimal needed stuff.) I usually make a ~/Applications/Huion folder and put them there.
4. **Optional** if you want to be able to launch it as a program. Copy the aide/.desktop file to ~/.local/share/applications (may be different on other distros.) Also in the .desktop file The Exec=python /path/to/main.py line needs to be changed to where you put your main.py file in step 2.
5. **Optional** if you want the daemon to be running when you login automatically. Add program to autostart on your distro. In KDE there is an option for this in the system settings, just Add Program and point to the .desktop file. (Of course there are other ways to do this but this seemed to be the easiest and not require any command line or system changes.)
6. Tablet Calibration. In config.py there are instructions on how to find the needed values for those variables. This is to properly calibrate the position of the monitor for multi-monitor setups and things like that.
7. Profiles. In config/profiles you'll find a Default.json file to get you started. You can rename this file to whatever you want and copy it as many times as you need. This folder is where the app will find all your profiles and the file name is what will be displayed in the GUI. The "buttons" section are the tablet's buttons from top to bottom and the pen's buttons from top to bottom. The "touchstrip" section is the movement up and an down on the tablet's touchstrip. Options for "command" are: key, keydown, keyup, click, mousedown, mouseup. The args are for what action to take. For example "key" and "ctrl+z" will make that button perform the traditional shortcut for undo. For other options search out what xdotool key codes exist.

Note: Dependencies for the project almost definitely exist but sadly I did not really keep track of it. So I cannot say for sure what all will be needed. Python obviously. I added a requirements.txt file for the pip install but I'm not sure if it is 100% accurate.

## Usage

The big bottom button on the Kamvas Pro 16 can be held to bring up the hardware settings menus. I decided to make this button hard coded to toggle the GUI instead of being mappable. Don't hold the button if you don't want the hardware menus. But you can just click it without worry. So, clicking it will toggle visibility of the GUI.

Do **NOT** close the GUI. Use the button to toggle it. If you close it, it will be gone until you restart.

The GUI will always have a "Refresh" button at the top. This will rebuild the profile options. So if you make changes in your profile's json file or add/delete profiles, use this to update the list of profile options and button actions for them.

It is quite simple from there. Just select your profile. And all your buttons will do what you have set in that profile's json file.

The GUI can be dragged around the screen by holding close to but not in the buttons and will always be on top so if you want to keep it up and quickly switch between profiles for lots of potential button actions, go for it!

## Future Ideas

I do not have immediate plans to support other tablets. If you follow what I'm doing for mine in the code, you can probably easily adapt this to yours. Maybe one day if there is enough interest this could be expanded to automatically detect other tablets and set up based on that, but that is a lot of work and testing I just don't have time or equipment for.

There are still other things I'd like to do though. If you want to help out, feel free to tackle it.

1. Enhance the GUI to pop up a new window for editing a profile visually (instead of manually in the json.) Also would be nice to have the ability to create a new profile in this gui as well.
2. Automate the rest of the configuration. I think it is pretty simple to follow the instructions in the config.py and a lot is already automated but it'd be great if this could eventually be turned into an installer and it'd need to do everything automatically.
3. System tray icon. As of now the daemon part just runs in the background and when you show the gui it pops up and goes in the task bar which is fine. But it'd be nice to have a system tray icon for always showing the daemon is running. Could also add a menu to it so you can do things like restart the daemon, or open the gui from there or refresh the profiles. Or exit completely.
4. Automate the profile edits. It'd be nice to get rid of the 'refresh' button in the GUI. If it could detect new/removed files in the profiles folder and changes to the existing profiles' json, that'd be great.
5. Further GUI enhancement idea. Icons. Basically allow a person to add icons per profile. And only display the icons isntead of words. It'd shrink the space it takes overall and make it look nicer. Could make tooltips for the icons that show the name of the profile, and even better the active profile tooltip could show the json content so you can see the commands list.


## Contributions

If anyone wants to tackle the Future Ideas, feel free to make a pull request. I'll eventually check it out and determine if it is a right fit or at least a good start.

If anyone wants to do things not on the Future Ideas list it may be better to just fork and make your own project. But I won't be totally against merging pull requests for anything that doesn't mess up the ease of use for my personal needs.

Bug fixes and reports are always welcome.

## License

I don't really know a ton about licenses so I just put the MIT license in there. Pretty sure the libraries I used are also MIT or similar. I want anyone that can get use out of this to do whatever they want with it.
