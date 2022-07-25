from Cars import car



class AvtoParking:
    def __init__(self,line,spot):
        self.line=line
        self.spot=spot
        self.available=set(line*spot)


    def entrance(self,car):
        if self.available==0:
            print("there are not  {self.model} color is{self.color},number is{self.number}")
            