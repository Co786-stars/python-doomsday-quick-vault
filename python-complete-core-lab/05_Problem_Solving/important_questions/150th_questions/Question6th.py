# WAPP to convert kilometer to miles, meter, centemeter ?
# 1km = 0.6214miles

# ___________________________________________________________________________________#

km = 1
cm = km*100000
miles = km*0.6214
meter = km*1000
print(f"{km}km = {cm}cm")
print(f"{km}km = {miles}miles")
print(f"{km}km = {meter}meter")

# ___________________________________________________________________________________#

class MeasurementUnit:
    """body try to display mesurement unit"""
    def __init__(self):
        """initilize the attribute"""
        self.km = float(input("Kilometer : "))

    def miles_unit(self):
        """function body display km in miles"""
        self.miles = self.km*0.6214
        print(f"{self.km} kilometers is equal to {self.miles} miles.")
    
    def meter_unit(self):
        """function body display km in kilometer"""
        self.meters = self.km*1000
        print(f"{self.km} kilometers is equal to {self.meters} meters.")

    def centemeter_unit(self):
        """function body display km in centimeter"""
        self.centimeters = self.km*100000
        print(f"{self.km} kilometers is equal to {self.centimeters} centimeters.")

unit = MeasurementUnit()
unit.miles_unit()
unit.meter_unit()
unit.centemeter_unit()

# __________________________________________________________________________________#

