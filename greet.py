
from flask import Flask
app=Flask(__name__)

@app.route('/user/<name>')
def user(name):
    return '<h1>Mwaramutse, %s!</h1>' % name


#This displays number in words when you type a digit 0-5
@app.route('/<int:a>')
def counter(a):
    d={0: 'Zero', 1:'number one', 2: 'number two', 3: 'number three', 4: 'number four', 5: 'number five'} 
    return '<h1>%s</h1>' % d.get(a, 'unkown number')
        

if __name__ == '__main__':
    app.run(debug=True)
