from flask import Flask, render_template
app = Flask(__name__)

# linking multiple urls
@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)

@app.route('/shopping')
def shopping():
    food= ["cheese","fries","pizza"]
    return render_template("shopping.html", food = food)
if __name__ == "__main__":
    app.run()  # start this app