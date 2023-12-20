import flask

app = flask.Flask('My application')

@app.route('/', methods=['GET', 'POST'])
def index():
    request_headers = ''.join([f'{k}: {v}<br>' for k, v in flask.request.headers])
    request_body = flask.request.data
    return f'''This is a response.<br>
----- request details -----<br>
request ip address: { flask.request.remote_addr }<br>
request method: { flask.request.method }<br>
request url: { flask.request.url }<br>
----- request headers -----<br>
{ request_headers }<br>
----- request data -----<br>
{ request_body }<br>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)