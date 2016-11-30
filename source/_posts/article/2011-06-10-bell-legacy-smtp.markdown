---
layout: post_article
category: article
date: 2011-06-10T13:38:00
title: "Sympatico Legacy SMTP Server"
tags: [smtp, email, sympatico, tech]
---

One of the large issues when trying to configure people's email usually comes to sending messages. If you/they are using Bell Internet (previously Sympatico) you can use a legacy SMTP server at `smtp1.sympatico.ca`. It will only work on Bell's ISP (not include your local Starbucks), so it would not be a good idea to configure it on a laptop. If they are working on a laptop the best idea is to see if their email provider provides an iterative SMTP port. Port numbers `587` and `2525` have become a somewhat standard alternative for email providers. If that doesn't work, another option would be to use the SSL server which is usually on port `465`.
