from flask import Flask
app = Flask(__name__)

@app.route("/<number>")
def hello(number):
    return 'Hello world! {}'.format(number)

if __name__ == "__main__":
    app.run()