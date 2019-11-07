from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

@app.route('/fortune')
def fortune():
    #returns fortune options
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    #displays user's fortune
    user_color = request.args.get('color')

    if user_color == 'red':
        fortune = "you like red"

    elif user_color == 'green':
        fortune = "you like green"

    elif user_color == 'orange':
        fortune = "you like orange"

    elif user_color == 'own':
        fortune = "you rock"

    else:
        fortune = "goodbye"

    return render_template('fortune_results.html', fortune=fortune)