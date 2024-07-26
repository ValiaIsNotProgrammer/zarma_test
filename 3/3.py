import csv
import json

import pandas as pd


def print_joined_v1():
    "Работает, только если данные отсортированы"
    with open('sales.json') as sales_file, \
         open('goods.csv') as goods_file:

        sales = json.load(sales_file)
        goods = csv.DictReader(goods_file)
        print("product_id", "sale_id", "amount", "product_name")
        for sale, good in zip(sales, goods):
            print(list((sale | good).values()))


def print_joined_v2():
    goods_df = pd.read_csv('goods.csv')

    with open('sales.json', 'r') as file:
        sales = json.load(file)

    sales_df = pd.DataFrame(sales)

    merged_df = pd.merge(goods_df, sales_df, on='product_id', how='left')

    print(merged_df)

