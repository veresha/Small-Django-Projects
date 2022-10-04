from datetime import datetime


class LoggingUsers:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        req_time = str(datetime.now())
        req_url = str(request.get_raw_uri())
        req_http = str(request.method)

        with open('logs', 'w') as log_file:
            log_file.write(req_time + ' | ' + req_url + ' | ' + req_http)

        response = self.get_response(request)
        return response
