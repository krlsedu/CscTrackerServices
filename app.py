from flask import Flask

from service.Service import Service

app = Flask(__name__)

service = Service()

@app.route('/service', methods=['POST'])
def register_service():  # put application's code here
    return service.add_service()


@app.route('/service', methods=['GET'])
def get_service_info():
    # put application's code here
    return service.get_service()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
