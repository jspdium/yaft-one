# Yet Another Flask Tutorial - Part 1

This is the source code for [Part 1](https://medium.com/@jorge.sousapinto/yet-another-flask-tutorial-e2fb84bdcd36) of my Yet Another Flask Tutorial.

## Installation

Create a Python3 virtual environment and install Flask in it:

```
$ cd yaft-one
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install flask
```


## Usage

Before running `app.py` set the `APP_CONFIG` environment variable to one of `config.DevelopmentConfig`, `config.TestingConfig`, `config.StagingConfig`, or `config.ProductionConfig`. 


```
$ export APP_CONFIG=config.DevelopmentConfig
$ python app.py
```


