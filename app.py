from flask import Flask ,render_template # this is the flask package       # syntax

app = Flask(__name__)      #syntax

@app.route('/rosemonkey/api/home') # default api
def home():
    return render_template("home.html")



@app.route('/rosemonkey/api/about')  # thia is also api
def about():
    return render_template("about.html")


@app.route('/rosemonkey/api/address.hari') # this is also api
def address():
    return render_template("address.html")




@app.route('/rosemonkey/api/contact')  # this  ia also api
def contact():
    return render_template("contact.html")





@app.route('/rosemonkey/api/signup') # create the another api
def user_signup():
    return render_template('signup.html')



@app.route('/rosemonkey/api/login') # create the another api
def user_login():
    return "this is user login page"



@app.route('/rosemonkey/api/menu') # create the another api
def menu():
    return render_template('menu.html')




if __name__ =="__main__":         #syntax
    app.run(debug=True,host='0.0.0.0')