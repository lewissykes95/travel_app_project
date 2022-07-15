from distutils.log import debug
from flask import Flask, render_template 

from controllers.destination_controller import destination_blueprint
from controllers.traveller_controller import traveller_blueprint

app = Flask(__name__)

app.register_blueprint(destination_blueprint)
app.register_bluprint(traveller_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)