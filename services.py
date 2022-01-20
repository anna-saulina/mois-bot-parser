# выделение массы продукта из строки
import json
import math

# CONSTANTS
MEASURE = ('кг', 'кг.', 'килограмм', 'г', 'гр', 'г.', 'гр.', 'грамм')
KILOGRAM = ('кг', 'кг.', 'килограмм')
GRAM = ('г', 'гр', 'г.', 'гр.', 'грамм')


def load_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as input_file:
        data = json.load(input_file)
        return data


def extract_ozon_product_weight(title):
    title_list = title.split(',')
    # print(title_list)
    if title and len(title_list) > 1:
        weight_list = title_list[1].strip().split()
        # print(weight_list)
        if len(weight_list) > 1:
            try:
                weight = int(weight_list[-2].strip())
            except ValueError:
                weight = None
            measure = weight_list[-1].strip()

            if measure.lower() in MEASURE:
                measure = measure.lower()
            else:
                measure = None

            weight_measure = (weight, measure)
            # print(weight, measure)

            return weight_measure


def extract_okey_product_weight(title=None):
    try:
        title_list = title.split()
    except AttributeError:
        title_list = []

    weight = 0
    measure = ''

    # print(title_list)
    if title_list and len(title_list) > 1:
        try:
            weight = float(title_list[-1][0:-1])
            measure = title_list[-1][-1]
        except ValueError:
            weight = None
            measure = None

    if weight is None:
        try:
            weight = float(title_list[-1][0:-2])
            measure = title_list[-1][-2:]
        except ValueError:
            weight = None
            measure = None

    if weight is None:
        try:
            weight = float(title_list[-2][0:-1])
            measure = title_list[-2][-1]
        except:
            weight = None
            measure = None
        # print(weight_list)

    if measure and measure.lower() in MEASURE:
        measure = measure.lower()
    else:
        measure = None

    weight_measure = (weight, measure)
    # print(weight, measure)

    return weight_measure


def parse_price(price_data):
    converted_price = 0.0
    if price_data:
        if len(price_data) == 2:
            price_list = price_data[0].split(',')
            integer_part_hundred = float(price_list[0])
            decimal_part = float(price_list[1]) / 100
            converted_price = integer_part_hundred + decimal_part
        if len(price_data) == 3:
            price_list = price_data[1].split(',')
            integer_part_thousand = float(price_data[0]) * 1000
            integer_part_hundred = float(price_list[0])
            decimal_part = float(price_list[1]) / 100
            converted_price = integer_part_thousand + integer_part_hundred + decimal_part

        # print(f'Converted price: {converted_price}')
        return converted_price


def find_minimum_price(product_data):
    minimum_price_product = {}
    minimum_price = math.inf
    for product in product_data:
        if product['price_kg'] and product['price_kg'] > 0:
            if product['price_kg'] < minimum_price:
                minimum_price_product = product
                minimum_price = product['price_kg']

    return minimum_price_product


if __name__ == '__main__':
    # price_list = load_json('./ozon_price.json')
    # print(price_list)
    #
    # for element in price_list:
    #     title = element['title']
    #     weight_measure = extract_ozon_product_weight(title)
    #     print(weight_measure)
    #     # print(title)

    price_list = load_json('./okey_price.json')
    print(price_list)

    # for element in price_list:
    #     title = element['title']
    #     weight_measure = extract_okey_product_weight(title)
    #     print(weight_measure)

    print(find_minimum_price(price_list))


    # parse_price(['1', '899,00', '₽'])
    # parse_price(['899,00', '₽'])
