from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from service.Service import Service

app = Flask(__name__)

service = Service()

metrics = PrometheusMetrics(app, group_by='endpoint')

@app.route('/service', methods=['POST'])
def register_service():  # put application's code here
    return service.add_service()


@app.route('/service', methods=['GET'])
def get_service_info():
    # put application's code here
    return service.get_service()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
