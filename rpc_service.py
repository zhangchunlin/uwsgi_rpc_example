import uwsgi
import os
import logging

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)

def hello_world():
    pid = os.getpid()
    log.info("%d enter"%(pid))
    os.system("sleep 1")
    log.info("    %s work after sleep"%(pid))
    log.info("%d exit"%(pid))
    return "Hello World from pid %s\n"%(os.getpid())

def test1(s):
    pid = os.getpid()
    log.info("%d enter"%(pid))
    os.system("sleep 3")
    log.info("    %s work after sleep"%(pid))
    log.info("%d exit"%(pid))
    return "test1 from pid %s: %s\n"%(os.getpid(),s)


uwsgi.register_rpc("hello", hello_world)
uwsgi.register_rpc("test1", test1)

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
