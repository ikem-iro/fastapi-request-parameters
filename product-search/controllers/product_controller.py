from config.file_config import read_file


def filter_products(product_name, price_range, category):
    """
    A function that filters products based on product name, price range, and category.
    
    Parameters:
    - product_name (str): The name of the product to filter by.
    - price_range (str): The price range in the format "min_price-max_price" to filter by.
    - category (str): The category of the product to filter by.
    
    Returns:
    - dict: A dictionary containing the filtered products or a message if no products fit the provided parameters.
    """
    products = read_file()
    product_name = product_name
    category = category
    price_range = price_range    


    if not any([product_name, price_range, category]):
        return {"products": products}

    filtered_products = []
    for product in products:
        if product_name and product_name.lower() not in product['product_name'].lower():
            continue
        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            if not min_price <= product['price'] <= max_price:
                continue
        if category and category.lower() != product['category'].lower():
            continue
        filtered_products.append(product)

    if not filtered_products:
        return{"message": "No product found that fits the provided parameters"}
    
    return {"products": filtered_products}   
        


