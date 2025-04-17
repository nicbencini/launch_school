from flask import Flask, render_template, g, redirect
import yaml

app = Flask(__name__)

@app.before_request
def load_data():
    with open('data/users.yaml', 'r') as file:
        g.users_data = yaml.safe_load(file) 

@app.route('/')
def index():

    return redirect('/users')

@app.route('/users')
def users():
    user_names = list(g.users_data.keys())
    return render_template('users.html', user_names=user_names)

@app.route('/users/<user_name>')
def user_page(user_name):

    if user_name in g.users_data.keys():
        return user_name
    
    return redirect('/users')

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run(debug=True, port=5003)