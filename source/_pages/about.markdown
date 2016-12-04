---
layout: page
title: About
---

{{ site.copy }}

You can follow this website on [Twitter](https://twitter.com/MylesWeb), [Feedly](http://cloud.feedly.com/#subscription%2Ffeed%2Fhttps%3A%2F%2Fmylesbraithwaite.com%2Ffeeds/), or [RSS](https://mylesbraithwaite.com/feeds/).

## About Myles

{% assign author = site.data.author %}

{{ author.copy }}

I was born on {{ author.born.date | date: '%d %B %Y' }} in {{ author.born.locality }} and currently lives in {{ author.location.locality }}, {{ author.location.region }}, {{ author.location.country }}.

## Contact Myles

You can email me at [{{ author.email }}](mailto:{{ author.email }}) and find me on {% for s in author.social %}{% if forloop.first == false %}, {% endif %} {% if forloop.last == true %}and{% endif %} [{{ s[1].name }}]({{ s[1].url }}){% endfor %}.

## Colophon

{% assign colophon = site.data.colophon %}

{{ site.title }} runs on [{{ colophon.runs_on.name }}]({{ colophon.runs_on.url }}) and is powered by [{{ colophon.powered_by.name }}]({{ colophon.powered_by.url }}) (you can view the source code on [GitHub](https://github.com/{{ site.repository.repositoryurl }})).
