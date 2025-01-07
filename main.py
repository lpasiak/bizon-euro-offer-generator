from pathlib import Path
import requests
import pandas as pd
import os

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

offers_to_create = pd.read_csv(GSHEETS_OFFERS, dtype=str)
product_descriptions = pd.read_csv(GSHEETS_DESCRIPTIONS, dtype=str)
shoper_offers = pd.read_csv(SHOPER_OFFERS_FILE_PATH,
                            sep=';',
                            usecols=shoper_columns_to_keep,
                            dtype=str)

# Merge the DataFrames
merged_df = pd.merge(offers_to_create, product_descriptions, on='Seria', how='left')
final_df = pd.merge(merged_df, shoper_offers, left_on='SKU', right_on='product_code', how='left')

final_df.to_excel('oferty.xlsx', index=False)
print(final_df)

# Main function
for index, row in final_df.iterrows():
    product_folder = Path(f'{row['PLU']}_{row['Seria'].lower().replace(' ', '_')}')
    img_folder = Path.joinpath(product_folder, 'img')

    print(f'{row['SKU']}: {row['Nazwa']}')

    product_folder.mkdir(exist_ok=True)
    img_folder.mkdir(exist_ok=True)

# Create a CSS file
# functions.generate_css_file()
