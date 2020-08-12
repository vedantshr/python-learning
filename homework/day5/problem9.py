class ParkedVehicle:
    def __init__(self, vehicleSeq, fourWheeler, parkedFor, valetParking):
        self.vehicleSeq = vehicleSeq
        self.fourWheeler = fourWheeler
        self.parkedFor = parkedFor
        self.valetParking = valetParking
        self.parkedStatus = "Parked"

class ParkingLot:
    def __init__(self, parkd_vehicle):
        self.parkd_vehicle = parkd_vehicle

    def updateParkedStatus(self, lot_number):
        for key in self.parkd_vehicle:
            if lot_number == key:
                self.parkd_vehicle[key].parkedStatus = "Cleared"
                return (lot_number, self.parkd_vehicle[key].parkedStatus)

    def getParkingCharges(self, lot_number):
        for key in self.parkd_vehicle:
            if lot_number == key:
                if self.parkd_vehicle[key].fourWheeler == "fourwheeler":
                    if self.parkd_vehicle[key].valetParking == "yes":
                        return (50*self.parkd_vehicle[key].parkedFor + 10)
                    elif self.parkd_vehicle[key].valetParking == "no":
                        return (50*self.parkd_vehicle[key].parkedFor)
                else:
                    return (30*self.parkd_vehicle[key].parkedFor)
                
if __name__ == "__main__":
    n = int(input())
    parkd_vehicle = {}
    for i in range(n):
        vehicleSeq = int(input())
        fourWheeler = input()
        parkedFor = float(input())
        valetParking = input()
        parkingLot_number = int(input())
        obj = ParkedVehicle(vehicleSeq, fourWheeler, parkedFor, valetParking)
        parkd_vehicle[parkingLot_number] = obj

    lot_number = int(input())
    obj2 = ParkingLot(parkd_vehicle)
    status = obj2.updateParkedStatus(lot_number)
    parkingCharge = obj2.getParkingCharges(lot_number)
    print(status)
    print(parkingCharge)
        
        

