from Cars import Car
from Parking import Parking


class ParkingLot(object):
    instance=None

    class _singleton:
        def __init__(self,size):
            self.size=size
            self.slot=[]
            self.registered_cars={}
    
    def __init_(self,size):
        if(int(size)<0):
            print("To'xtassh joyingizni xato kiritdingiz!")
            return

        if not ParkingLot.inctance:
            ParkingLot.instance=ParkingLot._singleton(int(size))
        
        else:
            ParkingLot.instance.size=int(size)

        for a in range(int(size)):
            ParkingLot.instance.slot.append(Parking(a+1))

        print("Size slotli avtoguruh yaratildi")

def get_size(self):
    return self.size

def get_slot(self):
    return self.slot

def get_registratsion_cars(self):
    return self.registered_cars

def park(self, registration_number, color):
		empty_spot = 0
		for i in range(len(ParkingLot.instance.size)):
			if ParkingLot.instance.slot[i].is_occupied() == False:
				empty_spot = i+1
				break
		if(empty_spot == 0):
			print("kechirasiz,Avtoparking to'lgan")
		else:
			current_slot = ParkingLot.instance._slots[empty_spot]
			print("Allocated slot number: #{empty_spot}")

			if ParkingLot.instance.registered_cars.get(registration_number) is not None:
				current_slot.car = ParkingLot.instance.registered_cars.get(registration_number)
				ParkingLot.instance.registered_cars.get(registration_number).set_spot(current_slot)
			else:
				car = Car(registration_number, color)
				current_slot.set_car(car)
				car.set_spot(current_slot)
				ParkingLot.instance.registered_cars[registration_number] = car

