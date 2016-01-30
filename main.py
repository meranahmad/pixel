from gi.repository import GObject
from tornado import websocket, web, ioloop
import simplejson as json
import scrollphat

class MainHandler(web.RequestHandler):
    def get(self):
        self.render("main.html")

class WebSocketHandler(websocket.WebSocketHandler):
    def initialize(self):
        self._foo= "hello"
        print self._foo

    def open(self):
        print "I am open"

    def on_message(self, message):
        cmd = json.loads(message)
        #{u'raw': 1, u'turned_on': True, u'led': 1}
        if cmd['turned_on']:
            scrollphat.set_pixel(cmd['led'],cmd['raw'],1)
        else:
            scrollphat.set_pixel(cmd['led'],cmd['raw'],0)
        scrollphat.update()

if __name__ == "__main__":
    handlers = [("/main", MainHandler), ("/ws", WebSocketHandler)];
    web.Application(handlers).listen(80)
    ioloop.IOLoop.current().start()
