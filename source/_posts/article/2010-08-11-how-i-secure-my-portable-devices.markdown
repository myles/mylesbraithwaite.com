---
layout: post_article
category: article
date: 2010-08-11T00:00:00
title: "How I Secure My Portable Devices"
tags: [laptop, lost, portable-device, security, phone, stolen]
---

We are living in a world where the average person is carrying at least three portable computing devices. Okay maybe not the average person but most days I have three portable computing devices with me; a laptop, cell phone, and tablet. Usually these devices have some sentience information; contacts, calendar, personal photos, documents, contracts, banking information, etc. During last nights [GTALUG](http://gtalug.org/ "Greater Toronto Linux User Group") [meeting](http://gtalug.org/wiki/Meetings:2010-08 "Linux Urban Street Hacking with William Porquet") we had a brief audience chat on dealing your portable device when it is outside the confront of your home. So i thought I would share my two cents.

The safeist way not to lose your computer and data (just ask an [iPhone engineer](http://www.suntimes.com/technology/ihnatko/2178822,ihnatko-apple-iphone-engadget-gizmodo.article "How Gizmodo got the biggest iPhone scoop of all")). If you can't live without your computer then do some serious auditing of your data. Do you need to carry around your personal (and corporate) accounting ledger, business contacts, calendar, proprietary source code, SSH keys, contacts, and other sensitive information. Also what I find helps is giving everything a value of money. For example I might have some source code for a client project I have been working on for sixty billable hours and haven't got paid yet. That would have a high monitory value, unlike an open source project. Something I should start doing is physically locking my laptop with a [security lock](http://www.amazon.ca/gp/product/B001911ZRQ?ie=UTF8&tag=mylesbrait0b-20&linkCode=as2&camp=15121&creative=390961&creativeASIN=B001911ZRQ) (they are reality cheap compared to my laptop and it's data).

Backup, Backup, Backup. I am not going to go to much into this but have some sort of offsite backup system installed and working. Mine is a combination of Git/Hg, [Dropbox](https://www.dropbox.com/referrals/NTU3ODAwMjk), and S3.

*   If I am working on a proposal it is saved to my Dropbox.
*   If I am working on code it is pushed to a remote computer.
*   If I can't push to a remote computer (SSH is blocked) I push to an S3 bucket.
*   etc.

Encrypt your laptops hard drive.

Most enterprisy companies have remote wipe on Blackberry's Enterprise Server, make sure you can have the same. The iPhone supports this though MobileMe and Android has [WaveSecure](https://www.wavesecure.com/) if you data is worth more than $200 these services are very beneficial. Also never be afraid of doing a remote wipe, backup your phone at least once or twice a week and use services that have some type of push to "the cloud" feature (I use SimpleNote which sends my notes to a remote web service).

Don't be paranoid, the majority of the people in this world are honest and good. If you have something telling them how to contact you if you device get lost, they will contact you. Just make sure they can easily find your information.
