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
    return render_template('users.html', 
                           user_names=user_names,
                           names_count = len(total_user_names()),
                           interests_count = len(total_user_interests())
                           )

@app.route('/users/<user_name>')
def user_page(user_name):

    if user_name in g.users_data.keys():
        user_data = g.users_data[user_name]

        user_email = user_data['email']
        user_interests = user_data['interests']
        user_names = [name for name in list(g.users_data.keys()) if name != user_name]

        return render_template('users_data.html', 
                               user_name=user_name,
                               user_email=user_email,
                               user_interests=user_interests,
                               user_names=user_names,
                               names_count = len(total_user_names()),
                               interests_count = len(total_user_interests())
                               )
    
    return redirect('/users')

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

def total_user_interests():
    interests = [interest for user_data in g.users_data.values() 
                 for interest in user_data['interests']]
    
    return interests

def total_user_names():

    user_names = list(g.users_data.keys())

    return user_names


if __name__ == '__main__':
    app.run(debug=True, port=5003)