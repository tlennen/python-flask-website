from flask import Flask, request as req

# Flask object, name helps us with connecting it to images and css
app = Flask(__name__)


# Root directory is '/', represents sub pages, ties url to python functions
# '@' is a decorator, way to wrap a function and modify its behavior
@app.route('/')
# customary to name after page name
def index():
    return "This is the home page "


@app.route('/tuna')
# html can be returned
def tuna():
    return "<h2>Tuna is good</h2?"


@app.route('/profile/<username>')
# can save variables with urls
def profile(username):
    return "<h2>Hey there %s</h2>" % username


@app.route('/post/<int:post_id>')
# need type for integers, otherwise it is string
def post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id


@app.route('/request')
# Shows that GET is used when requesting page
def request():
    return "<h2>Method used is %s</h2>" % req.method


@app.route('/bacon', methods=['GET', 'POST'])
# enables post requests on page
def bacon():
    return "<h2>Method used is %s</h2>" % req.method


# Runs only if script is run directly (no imports)
if __name__ == "__main__":
    app.run(debug = True)  # start this app