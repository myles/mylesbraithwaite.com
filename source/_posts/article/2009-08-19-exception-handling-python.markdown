---
layout: post_article
category: article
date: 2009-08-19T00:00:00
title: "Exception Handling in Python"
tags: [pygta, python, exception, programming, logging]
---

Last night [PyGTA](http://pygta.org/ "Python Greater Toronto Area User Group") was a _Exceptional Conditions_ round table, like most PyGTA meetings it went [philosophical side of programming](http://tomlowshang.blogspot.com/2009/08/exceptional-condition.html "Tom Low-Shang: Exceptional Condition").

My personal philosophy, in web development, is to log exceptions, not found pages, and performance to almost extreme levels. Then weekly I take the logs and analyzes them with a script which puts them into a database, which groups the results. If an error happens more than five times in the given week the script creates a ticket in the issue tracker for me to work on later. I log all not found pages by real people (not search engine bots) to try and understand why they navigated to that page. The performance log is how long the system took to generate the page and SQL queries and time it took to execute them.

[Mike](http://blog.vrplumber.com/) took some good [notes](http://pygta.vrplumber.com/exceptional-conditions.html) so if you are interested you should definitely check it out.
