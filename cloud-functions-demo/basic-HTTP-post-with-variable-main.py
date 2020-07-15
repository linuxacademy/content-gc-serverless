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
    return '<html><head></head>\
        <body style="background-color:#060C59;"><div style="height:100%;background-repeat:no-repeat;background-position:center;\
        background-image:url(https://raw.githubusercontent.com/linuxacademy/content-gc-serverless/master/cloud-functions-demo/assets/acg-logo.png);">\
        <h1 style="padding-top:100px;font-size:48px;color:white;text-align:center;">Greetings from A Cloud Guru, {}!</h1>\
        </div></body></html>'.format(escape(name))