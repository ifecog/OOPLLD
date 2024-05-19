from parking_lot import (
    VehicleType,
    Vehicle,
    ParkingSpot,
    ParkingRow,
    ParkingLevel,
    ParkingLot
)

def test_parking_lot():
    # Initialize parking lot (1 level, 2 rows each, 5 spots each)
    level1row1 = ParkingRow(row_id=0, num_of_spots=5, spot_type=VehicleType.CAR)
    level1row2 = ParkingRow(row_id=1, num_of_spots=5, spot_type=VehicleType.CAR)
    
    level1 = ParkingLevel(level_id=0, rows=[level1row1, level1row2])
    
    parking_lot = ParkingLot(levels=[level1,])
    
    # Vehicles
    car1 = Vehicle(license_plate='123LAG456', vehicle_type=VehicleType.CAR)
    motorcycle1 = Vehicle(license_plate='123OYO456', vehicle_type=VehicleType.MOTORCYCLE)
    bus1 = Vehicle(license_plate='123OSU456', vehicle_type=VehicleType.BUS)
    
    # Initial available spots
    print('Initial available spots:', parking_lot.get_available_spots())
    
    # Test car parking
    assert parking_lot.park_vehicle(car1) == True


if __name__ == '__main__':
    test_parking_lot()