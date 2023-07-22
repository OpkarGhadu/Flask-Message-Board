import models
from flask import Flask, render_template, request
from flask_cors import CORS

# Server Object
app = Flask(__name__)
CORS(app) #CORS security to protect site resources

# Route to default Index page
@app.route('/', methods=['GET','POST'])
def index():
    # If user is adding a new post
    if request.method == "POST":
        # Info sent by user to POST
        name = request.form.get('name')
        post = request.form.get('post')
        models.create_post(name,post) 

    posts = models.get_posts()
    return render_template('index.html', posts=posts)

# Route to Clear Index page
@app.route('/clear', methods=['POST'])
def clear():
    if request.method == "POST":
        models.delete_posts()
    
    posts = models.get_posts()
    return render_template('index.html', posts=posts)

# Route to About page
@app.route('/about')
def about():
    return render_template('about.html')

# Run Server
if __name__ == '__main__':
    app.run(debug=True)