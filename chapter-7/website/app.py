from flask import Flask
from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis(host='redis')

@app.route('/')
def hello_world():
    hits = redis.incr('hits')
    return 'You visited {0} times!'.format(hits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
