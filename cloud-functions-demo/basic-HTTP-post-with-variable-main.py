from flask import escape

def greetings_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'my friend'
    return '<html><head>\
        <style>body { background-color:#060C59; } div {width: 75%; height: 100%; \
        background-image-url: https://raw.githubusercontent.com/linuxacademy/content-gc-serverless/master/cloud-functions-demo/assets/acg-logo.png} \
        div h1 { margin-top: 80px; font-size: 48px; color: white;}</style></head>\
        <body><div>\
        <h1>Greetings from A Cloud Guru, {}!</h1>\
        </div></body></html>'.format(escape(name))