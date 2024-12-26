import pandas as pd
import os
import functions

GSHEETS_OFFERS = os.environ.get('GSHEETS_OFFERS')
GSHEETS_DESCRIPTIONS = os.environ.get('GSHEETS_DESCRIPTIONS')
SHOPER_OFFERS_FILE_PATH = os.environ.get('SHOPER_OFFERS_FILE_PATH')

shoper_columns_to_keep = ['product_code', 
                          'images 1',
                          'images 2',
                          'images 3',
                          'images 4',
                          'images 5',
                          'images 6',
                          'images 7',
                          'images 8',
                          'images 9',
                          'images 10']

offers_to_create = pd.read_csv(GSHEETS_OFFERS)
product_descriptions = pd.read_csv(GSHEETS_DESCRIPTIONS)
shoper_offers = pd.read_csv(SHOPER_OFFERS_FILE_PATH, sep=';', usecols=shoper_columns_to_keep)


print(shoper_offers)

functions.generate_css_file()
