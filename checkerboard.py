from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    x = 8
    y = 8
    rsc = 'red'
    bsc = 'black'
    return render_template('index.html', x=x, y=y, rsc=rsc, bsc=bsc)

@app.route('/<int:height>')
def adjHeight(height):
    x = 8
    y = height
    rsc = 'red'
    bsc = 'black'
    return render_template('index.html', x=x, y=y, rsc=rsc, bsc=bsc)

@app.route('/<int:width>/<int:height>')
def adjwidthHeight(width, height):
    x = width
    y = height
    rsc = 'red'
    bsc = 'black'
    return render_template('index.html', x=x, y=y, rsc=rsc, bsc=bsc)

@app.route('/<int:width>/<int:height>/<string:redSquareColor>/<string:blackSquareColor>')
def adjWidthHeightColor(width, height, redSquareColor, blackSquareColor):
    x = width
    y = height
    rsc = redSquareColor
    bsc = blackSquareColor
    return render_template('index.html', x=x, y=y, rsc=rsc, bsc=bsc)

if __name__ =='__main__':
    app.run(debug=True)