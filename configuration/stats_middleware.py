import time


class StatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        response["X-Response-Time"] = f'{round(duration * 1000, 3)}ms'
        response["Access-Control-Expose-Headers"] = "X-Response-Time"

        return response
