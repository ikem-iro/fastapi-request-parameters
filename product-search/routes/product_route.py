from fastapi import APIRouter, Query, Response
from controllers.product_controller import filter_products


router = APIRouter(prefix='/api', tags=["Filter Products"])



@router.get('/products')
async def search_product( response: Response, product_name: str = Query(default=None, description="Product Name"), price_range: str = Query(default=None, description="Price Range"), category: str = Query(default=None, description="Category")):
    """
    A function to search for products based on the provided parameters.
    
    Parameters:
    - response: The response object to send back the search results.
    - product_name: The name of the product to search for.
    - price_range: The price range to filter the products.
    - category: The category of the product to search for.
    
    Returns:
    - A message indicating the search results or a message if no product is found.
    """

    message = filter_products(product_name, price_range, category)
    if message == {"message": "No product found that fits the provided parameters"}:
        response.status_code = 404
        return message
    response.status_code = 200
    return message
