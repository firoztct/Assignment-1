mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

import random

ex_rate = mobile_data.get("exchnage_rate")
all_data = mobile_data.get("data")

for data in all_data:
    mobile_name = data.get("name")
    country = data.get("made")
    usd_price = data.get("price")
    usd_price = usd_price.strip(" USD")
    usd_price = float(usd_price)
    bd_price = round(usd_price * ex_rate)

    sentence1 = [f'{country} has launched a new smartphone, which name is {mobile_name}. ',
                    f'Let\'s introduce the newly launched smartphone, model {mobile_name}. ',
                    f'{mobile_name}, is one of the most popular smartphone. ',
                    ]
    sentence2 = [f'The {mobile_name} Made in {country}.',
                    f'The Smartphone comes from {country}.',
                    f'{mobile_name} is made by {country}.',
                    ]

    sentence3 = [f'This Smartphone price is only {usd_price} USD which is almost equal to {bd_price} BDT. ',
                        f'At present {mobile_name} is one best budget Smratphone in the world, which global price is {usd_price} & Bangladeshi price is only {bd_price} BDT.',
                        f'Do you know what is the price of this handset? It\'s price is only {usd_price} USD or {bd_price} BDT.',
                    ]
    final_template = random.choice(sentence1) + random.choice(sentence2) + random.choice(sentence3)
    print(final_template)