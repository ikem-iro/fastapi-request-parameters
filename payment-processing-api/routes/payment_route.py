from fastapi import APIRouter, Response
from models.payment_model import PaymentModel
from controllers.payment_controller import complete_transaction


router = APIRouter(prefix='/api', tags=['Payment Processing'])



@router.post('/payments')
async def make_payment(payment: PaymentModel, response: Response):
    """
    A POST endpoint to process payments.
    
    Parameters:
    - payment: PaymentModel
    - response: Response
    
    Returns:
    - data: dict
    """
    data = complete_transaction(payment)

    if "error" in data:
        response.status_code = 400
        return data
    response.status_code = 200
    return data
    
