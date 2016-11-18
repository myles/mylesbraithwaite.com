---
layout: post_article
category: article
date: 2007-10-12T00:00:00
title: Generate a secret key for your Django Application
tags: [django, snippets, python]
---

```python
#!/usr/bin/python

import string
from random import choice

print ''.join([
    choice(string.letters + string.digits + string.punctuation) for i in range(50)])
```
