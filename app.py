from flask import Flask ,render_template # this is the flask package

app = Flask(__name__)


@app.route('/') # default api
def home():
    return render_template("home.html")

@app.route('/rosemonkey/api/about')
def about():
    return render_template("about.html")

@app.route('/rosemonkey/api/address.hari')
def address():
    return render_template("address.html")


@app.route('/rosemonkey/api/contact')
def contact():
    return render_template("contact.html")



@app.route('/rosemonkey/api/signup') # create the another api
def user_signup():
    return render_template('signup.html')


@app.route('/rosemonkey/api/login') # create the another api
def user_login():
    return "this is user login page"

if __name__ =="__main__":
    app.run(debug=True)