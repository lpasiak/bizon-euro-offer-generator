import os

def generate_css_file():

    directory = 'products/css'
    file_path = os.path.join(directory, 'style.css')

    if not os.path.exists(directory):
        os.makedirs(directory)

    # CSS contents
    contents = """
/* css reset */
#prod-desc-container,#prod-desc-container *{box-sizing:border-box}
#prod-desc-container{max-width:920px;margin:0 auto;font-family:Lato,sans-serif}
#prod-desc-container .desc-img,#prod-desc-container .desc-img.lazy{width:initial;max-width:100%;height:auto}

/* custom style */
#prod-desc-container .flex-container{display:flex;flex-wrap:wrap;flex-direction:row}
#prod-desc-container .col{padding:.5em}
#prod-desc-container .col-1{width:100%}
#prod-desc-container .col-2{width:50%}
#prod-desc-container .col-3{width:33.33%}
#prod-desc-container .col.center{justify-content:center;text-align:center;display:flex;flex-wrap:wrap;align-content:flex-start}
@media screen and (max-width:919px){
#prod-desc-container{font-size:14px;max-width:100%}
#prod-desc-container .col-1,#prod-desc-container .col-2,#prod-desc-container .col-3{width:100%}
#prod-desc-container .flex-container.revert{flex-direction:column-reverse}}"""

    with open(file_path, 'w') as file:
        file.write(contents)

    print(f"CSS file created at: {file_path}")