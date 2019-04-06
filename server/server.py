from flask import Flask

app = Flask(__name__)


@app.route('/pickupline')
def get_pickup_line():
    return 'Dig. Mig. Spandauer.'

@app.route('/')
def root():
    return "The service for shy people in need of a hookup"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
