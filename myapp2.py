from flask import Flask

app = Flask(__name__)


@app.route('/')
def admin():
    return "<body style=background-color:pink ><h1>Admin</h1>"


@app.route('/guest/')
def guest():
    return "<body style=background-color:blue ><h1>Guest</h1>"


@app.route('/username/')
def username():
    return "<body style=background-color:purple ><h1>Username</h1>"


if __name__ == '__main__':
    app.debug = True
    app.run()


# Create a new Flask app in directory Flask_lesson2
# create a python app file called app2
# Add the following route
# admin- Display This is the admin page Add background colour to pink
# guest - Display This is the guest page Add background colour to blue
# username- Display This is the user page Add background colour to purle
