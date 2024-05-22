from enum import Enum

class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    BUS = 3
    
    
class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        
    
    def get_type(self):
        return self.vehicle_type
    
    
    def get_license_plate(self):
        return self.license_plate
    

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: VehicleType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None
    
        
    def is_available(self):
        return self.vehicle is None
    
      
    def can_fit_vehicle(self, vehicle: Vehicle):
        return vehicle.get_type().value <= self.spot_type.value
    
    
    def park_vehicle(self, vehicle: Vehicle):  
        if self.is_available and self.can_fit_vehicle(vehicle):
            self.vehicle = vehicle
            return True
        return False
        
    
    def remove_vehicle(self):
        self.vehicle = None
        
        
class ParkingRow:
    def __init__(self, row_id: int, num_of_spots: int, spot_type: VehicleType):
        self.row_id = row_id
        self.spots = [ParkingSpot(i, spot_type) for i in range(num_of_spots)]
        
        
    def park_vehicle(self, vehicle: Vehicle):
        for spot in self.spots:
            if spot.park_vehicle(vehicle):
                return True
        return False
    
    
    def remove_vehicle(self, vehicle: Vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                spot.remove_vehicle()
                return True
        return False
    
    
    def get_available_spots(self):
        return sum(spot.is_available() for spot in self.spots)
    
    
    def is_spot_available(self, spot_id: int):
        if 0 <= spot_id < len(self.spots):
            return self.spots[spot_id].is_available()
        return False
    
    
class ParkingLevel:
    def __init__(self, level_id: int, rows: [ParkingRow]):
        self.level_id = level_id
        self.rows = rows
        
        
    def park_vehicle(self, vehicle: Vehicle):
        for row in self.rows:
            if row.park_vehicle(vehicle):
                return True
        return False
    
    
    def remove_vehicle(self, vehicle: Vehicle):
        for row in self.rows:
            if row.remove_vehicle(vehicle):
                return True
        return False
    
    
    def get_available_spots(self):
        return sum(row.get_available_spots() for row in self.rows)
    
    
    def is_spot_available(self, row_id: int, spot_id: int):
        if 0 <= row_id < len(self.rows):
            return self.rows[row_id].is_spot_available(spot_id)
        return False
    

class ParkingLot:
    def __init__(self, levels: [ParkingLevel]):
        self.levels = levels
        
        
    def add_level(self, level: ParkingLevel):
        return self.levels.append(level)
    
    
    def park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
    
    
    def remove_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.remove_vehicle(vehicle):
                return True
        return False
    
    
    def get_available_spots(self):
        return sum(level.get_available_spots() for level in self.levels)
    
    
    def is_spot_available(self, level_id: int, row_id: int, spot_id: int): 
        if 0 <= level_id < len(self.levels):
            return self.levels[level_id].is_spot_available(row_id, spot_id)
        return False


# # Example usage
# # Define a parking lot with 1 level, 2 rows per level, and 5 spots per row
# level1_row1 = ParkingRow(row_id=0, num_of_spots=5, spot_type=VehicleType.CAR)
# level1_row2 = ParkingRow(row_id=1, num_of_spots=5, spot_type=VehicleType.CAR)

# level1 = ParkingLevel(level_id=0, rows=[level1_row1, level1_row2])

# parking_lot = ParkingLot(levels=[level1,])

# # Add vehicles
# car = Vehicle(license_plate='123LAG456', vehicle_type=VehicleType.CAR)
# motorcycle = Vehicle(license_plate='123OYO456', vehicle_type=VehicleType.MOTORCYCLE)
# bus = Vehicle(license_plate='123OSU456', vehicle_type=VehicleType.BUS)

# # Park vehicle
# print(parking_lot.park_vehicle(car))
# # print(parking_lot.park_vehicle(motorcycle))

# print(parking_lot.get_available_spots())

# # Check if a specific spot is available
# print(parking_lot.is_spot_available(level_id=0, row_id=0, spot_id=0))

# print(parking_lot.remove_vehicle(car))
# print(parking_lot.is_spot_available(level_id=0, row_id=0, spot_id=0))
