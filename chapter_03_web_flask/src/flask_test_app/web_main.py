from flask import Flask, render_template, request, flash, redirect, url_for
from flask_session import Session

# The run path is the parent folder of templates/static
app = Flask(__name__, template_folder='templates', root_path='.', static_folder="static")

# session settings based on files.
app.secret_key = 'I am secret'  # session requires this
app.config['SESSION_TYPE'] = 'filesystem'
# app.config['SESSION_FILE_DIR'] = 'my_folder'  # default to flask_session
Session(app)

# file upload settings
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # limit upload file size
app.config['UPLOAD_EXTENSIONS'] = ['.png']  # limit upload file type
app.config['UPLOAD_FOLDER'] = '/tmp'


# map urls to functions
@app.route('/')  # return a string
def root():
    return "Hello, world"


@app.route('/hello')  # return template with data filling
def hello():
    return render_template('hello_world.html', username='monkey')


@app.route('/bye')  # input GET parameters
def bye():
    flash('get name')  # session is required
    name = request.args.get('name')
    flash('get food')
    food = request.args.get('food')
    return 'bye ' + name + ' ' + food


@app.route('/bye1')
def bye1():
    return redirect(url_for('bye', new_param='new_value', **request.args))


@app.route('/name', methods=['GET', 'POST'])  # GET / POST methods
def full_name():
    if request.method == 'GET':
        return render_template('hello_world1.html')
    elif request.method == 'POST':
        first = request.form.get('fname')
        last = request.form.get('lname')
        return render_template('hello_world1.html', last=last, first=first)


@app.route('/pokemon/<int:num>', )  # rest style
def pokemon(num):
    pokemons = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff",
                "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
    return render_template("pokemon.html", num=num, pokemons=pokemons, len=len(pokemons))


@app.route('/length', methods=['GET', 'POST'])  # HTML form
def length():
    if request.method == 'GET':
        return render_template('length.html')
    elif request.method == 'POST':
        first = request.form.get('first')
        second = request.form.get('second')
        return render_template('length.html', second=second, first=first)


@app.errorhandler(Exception)  # use /bye without parameter to test
def exception_catch(error):  # can pass in 404, 500, error code
    app.logger.exception(error)  # should log this for investigation
    flash('OMG, I saw a bug.')
    # return "error happened!"  # use render_template in real.
    return render_template('error.html')


# we may add more urls from other files
import flask_test_app.web_handlers as web_handlers
app.register_blueprint(web_handlers.stream_urls)

# start web app
if __name__ == '__main__':
    app.run(debug=True)
