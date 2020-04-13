from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    x = 8
    y = 8
    return render_template('index.html', x=x, y=y)

@app.route('/<int:height>')
def adjHeight(height):
    x = 8
    y = height
    return render_template('index.html', x=x, y=y)

@app.route('/<int:width>/<int:height>')
def adjBoth(width, height):
    x = width
    y = height
    return render_template('index.html', x=x, y=y) 

if __name__ =='__main__':
    app.run(debug=True)