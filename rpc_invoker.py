import uwsgi

def application(env, start_response):
    start_response('200 Ok', [('Content-Type', 'text/html')])
    return uwsgi.rpc('127.0.0.1:3031', 'hello')
