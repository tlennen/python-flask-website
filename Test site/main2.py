from flask import Flask, render_template

# Flask object, name helps us with connecting it to images and css
app = Flask(__name__)


# Root directory is '/', represents sub pages, ties url to python functions
# '@' is a decorator, way to wrap a function and modify its behavior
@app.route('/')
# customary to name after page name
def index():
    return "This is the home page "

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name = name)

# Runs only if script is run directly (no imports)
if __name__ == "__main__":
    app.run(debug = True)  # start this app