from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    items = ["Javascript", "Python", "SQL", "CSS"]
    return render_template('home.html', title="Home Page", name="Fidel", items=items)

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return render_template('greet.html', title="Greeting Page", username=username)


@app.route('/about')
def about():
    return render_template('about.html', title="About Page")

if __name__ == '__main__':
    app.run(debug=True)
