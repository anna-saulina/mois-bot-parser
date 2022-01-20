# выделение массы продукта из строки
import json


# CONSTANTS
MEASURE = ('кг', 'кг.', 'килограмм', 'г', 'гр', 'г.', 'гр.', 'грамм')


def load_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as input_file:
        data = json.load(input_file)
        return data


def extract_product_weight(title):
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




if __name__ == '__main__':
    price_list = load_json('./ozon_price.json')
    print(price_list)

    for element in price_list:
        title = element['title']
        weight_measure = extract_product_weight(title)
        print(weight_measure)
        # print(title)
