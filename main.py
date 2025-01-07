from pathlib import Path
import requests
import pandas as pd
import os
import my_functions as mf

GSHEETS_OFFERS = os.environ.get('GSHEETS_OFFERS')
GSHEETS_DESCRIPTIONS = os.environ.get('GSHEETS_DESCRIPTIONS')
SHOPER_OFFERS_FILE_PATH = os.environ.get('SHOPER_OFFERS_FILE_PATH')

SHOPER_COLUMNS_TO_KEEP = [f"images {i}" for i in range(1, 11)] + ["product_code"]

offers_to_create = pd.read_csv(GSHEETS_OFFERS, dtype=str)
product_descriptions = pd.read_csv(GSHEETS_DESCRIPTIONS, dtype=str)
shoper_offers = pd.read_csv(SHOPER_OFFERS_FILE_PATH,
                            sep=';',
                            usecols=SHOPER_COLUMNS_TO_KEEP,
                            dtype=str)

# Merge the DataFrames
merged_df = pd.merge(offers_to_create, product_descriptions, on='Seria', how='left')
final_df = pd.merge(merged_df, shoper_offers, left_on='SKU', right_on='product_code', how='left')

# CSS files
style_path = Path('data/style.css')

if style_path.exists():
    style_contents = style_path.read_text(encoding='utf-8')
    print("Style.css contents loaded successfully.")

# Main function
def main():
    # Create the "products" directory
    products_path = Path("products")
    zipped_products_path = Path("zipped_products")

    products_path.mkdir(exist_ok=True)

    for index, row in final_df.iterrows():  # Loop through the entire DataFrame

        product_folder = products_path / f"{row['PLU']}_{row['Seria'].lower().replace(' ', '_')}"
        product_description = row['Opis']
        img_folder = product_folder / 'img'
        css_folder = product_folder / 'css'

        product_folder.mkdir(exist_ok=True)
        img_folder.mkdir(exist_ok=True)
        css_folder.mkdir(exist_ok=True)

        # Write style.css
        if style_contents:
            (css_folder / "style.css").write_text(style_contents, encoding='utf-8')
            print(f"style.css created in {css_folder}")

        # Download images
        downloaded_images = 0
        for i in range(1, 11):  # Loop through 'images 1' to 'images 10'
            column_name = f"images {i}"
            image_url = row[column_name]

            photo_placeholder = f'[img-{i}]'

            if pd.notna(image_url):  # Check if the URL exists and is not NaN
                try:
                    response = requests.get(image_url, stream=True)
                    if response.status_code == 200:
                        downloaded_images += 1
                        image_path = img_folder / f"z{downloaded_images}.jpg"  # Save as z1, z2, z3, etc.

                        # Replace placeholder with actual image path
                        product_description = product_description.replace(photo_placeholder, f'img/z{downloaded_images}.jpg')

                        with open(image_path, 'wb') as f:
                            for chunk in response.iter_content(1024):
                                f.write(chunk)
                        print(f"Downloaded {image_url} as {image_path}")
                    else:
                        print(f"Failed to download {image_url} (status code: {response.status_code})")
                except Exception as e:
                    print(f"Error downloading {image_url}: {e}")
            else:
                # Replace unused placeholders with the first image (z1.jpg)
                product_description = product_description.replace(photo_placeholder, 'img/z1.jpg')

        # Replace any remaining placeholders with default image path
        for i in range(downloaded_images + 1, 11):
            photo_placeholder = f'[img-{i}]'
            product_description = product_description.replace(photo_placeholder, 'img/z1.jpg')

        # Update the "Opis" column for the current row
        final_df.at[index, 'Opis'] = product_description

        # Save the description as index.html
        (product_folder / "index.html").write_text(product_description, encoding='utf-8')

    # Save the updated DataFrame to Excel
    final_df.to_excel('oferty.xlsx', index=False)
    print("Updated DataFrame saved to 'oferty.xlsx'.")

    mf.zip_all_folders(products_path, zipped_products_path)

if __name__ == "__main__":
    main()
