from flask import render_template
from version import app

@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")



@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found"), 404
