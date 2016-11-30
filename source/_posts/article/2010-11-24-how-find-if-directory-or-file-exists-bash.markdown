---
layout: post_article
category: article
date: 2010-11-24T00:00:00
title: "How to find if a directory or file exists in Bash"
tags: [bash, snippet, code]
---

This is a quick service announcement on how to find if a directory or file exists in Bash.

```bash
#!/bin/bash

# Notice the '-d'
if [ -d ~/.bin-private ]; then
    echo "Your private bin exists."
else
    echo "Your private bin doesn't exists."
fi

# Notice the '-f'
if [ -f ~/.ssh/config ]; then
    echo "You have configured SSH."
else
    echo "You haven't configured SSH."
fi
```

You are welcome.
