from flask import request

from service.Interceptor import Interceptor


class Service(Interceptor):
    def __init__(self):
        self.services = {}

    def get_service(self):
        name = request.args.get('service')
        try:
            name_ = self.services[name]
            return name_
        except:
            return None

    def add_service(self):
        json = request.get_json()
        self.services[json['serviceName']] = json
