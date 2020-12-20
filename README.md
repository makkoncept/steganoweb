# Steganoweb
Basic web wrapper of the Stegano (https://github.com/cedricbonhomme/Stegano/) library.

## Live

View it live at : https://steganoweb.herokuapp.com/

You can deploy your own instance on heroku by clicking the following button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Run locally

- clone the repo
```
git clone https://github.com/makkoncept/steganoweb.git
cd steganoweb
```
- create a virtual environment and install requirements
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
- run the development server
```
python run.py
```
visit http://localhost:5000/ 
