import time
import websocket
import _thread as thread
from app import app
from util.db import db
from price.input.ops import *
from price.input.sina import to_dict as sina_to_dict



def on_sina_message(ws, message):
    price_dict = sina_to_dict(message)
    create_price_obj(price_dict)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(60):
            time.sleep(60)
            ws.send("")
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    app.app_context().push()
    db.init_app(app)
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://hq.sinajs.cn/wskt?list=sh000001",
                                on_message=on_sina_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
