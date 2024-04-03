from config.file_config import read_file





def get_vehicle_vin(num):
    vehicles = read_file()

    for vehicle in vehicles:
        if vehicle["vin"] == num:
            return vehicle
            
    return {"error": "Vehicle not found"}

       



def get_vehicles(make, model, price_range):
    
    vehicles = read_file()

    if not any([make, model, price_range]):
        return vehicles

    filtered_vehicles = []
    for vehicle in vehicles:
        if model and model.lower() not in vehicle['car_model'].lower():
            continue
        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            if not min_price <= vehicle['price'] <= max_price:
                continue
        if make and make.lower() != vehicle['car_make'].lower():
            continue
        filtered_vehicles.append(vehicle)

    if not filtered_vehicles:
        return {"error": "No vehicle found that fits the provided parameters"}

    return filtered_vehicles