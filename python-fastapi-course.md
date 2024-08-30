# Python API Development - Comprehensive Course for Beginners
by `freeCodeCamp.org`, `Sanjeev Thiyagarajan`

YouTube: `https://www.youtube.com/watch?v=0sOvCWFmrtA&t=20s`

Source: 'https://github.com/Sanjeev-Thiyagarajan/fastapi-course'

 x. Intro
01. Project Overview Python
02. Mac Python Installation
03. Mac VS Code install and setup
04. Windows Python Installation
05. Windows VS Code install and setup
06. Python virtual Env Basics
07. Virtual Env on windows
08. Virtual Env on Mac
09. Install dependencies w/ pip
10. Starting FastAPI
11. Path Operations
12. Intro to Postman
13. HTTP Requests
14. Schema Validation with Pydantic
15.
16.
17.
18.
19.
20.

## Docs

FastApi `https://fastapi.tiangolo.com/`
Pydantic  `https://docs.pydantic.dev`

## Project Notes

### Tech Stack

* Python
* FastAPI
* SQLAlchemy

### Documents

* 'HTTP Methods' - `https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods`

### Docker

* Remember to update requirements.txt on adding packages.

Set in .env
`FASTAPI_SRC_DIR=/python-fastapi-aourse`
`FAST_API_START_DEV_SERVER=`

### Using 'pipenv'

In 'python-fastapi-course' folder:
`$ pipenv shell`

### Install Packages(Using pipenv)

`$ pipenv install fastapi[all]`

### Run App

`$ uvicorn main:app --reload`


## Python Virtual Environment

### 'pipenv'

#### Install pipenv

`$ pip install pipenv`

#### Create/Activate Environment

In Top Source Directory.

`$ pipenv shell`

* Creates: Pipfile(Toml Format), Pipfile.lock

##### Create Virtual Environment From Pipfile

`$ pipenv install` using Pipfile

#### Change Version

`$ pipenv --python {version}`

#### Install package

`$ pipenv install {package}`
or
`$ pipenv install {package} --dev`

#### Uninstall package

`$ pipenv uninstall {package}`

#### Run in Current Environment

`$ pipenv run python script.py`
or
`$ pipenv run python`

##### Check Environment

In python:
`>>> import sys`
`>>> sys.executable`

#### Install requirements.txt

`$ pipenv install -r requirements.txt`

#### Create requirements.txt

`$ pipenv requirements`

To requirements.txt
`$ pipenv requiements > requirements.txt`

#### Deactivate Virtual Environment

`$ exit`

#### Remove Virtual Environment

`$ pipenv --rm`


### 'venv'

* Built into Python

#### Create Virtual Environment

`$ python -m venv {.venv|name}`

* Creates `.venv|name` directory

#### Activate Virtual Environment

`source .venv/bin/activate`

#### Deactivate Virtual Environment
 
`deactivate`

#### Select Environment

VSCode:
`View > Command Palette > Python: Select Interpreter > Enter interpreter path: .venv/bin/python`
