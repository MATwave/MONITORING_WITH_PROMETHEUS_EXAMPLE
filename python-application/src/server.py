import time

from flask import Response, Flask
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

graphs = {
    'REQUEST_COUNT': Counter('python_request_operations_total',
                             'The total number of processed requests'),
    'REQUEST_LATENCY': Histogram('python_request_duration_seconds',
                                 'Histogram for the duration in seconds.',
                                 buckets=(1, 2, 5, 6, 10, float("inf")))
}


@app.route("/")
def hello():
    graphs['REQUEST_COUNT'].inc()

    with graphs['REQUEST_LATENCY'].time():
        time.sleep(0.600)
        return "Hello World!"


@app.route("/metrics")
def requests_count():
    res = [generate_latest(v) for v in graphs.values()]
    return Response(res, mimetype="text/plain")
