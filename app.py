from flask import Flask, render_template 

from controllers.destination_controller import destinations_blueprint
from controllers.traveller_controller import travellers_blueprint

app = Flask(__name__)

app.register_blueprint(destinations_blueprint)
app.register_blueprint(travellers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)