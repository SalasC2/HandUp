from flask import render_template, flash, redirect
from app import app
from app.models import Company, Need

@app.route('/')
@app.route('/index')
def index():
    return render_template("home/index2.html")

@app.route('/companies')
def companies():
    companies = Company.query.all() 
    # needs = Need.filter_by(company=company)
    return render_template("company/index.html", companies=companies)

@app.route('/companies/<id>/')
def company(id):
    company = Company.query.filter_by(id=1).first()
    print(company)

    needs = Need.query.filter_by(company=company)
    return render_template("company/profile.html", company=company, needs=needs)



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect('/index')
#     return render_template('user/login.html', title='Sign In', form=form)