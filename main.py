import pandas as pd
import os
import functions

GSHEETS_OFFERS = os.environ.get('GSHEETS_OFFERS')
GSHEETS_DESCRIPTIONS = os.environ.get('GSHEETS_DESCRIPTIONS')
SHOPER_OFFERS_FILE_PATH = os.environ.get('SHOPER_OFFERS_FILE_PATH')

offers_to_create = pd.read_csv(GSHEETS_OFFERS)
product_descriptions = pd.read_csv(GSHEETS_DESCRIPTIONS)
shoper_offers = pd.read_csv(SHOPER_OFFERS_FILE_PATH, sep=';')

functions.generate_css_file()

print(shoper_offers)