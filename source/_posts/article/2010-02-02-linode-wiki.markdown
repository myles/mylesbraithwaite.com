---
layout: post_article
category: article
date: 2010-02-02T00:00:00
title: "Got another Linode & Moved the Wiki"
tags: [linode, system-administration, munin, wiki, server, hatta]
---

I ordered a second [Linode](http://www.linode.com/?r=489fd5146a3553db67138302f6c6d44a029cf45a "A VPS Provider") (a 360) on the weekend for some PHP applications ([Fever](http://feedafever.com/ "An online feed reader.") and [DokuWiki](http://dokuwiki.org/ "A super simple and powerful wiki engine.")). I have been with many VPS services and [Linode](http://www.linode.com/?r=489fd5146a3553db67138302f6c6d44a029cf45a "A VPS Provider") is by far the best you can buy (shared host I will have to say [Nearly Free Speech](https://www.nearlyfreespeech.net/ "NearlyFreeSpeech.NET Web Hosting")). It is hosted in the same data centre (Newark, NJ) so I have an internal IP address connecting both of them. I am running [Nagios](http://www.nagios.org/) and [Munin](http://munin.sourceforge.net/) on both computers ([Panda is monitoring Fox](http://panda.mylesbraithwaite.com/munin/mylesbraithwaite.com/fox.mylesbraithwaite.com.html) and [Fox is monitoring Panda](http://fox.mylesbraithwaite.com/munin/mylesbraithwaite.com/panda.mylesbraithwaite.com.html)) that way if one goes down the other will notify me.

I also moved my [Wiki](http://wiki.mylesbraithwaite.com/) from [DokuWiki](http://dokuwiki.org/ "A super simple and powerful wiki engine.") to [Hatta](http://hatta.sheep.art.pl/). Hatta is a really simple wiki engine written in Python that use Mercurial for storage. Which means I just have to clone a repository to edit a page (you can clone the [my draft wiki](http://bitbucket.org/myles/wiki-pages/) or [my published wiki](http://wiki.mylesbraithwaite.com/hg/)). I am going to miss some of the more powerful features of DokuWiki so I have started working on my own wiki engine called **Episteme**.

Episteme will have some of my favorite feature of DokuWiki, Hatta, [Confluence](http://www.atlassian.com/software/confluence/), and [Yaki](http://code.google.com/p/yaki/).
