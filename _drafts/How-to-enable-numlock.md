---
layout: default
title:  "How to enable NumLock on Ubuntu Login Screen"
class: post
excerpt: In this post we discuss how to enable both NumLock and tap-to-click for the login screen of Ubuntu 18.04 LTS.
author: Jeremiah J. Haremza
date: 2019-01-01
updated: 2019-04-03
---

In this post we discuss how to enable both NumLock and tap-to-click for the login screen of Ubuntu 18.04 LTS.

The GSettings configuration tool will enable us to do the task via 2 commands, although it requires the gdm user privilege.

1. Get gdm user privilege in a terminal window.

    1. Open terminal by either pressing Ctrl+Alt+T or searching for ‘Terminal’ from software launcher.

        ![launch terminal](/images/launch_terminal.jpg)

    2. Run command to get root privilege (type your password when it prompts):

            sudo -i

        ![get into root](/images/Screenshot&#32;from&#32;2019-04-03&#32;11-18-50_cropped.png)

    3. In the terminal, run command to allow gdm to make connections to the X server:

            xhost +SI:localuser:gdm

        ![allow-gdm-tox](/images/Screenshot&#32;from&#32;2019-04-03&#32;11-21-02_cropped.png)

    4. Finally switch to user gdm in this terminal via command:

            su gdm -s /bin/bash

    ![gdm-terminal](/images/Screenshot&#32;from&#32;2019-04-03&#32;11-21-52_cropped.png)

2. Run the command to enable NumLock automatically on the login screen:

        gsettings set org.gnome.settings-daemon.peripherals.keyboard numlock-state 'on'

    ![enable numlock](/images/Screenshot&#32;from&#32;2019-04-03&#32;11-23-10_cropped.png)

3. To enable tap-to-click, run the following command in the same terminal:

        gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true

![enable tap-to-click](/images/Screenshot&#32;from&#32;2019-04-03&#32;11-24-20_cropped.png)

NumLock and tap-to-click should now be enabled on your next startup.