from fastapi import APIRouter, Query, Path, Response
from controllers.vehicle_controller import get_vehicle_vin, get_vehicles


router = APIRouter(prefix="/api", tags=["Vehicle Inventory"])


@router.get("/vehicles/{vin}")
async def get_vehicle_by_vin(
    response: Response,
    vin: str = Path(
        title="Vehicle Identification Number",
        description="Vehicle Identification Number",
        examples=["3C63D2CLXCG266815"],
        pattern="^[A-Z0-9]{17}$",
    ),
):
    """
    A GET endpoint to get vehicle details based on the provided VIN.

    Parameters:
    - vin: The vehicle identification number (VIN) of the vehicle.

    Returns:
    - A dictionary containing the vehicle details if found, otherwise an error message.
    """
    data = get_vehicle_vin(vin)
    if "error" in data:
        response.status_code = 404
        return data

    response.status_code = 200
    return data


@router.get("/vehicles")
async def get_vehicle_by_params(
    response: Response,
    make: str = Query(
        title="Make", default=None, description="Make", examples=["Toyota"]
    ),
    model: str = Query(
        title="Model", default=None, description="Model", examples=["Camry"]
    ),
    price_range: str = Query(
        title="Price Range",
        default="10000-200000",
        description="Price Range",
        examples=["1000-2000"],
    ),
):
    """
    A GET endpoint to get vehicle details based on the provided parameters.

    Parameters:
    - year: The year of the vehicle.
    - make: The make of the vehicle.
    - model: The model of the vehicle.

    Returns:
    - A dictionary containing the vehicle details if found, otherwise an error message.
    """
    data = get_vehicles(make, model, price_range)
    if "error" in data:
        response.status_code = 404
        return data

    response.status_code = 200
    return data
