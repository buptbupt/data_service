import time
import websocket
import threading
import _thread as thread
from app import app
from util.db import db
from price.input.ops import *
from price.input.sina import to_dict as sina_to_dict
from price.input.sina import product_list as sina_product_list


def on_sina_message(ws, message):
    price_dict = sina_to_dict(message)
    create_price_obj(price_dict)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(360):
            time.sleep(60)
            ws.send("")
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


def get_sina_data(product_code):
    ws = websocket.WebSocketApp(
        "wss://hq.sinajs.cn/wskt?list={}".format(product_code),
        on_message=on_sina_message,
        on_error=on_error,
        on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


if __name__ == "__main__":
    app.app_context().push()
    db.init_app(app)
    websocket.enableTrace(True)
    for product_code in sina_product_list:
        new_thread = threading.Thread(
            target=get_sina_data, args=(product_code,))
        new_thread.start()
