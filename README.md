<h1 align="center">My-IKEA-Greenhouse-Cabinet</h1>

<p align="center">
    <img src="https://img.shields.io/github/v/release/chrisdo023/My-IKEA-Greenhouse-Cabinet?include_prereleases&logo=github">
    <img src="https://img.shields.io/gitlab/coverage/chrisdo023/My-IKEA-Greenhouse-Cabinet/main">
    <img src="https://img.shields.io/github/repo-size/chrisdo023/My-IKEA-Greenhouse-Cabinet">
    <img src="https://img.shields.io/github/downloads/chrisdo023/My-IKEA-Greenhouse-Cabinet/total">
    <img src="https://img.shields.io/github/license/chrisdo023/My-IKEA-Greenhouse-Cabinet">
    <img src="https://img.shields.io/github/followers/chrisdo023?style=social">
    <img src="https://img.shields.io/pypi/pyversions/4?logo=Python&logoColor=white">
    <img src="https://img.shields.io/github/commit-activity/m/chrisdo023/My-IKEA-Greenhouse-Cabinet">
</p>

For any IKEA greenhouse cabinet enthusiasts, we know maintaining a healthy environment for our plants is important.

With a comprehensive web application built, using a Raspberry Pi integrated with a DHT22 sensor, users are now able to view the temperature and humidity inside their cabinet anywhere from the comfort of their home via computer or mobile phone.

<a name="installation"></a>
## Installation
```
$ git clone https://github.com/chrisdo023/My-IKEA-Greenhouse-Cabinet.git
$ cd My-IKEA-Greenhouse-Cabinet
$ pip3 install -r requirements.txt
```

## Dependencies
My-IKEA-Greenhouse Cabinet currently only supports Python 3.

## Usage
Start the Flask web server via
```
$ python3 flask/__init__.py
```
will allow you to view the temperature and humidity inside of your cabinet through your browser.

By default it binds to all interfaces on port 5000 (so pointing your browser to `http://127.0.0.1:5000` will do the trick).


## Architecture
