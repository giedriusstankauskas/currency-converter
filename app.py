from flask import Flask, render_template
from models import ConvertForm
from converter import convert

app = Flask(__name__)
app.secret_key = "whatever-secret-key"


@app.route('/', methods=["GET", "POST"])
def index():
    form = ConvertForm()
    if form.validate_on_submit():
        to_ = form.to.data
        from_ = form.from_.data
        amount = form.amount.data
        convert(to_, from_, amount)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)