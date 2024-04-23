from flask import Flask # this is the flask package

app = Flask(__name__)


@app.route('/') # default api
def home():
    return "Welcome to azure and flask webpage"


@app.route('/rosemonkey/api/signup') # create the another api
def user_signup():
    return "this is the user signup page"




if __name__ =="__main__":
    app.run(debug=True)