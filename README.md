# MylesBraithwaite.com

Hi! This is the source code for [my blog](https://mylesbraithwaite.com/). It uses the Ruby statis web site generator [Jekyll](https://jekyllrb.com) and a bunch of Node.js, Ruby, and Python scripts.

## Objectives

1. A place I can write blog posts.

## Development Environment Setup

You can run `./script/bootstrap` in the project path to setup your environment.

The following is a step by step guide for developing [my blog](https://mylesbraithwaite.com/).

### Requirements

* Ruby
  * [Bundler](http://bundler.io/) - `sudo gem install bundler`
* Node.js
  * Bower - `sudo yarn global add bower`
  * Grunt - `sudo yarn global add grunt-cli`
* Python 3.5
  * [awesome-slugify](https://pypi.python.org/pypi/awesome-slugify) - `sudo pip3 install awesome-slugify`
  * [python-frontmatter](https://pypi.python.org/pypi/python-frontmatter) - `sudo pip3 install python-frontmatter`
  * [PyYAML](https://pypi.python.org/pypi/PyYAML) - `sudo pip3 install PyYAML`

### Clone the Repository

```bash
$ git clone git@github.com:myles/mylesbraithwaite.com.git mylesbraithwaite.com
$ cd mylesbraithwaite.com
mylesbraithwaite.com $
```

### Instaill the Dependencies

Install the Ruby dependencies:

```bash
mylesbraithwaite.com $ bundle install
```

Install the Node.js dependencies:

```bash
mylesbraithwaite.com $ yarn install
```

Install the Bower assets:

```bash
mylesbraithwaite.com $ bower install
```

### Usage

#### Build the Web site

`grunt build` or `./script/build`

### Run a Development Server

`grunt develop` or `./script/server`

<http://127.0.0.1:4000/>

### Deploy the Web site

#### Staging

`grunt deploy` or `./script/deploy`

<https://staging.mylesbraithwaite.com>

#### Production

`grunt deploy:prod`

<https://mylesbraithwaite.com/>
