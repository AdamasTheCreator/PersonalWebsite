from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/aboutadamas')
def aboutadamas():
    return render_template('aboutadamas.html')

@app.route('/abouteasy')
def abouteasy():
    return render_template('abouteasy.html')

@app.route('/abouteffi')
def abouteffi():
    return render_template('abouteffi.html')

if __name__ == '__main__':
    app.run(debug=True)
