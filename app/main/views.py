from . import main
from flask import render_template

@main.route('/')
def index():
    title = "Pitch | Home"
    return render_template('index.html', title = title)

@main.route("/new/pitch")
@login_required
def new_post():
    title = "Create Pitch"
    return render_template("new_pitch.html", title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)
