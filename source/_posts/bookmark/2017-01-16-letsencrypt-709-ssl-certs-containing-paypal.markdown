---
bookmark:
  url: https://textslashplain.com/2017/01/16/certified-malice/
  author: Eric Law
via:
  url: https://news.ycombinator.com/item?id=13412839
  title: 	Certified Malice
  publisher: HackerNews
  published: 2016-01-16T15:43
category: bookmark
date: '2017-01-16T21:08:37.435131'
layout: post_bookmark
slug: letsencrypt-709-ssl-certs-containing-paypal
tags:
- letsencrypt
- ssl
- infosec
- phishing
title: Let's Encrypt has issued 709 SSL Certificates Containing PayPal
---

> By December 8, 2016, [Let's Encrypt](https://letsencrypt.org/) had issued 409 certificates containing “Paypal” in the hostname; that number is [up to 709](https://censys.io/certificates?q=paypal+AND+parsed.issuer_dn%3A+%22C%3DUS%2C+O%3DLet%27s+Encrypt%2C+CN%3DLet%27s+Encrypt+Authority+X3%22) as of this morning. Other targets include BankOfAmerica ([14 certificates](https://censys.io/certificates?q=bankofamerica+AND+parsed.issuer_dn%3A+%22C%3DUS%2C+O%3DLet%27s+Encrypt%2C+CN%3DLet%27s+Encrypt+Authority+X3%22)), Apple, Amazon, American Express, Chase Bank, Microsoft, Google, and many other major brands. LetsEncrypt validates only that (at one point in time) the certificate applicant can publish on the target domain; the CA also [grudgingly](https://letsencrypt.org/2015/10/29/phishing-and-malware.html) checks with the SafeBrowsing service to see if the target domain has already been blocked as malicious, although they “disagree” that this should be their responsibility. Let's Encrypt’s short [position paper](https://letsencrypt.org/2015/10/29/phishing-and-malware.html) is worth a read; many reasonable people agree with it.
