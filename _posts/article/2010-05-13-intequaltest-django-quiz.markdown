---
title: What is the Django Template Tag intequaltest and an update on Django Quiz?
date: 2010-05-13 00:00:00 Z
categories:
- source
- article
tags:
- django
- django-quiz
- python
- project
layout: post_article
---

[Travis Millward](http://gravitymad.com/) [commented](http://mylesbraithwaite.com/projects/django-quiz/#c195) on my [Django Quiz](http://mylesbraithwaite.com/projects/django-quiz) project today:

<blockquote class="blockquote">
    <p>Hey Myles, I believe I'm going to checkout your django quiz. Can you explain what the <code>&lcub;% if score.corrent_anwsers|intequaltest:question %&rcub; This wont work &lcub;% endif %&rcub;</code> is doing? It looks really good!</p>
</blockquote>

First I just like to say I love talking to people so if you ever have a question for me about anything (literally) don't hesitate emailing me [me@mylesbraithwaite.com](mailto:me@mylesbraithwaite.com) or chatting with me on XMPP.

```python
def intequaltest(value, arg):
    return (value == arg)
```

Okay so `intequaltest` is got to be the studied template tag in the world. It's sole purpose is to see if two things (i.e. a `list`, `str`, `dict`, etc.) are the same and if they are return `True` or `False`. In this case see if the correct answer is equal to the answer they gave. I will go into the history a little later in this post but essentially this application use to work a lot differently and the only reason this template tag is in here is because I have an issue with copying and pasting.

When I first started developing the Django Quiz application in 2008 it was for a client. They wanted to quiz their sales consultants on very complex financial process. The consultants could take each quiz as many times as they want, but their "score" wouldn't be submitted to their manager until they got prefix.

I spent about a two days in July (10th, and 11th) developing this application for the client. In the middle of my second day the client came to me and said they found a better solution, a pice of paper and a pencil.

I have been asked about this application five or six times in the last month, so I guess it is about time I write my formal apology. This application doesn't work. I tried to start up again on April 28, but my heart isn't really there anymore (my heart was not really there the first time but I was getting paid).

So will this application ever be completed? Maybe, if one day I wake up and get really excited about coding it again or a client comes along and ask me to code them a quiz application.
