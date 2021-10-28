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
    return "Hi " + name + "!"

@app.route('/repeat/<number>/<input>')
def repeat(number, input):
    x = int(number)
    print(int(number))
    print(input)
    return  input * x

if __name__=="__main__":
    app.run(debug=True)

