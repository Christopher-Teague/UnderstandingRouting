from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/Dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def hello(name):
    print(name)
    return f"Hi {name}!"

@app.route('/repeat/<int:number>/<input>')
def repeat(number, input):
    print(number)
    print(input)
    return input * number

if __name__=="__main__":
    app.run(debug=True)

