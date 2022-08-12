from flask import Flask, render_template
from models import ConvertForm
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/', methods=["GET", "POST"])
def index():
    form = ConvertForm()
    api_key = os.getenv('API_KEY')
    return render_template('index.html', form=form, api_key=api_key)


if __name__ == '__main__':
    app.run(debug=True)
