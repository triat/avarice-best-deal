#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from bs4 import BeautifulSoup


def main():
    """ Main entry point of the app """
    with open('page.html', 'r') as f:
        html = BeautifulSoup(f.read(), 'html.parser')


    sell_blocks = html.find_all(class_='itm')
    all_block = list()

    for sell_block in sell_blocks:
        sell_block_stacked = sell_block.find(class_='v-i-4').text
        sell_block_dividend = sell_block.select('span[class*="v-i-5-"]')[0].text
        sell_block_bonus = sell_block.find(class_='v-i-6').text
        sell_block_buy_price = sell_block.find(class_='v-i-7').text

        block = {
                'stacked': int(sell_block_stacked.split(' ')[0].split('.')[0]),
                'dividend': int(sell_block_dividend.split(' ')[0].split('.')[0]),
                'bonus': int(sell_block_bonus.split(' ')[0].split('.')[0]),
                'buy_price': int(sell_block_buy_price.split(' ')[2].split('.')[0]),
            }

        price_per_bavc = (block['buy_price'] - block['dividend']) / block['stacked']
        block['price_per_bavc'] = price_per_bavc

        all_block.append(block)

    max_price_possible = 200000
    best_price = 999999
    best_block = dict()
    for block in all_block:
        if block['price_per_bavc'] < best_price and block['buy_price'] < max_price_possible:
            best_price = block['price_per_bavc']
            best_block[best_price] = block
        
    print(best_block)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
