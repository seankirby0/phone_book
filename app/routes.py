from app.forms import Add_phone_number
from app import app
from flask import render_template
from app.forms import Add_phone_number


@app.route('/', methods = ['GET', 'POST'])
def home():
    form = Add_phone_number()
    if form.validate_on_submit():
        print('THE FORM IS VALID!!!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        print(first_name, last_name, phone_number)
    return render_template('home.html', form = form)