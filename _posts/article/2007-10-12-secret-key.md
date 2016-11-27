---
title: Generate a secret key for your Django Application
date: 2007-10-12 00:00:00 Z
categories:
- source
- article
tags:
- django
- snippets
- python
layout: post_article
---

```python
#!/usr/bin/python

import string
from random import choice

characters = "{0}{1}{2}".format(string.letters, string.digits,
                                string.punctuation)

print ''.join([choice(characters) for i in range(50)])
```
