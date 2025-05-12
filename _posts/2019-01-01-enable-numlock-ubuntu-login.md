---
layout: post
title: "How to enable NumLock on Ubuntu Login Screen"
excerpt: In this post we discuss how to enable both NumLock and tap-to-click for the login screen of Ubuntu 18.04 LTS.
author: jharemza
date: 2019-01-01
updated: 2019-04-03
tags: [Ubuntu, NumLock, tap-to-click, login-screen, Linux tips]
categories: [Linux, Tutorials]
---
## Introduction

In this post we discuss how to enable both NumLock and tap-to-click for the login screen of Ubuntu 18.04 LTS.

## Steps

The GSettings configuration tool will enable us to do the task via 2 commands, although it requires the gdm user privilege.

1. Get gdm user privilege in a terminal window.

    1. Open terminal by either pressing Ctrl+Alt+T or searching for ‘Terminal’ from software launcher.

        ![launch terminal](/assets/img/posts/launch_terminal.jpg)

    2. Run command to get root privilege (type your password when it prompts):

            sudo -i

        ![get into root](/assets/img/posts/Screenshot_from_2019-04-03_11-18-50_cropped.png)

    3. In the terminal, run command to allow gdm to make connections to the X server:

            xhost +SI:localuser:gdm

        ![allow-gdm-tox](/assets/img/posts/Screenshot_from_2019-04-03_11-21-02_cropped.png)

    4. Finally switch to user gdm in this terminal via command:

            su gdm -s /bin/bash

        ![gdm-terminal](/assets/img/posts/Screenshot_from_2019-04-03_11-21-52_cropped.png)

2. Run the command to enable NumLock automatically on the login screen:

        gsettings set org.gnome.settings-daemon.peripherals.keyboard numlock-state 'on'

    ![enable numlock](/assets/img/posts/Screenshot_from_2019-04-03_11-23-10_cropped.png)

3. To enable tap-to-click, run the following command in the same terminal:

        gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true

    ![enable tap-to-click](/assets/img/posts/Screenshot_from_2019-04-03_11-24-20_cropped.png)

NumLock and tap-to-click should now be enabled on your next startup.
