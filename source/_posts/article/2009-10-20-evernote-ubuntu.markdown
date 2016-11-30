---
layout: post_article
category: article
date: 2009-10-20T00:00:00
title: "Installing Evernote on Ubuntu 9.04"
tags: [evernote, ubuntu, wine, linux]
---

[Evernote](http://www.evernote.com/) is a note taking service that has clients for [Windows](http://www.evernote.com/about/download/windows.php), [Mac OS X](http://www.evernote.com/about/download/mac.php), [iPhone](http://www.evernote.com/about/download/iphone/), and some other systems I don't use. Which is great but I doesn't support Linux.

The installation process is really simple just [install Wine](https://help.ubuntu.com/community/Wine "Ubuntu Community Documentation for Wine") and download [Evernote 3.1 for Windows](http://www.evernote.com/about/download/windows.php) (not the beta). Next just type in `wine ~/Downloads/Evernote_3.1.0.1225.exe` and follow the normal installation process.

{% include c_image.html src='2009/292/evernote-ubuntu/evernote-windows-client-in-ubuntu.png' alt='Evernote in Ubuntu 9.04' %}

Evernote is really cool, but as you can see from the screen shot above, it doesn't look so good. But I am impressed though that Wine added the Tray icon to my Gnome notification area.
