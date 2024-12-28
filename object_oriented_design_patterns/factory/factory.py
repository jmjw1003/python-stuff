from enum import Enum
from abc import ABC, abstractmethod


class Vehicles(Enum):
    CAR = "Car"
    VAN = "Van"
    MOTORBIKE = "Motorbike"


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Van(Vehicle):
    def drive(self):
        return "Driving a van"
    

class Motorbike(Vehicle):
    def drive(self):
        return "Driving a motorbike"



class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, vehicle_type: Vehicles):
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type: Vehicles):
        if vehicle_type == Vehicles.CAR:
            return Car()
        else:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}")
        

class VanFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type: Vehicles):
        if vehicle_type == Vehicles.VAN:
            return Van()
        else:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}")


class MotorbikeFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type: Vehicles):
        if vehicle_type == Vehicles.MOTORBIKE:
            return Motorbike()
        else:
            raise ValueError(f"Invalid vehicle type: {vehicle_type}")
        

