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
            'selling_price_5', 'date', 'time', 'status']):
        res[k] = message[i]
    return res
