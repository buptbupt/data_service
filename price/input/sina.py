import pytz
import datetime
from decimal import Decimal

local = pytz.timezone("Asia/Shanghai")


product_list = [
    'sh000001', 'sh000002', 'sh000003',
    'sh000004', 'sh000005', 'sh000006',
    'sh000007', 'sh000008', 'sh000009',
    'sh000010', 'sh000011', 'sh000012',
]


def product_list_gen():
    for i in range(2):
        yield 'sh%06d' % (i)
    for i in range(0):
        yield 'sh6%05d' % (i)


def to_dict(message):
    res = {}
    message = message.split(',')
    for i, k in enumerate([
        'product_abbr_name', 'today_opening_price', 'yesterday_closing_price',
        'current_price', 'highest_price', 'lowest_price', 'buying_price',
        'selling_price', 'dealed_number', 'dealed_amount', 'buying_number_1',
        'buying_price_1', 'buying_number_2', 'buying_price_2',
        'buying_number_3', 'buying_price_3', 'buying_number_4',
        'buying_price_4', 'buying_number_5', 'buying_price_5',
        'selling_number_1', 'selling_price_1', 'selling_number_2',
        'selling_price_2', 'selling_number_3', 'selling_price_3',
        'selling_number_4', 'selling_price_4', 'selling_number_5',
            'selling_price_5', 'price_date', 'price_time', 'status']):
        res[k] = message[i]
    res['product_code'] = res['product_abbr_name'].split('=')[0]
    res['product_abbr_name'] = res['product_abbr_name'].split('=')[-1]
    for k, v in res.items():
        if k in ['today_opening_price', 'yesterday_closing_price'
                 'current_price', 'highest_price', 'lowest_price'
                 'buying_price', 'selling_price', 'buying_price_1',
                 'buying_price_2', 'buying_price_3', 'buying_price_4',
                 'buying_price_5', 'selling_price_1', 'selling_price_2',
                 'selling_price_3', 'selling_price_4', 'selling_price_5']:
            res[k] = Decimal(v)
        if k in ['dealed_number', 'buying_number_1', 'buying_number_2',
                 'buying_number_3', 'buying_number_4', 'buying_number_5',
                 'selling_number_1', 'selling_number_2', 'selling_number_3',
                 'selling_number_4', 'selling_number_5']:
            res[k] = int(v)
    price_time = datetime.datetime.strptime(
        res['price_date'] + " " + res['price_time'], "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(price_time, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    res['price_date'] = str(utc_dt)[:10]
    res['price_time'] = str(utc_dt)[11:19]
    res['create_time'] = datetime.datetime.now()
    res['source'] = 'sina'
    return res
