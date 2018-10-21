def line(length):
    return '-' * length


ITEM_NAME_LENGTH = 20
ITEM_BRAND_LENGTH = 20

ITEM_INFO_ROW_FORMAT = '{:<20} {:<20} {:<12} {:10}'
ITEM_INFO_HEADER = (f"{'NAME':<20} {'BRAND':<20} {'QUANTITY':<12} {'PRICE':<10}\n"
                    f'{line(20)} {line(20)} {line(12)} {line(10)}')
