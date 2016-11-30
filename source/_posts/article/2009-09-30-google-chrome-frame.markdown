---
layout: post_article
category: article
date: 2009-09-30T00:00:00
title: "Google Chrome Frame"
tags: [google-chrome-frame, microsoft, internet-explore]
---

This week two [Mozilla Foundation](http://mozilla.org/) executives, Chairperson [Mitchell Baker](http://lizardwrangler.com/) and [Mike Shaver](http://shaver.off.net/) Vice President Engineering criticised Google for their [Chrome Frame](http://code.google.com/chrome/chromeframe/), an Internet Explorer add-on that allows the use of the Google Chrome's layout engine instead of using Microsoft's [Trident](http://en.wikipedia.org/wiki/Trident_%28layout_engine%29) layout engine.

[Mike Shaver](http://shaver.off.net/diary/2009/09/28/thoughts-on-chrome-frame/) is criticising Chrome Frame for loss of security controls and features.

> Running Chrome Frame within IE makes many of the browser applications features non-functional, or less effective. These include private browsing mode or their other security controls, features like accelerators or add-ons that operate on the content area, or even accessibility support.

And [Mitchell Baker](http://blog.lizardwrangler.com/2009/09/28/browser-soup-and-chrome-frame/) is criticising Chrome Frame for the loss of control from the users perceptive.

> What rendering engine do you end up using? That depends on the website now, not on you. And if you end up at a website that makes use of the Chrome Frame, the treatment of your passwords, security settings, personalization all the other things one sets in a browser is suddenly unknown. Will sites you tag or bookmark while browsing with one rendering engine show up in the other? Because the various parts of the browser are no longer connected, actions that have one result in the browser you think youre using wont have the same result in the Chrome browser-within-a-browser.

I agree that the issue of security of Chrome Frame is a big one. But from the perspective of a web developer this is the greatest thing that Google has released in a long time. One issue that I run into writing web applications is cross-browser support because most business management web software (CRMs, ERPs, Accounting, etc.) have be design to work with IE 6 (and don't work with a modern web browser) it is difficult to tell someone you will have to open Mozilla Firefox or Google Chrome to visit the web page. So I have to spend almost half my time writing IE support.

One way around this issue is the Firefox add-on [IE Tab](http://ietab.mozdev.org/) (which allows the user to render a web page using the Trident layout engine instead of the Mozilla's [Gecko](http://en.wikipedia.org/wiki/Gecko_%28layout_engine%29) layout engine). This plugin had a major design flaw it was targeted to the Power User which meant it was extremely hard to train non-technical people to use the plugin.

Google Chrome Frame has taken the need for the user to switch the Layout Engine and has put that power into the hands of web developers (which I admit is a bad thing). All I have to do is add a simple meta tag to the `<head>` of the base template:

```html
<meta http-equiv="X-UA-Compatible" content="chrome=1">
```

I don't think Google Chrome Frame is an elegant or technically sound solution but it is a step in the right direction and hopefully it just might make Microsoft and more importantly business management web software think that maybe they should start support the modern web.
