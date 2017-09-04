# Myplotlib API

Simple API using python Flask and Google Cloud App Engine. 

## Service

The API is available at: https://myplotlib-api.appspot.com

### Examples

* https://myplotlib-api.appspot.com/scatter?x=0,1,2,3,4,5&y=0,4,1,2,3,5
* https://myplotlib-api.appspot.com/barplot?labels=A,B,C&values=3,4,2
* https://myplotlib-api.appspot.com/function?func=x^2&start=-10&end=10

## Usage

To run a local version of the API run the following:

* ```source activate venv```
* ```dev_appserver.py app.yaml```

Deploy changes by running:

* ```gcloud app deploy --project myplotlib-api```

## Setup

0. Create .env file.
* ```cp conf/.env.example conf/.env```

1. Create and activate a virtual environment with python 2.7
*  ```virtualenv -p /usr/bin/python2.7 venv```
* ```source activate venv```

2. Install requirements.
* ```pip install --upgrade -t lib -r requirements.txt```

3. Run setup script.
* ```python setup.py```

## Todo

* Keys.
* Fix histograms.