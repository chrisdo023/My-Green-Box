<h1 align="center">My-Green-Box</h1>

<p align="center">
    <img src="https://img.shields.io/github/v/release/chrisdo023/My-Green-Box?include_prereleases&logo=github">
    <img src="https://img.shields.io/gitlab/coverage/chrisdo023/My-Green-Box/main">
    <img src="https://img.shields.io/github/repo-size/chrisdo023/My-Green-Box">
    <img src="https://img.shields.io/github/downloads/chrisdo023/My-Green-Box/total">
    <img src="https://img.shields.io/github/license/chrisdo023/My-Green-Box">
    <img src="https://img.shields.io/github/followers/chrisdo023?style=social">
    <img src="https://img.shields.io/pypi/pyversions/4?logo=Python&logoColor=white">
    <img src="https://img.shields.io/github/commit-activity/m/chrisdo023/My-Green-Box">
    <img src="https://img.shields.io/github/license/chrisdo023/My-Green-Box">
</p>

For any IKEA greenhouse cabinet enthusiasts, we know maintaining a healthy environment for our plants is important.

With a comprehensive web application built, using a Raspberry Pi integrated with a DHT22 sensor, users are now able to view the temperature and humidity inside their cabinet anywhere from the comfort of their home via computer or mobile phone.

<a name="installation"></a>
## Installation
```
$ git clone https://github.com/chrisdo023/My-Green-Box.git
$ cd My-Green-Box
$ pip3 install -r requirements.txt
```

## Dependencies
My-Green-Box currently only supports Python 3.

## Usage
Start the Flask web server via
```
$ python3 flask/app.py
```
will allow you to view the temperature and humidity inside of your cabinet through your browser.

By default it binds to all interfaces on port 5000 (so pointing your browser to `http://127.0.0.1:5000` or `http://<Flask Server IP Address>:5000` will do the trick).

## Roadmap

- [x] Create RESTful Web APIs
- [x] Add Index Templates
    - [x] Establish Header with "Add Me" and "Notification" features
    - [x] Display created Cabinet
    - [x] Display captured temperature and humidity data from Cabinet
        - [ ] Structure temperature and humidity data in aesthetic format
    - [ ] Add temperature and humidity graph
    - [ ] Display number of plants inside of Cabinet
- [ ] Add "Update" mechanism for Notification bell (Creation/Deletion of Cabinet, All Time High Temperature for Cabinet, Watering Plants)
- [x] Add Ajax (Asynchronous JavaScript and XML) to Pass Information between Client-Server
- [x] Interface DHT22 sensor w/ Raspberry Pi (RPi)
- [x] Capture temperature and humidity data w/ DHT22 sensor
- [] SQLite3
    - [x] Setup Structured Query Lite (SQLite3) on RPi
    - [ ] Create 3 different tables (Cabinets, DHT22, Plants)
    - [ ] Establish Primary Key and Foreign Key for Tables
    - [ ] Successfully access all data from Tables
the readme
- [ ] Optimize Flask Server or other mechanisms
- [ ] Create test bed for application
- [ ] Version 1 Roadmap is completed when above tasks are completed

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

## Architecture
