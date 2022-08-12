# currency-converter
 currency converter

<hr>
Home screen
<img src="static/images/currency-converter-1.png" width="700">
<hr>
Choose currencies and enter amount
<img src="static/images/currency-converter-2.png" width="700">
<hr>
Get result
<img src="static/images/currency-converter-3.png" width="700">
<hr>

### Setup

<hr>

Clone repo and create a virtual environment
```
$ git clone https://github.com/giedriusstankauskas/currency-converter.git
$ cd currency-converter
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install -r requirements.txt
```

Start Flask app.
```
$ (venv) export FLASK_APP=app.py
$ (venv) flask run
```