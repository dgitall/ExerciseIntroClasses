
class Animal:
    """Animal Class"""
    def __init__(self, name):
        self.__CommonName = name
        
    @property
    def CommonName(self):
        return self.__CommonName
    
    @CommonName.setter
    def CommonName(self, name):
        self.__CommonName = name
        
    @property
    def Genus(self):
        return self.__Genus
    
    @Genus.setter
    def Genus(self, genus):
        self.__Genus = genus
          
    @property
    def Species(self):
        return self.__Species
    
    @Species.setter
    def Species(self, species):
        self.__Species = species
         
    @property
    def Subspecies(self):
        return self.__Subspecies
    
    @Subspecies.setter
    def Subspecies(self, Subspecies):
        self.__Subspecies = Subspecies
        
    @property
    def Weight(self):
        return self.__Weight
    
    @Weight.setter
    def Weight(self, Weight):
        self.__Weight = Weight
          
    @property
    def Height(self):
        return self.__Height
    
    @Height.setter
    def Height(self, Height):
        self.__Height = Height
          
    @property
    def Width(self):
        return self.__Width
    
    @Width.setter
    def Width(self, Width):
        self.__Width = Width

    def move(self, direction):
        print(f"Moving toward {direction}")
        distance = 0
        return distance
        
    def eat(self):
        print("eat")
        
    def sleep(self):
        print("sleep")
        duration = 0
        return duration
    

class Book:
    """Book Class"""

    def __init__(self, title):
        self.__Title = title

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, title):
        self.__Title = title

    @property
    def Format(self):
        return self.__Format

    @Format.setter
    def Format(self, Format):
        self.__Format = Format

    @property
    def AuthorName(self):
        return self.__AuthorName

    @AuthorName.setter
    def AuthorName(self, AuthorName):
        self.__AuthorName = AuthorName

    @property
    def Publisher(self):
        return self.__Publisher

    @Publisher.setter
    def Publisher(self, Publisher):
        self.__Publisher = Publisher

    @property
    def PublishedDate(self):
        return self.__PublishedDate

    @PublishedDate.setter
    def PublishedDate(self, PublishedDate):
        self.__PublishedDate = PublishedDate

    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self.__ISBN = ISBN

    @property
    def ISBN13(self):
        return self.__ISBN13

    @ISBN13.setter
    def ISBN13(self, ISBN13):
        self.__ISBN13 = ISBN13

    def read(self, start_loc):
        print(f"Moving toward {start_loc}")
        end_loc = start_loc
        return end_loc


class Vehicle:
    """Vehicle Class"""

    def __init__(self, Make, Model, Year):
        self.__Make = Make
        self.__Model = Model
        self.__Year = Year

    @property
    def Make(self):
        return self.__Make

    @Make.setter
    def Make(self, Make):
        self.__Make = Make

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, Model):
        self.__Model = Model

    @property
    def Year(self):
        return self.__Year

    @Year.setter
    def AuthorYearName(self, Year):
        self.__Year = Year

    @property
    def VIN(self):
        return self.__VIN

    @VIN.setter
    def VIN(self, VIN):
        self.__VIN = VIN

    @property
    def Mileage(self):
        return self.__Mileage

    @Mileage.setter
    def Mileage(self, Mileage):
        self.__Mileage = Mileage

    @property
    def ExteriorColor(self):
        return self.__ExteriorColor

    @ExteriorColor.setter
    def ExteriorColor(self, ExteriorColor):
        self.__ExteriorColor  = ExteriorColor

    @property
    def InteriorColor(self):
        return self.__InteriorColor

    @InteriorColor.setter
    def InteriorColor(self, InteriorColor):
        self.__InteriorColor = InteriorColor

    @property
    def Engine(self):
        return self.__Engine

    @Engine.setter
    def Engine(self, Engine):
        self.__Engine = Engine

    @property
    def FuelType(self):
        return self.__FuelType

    @FuelType.setter
    def FuelType(self, FuelType):
        self.__FuelType = FuelType

    @property
    def Transmission(self):
        return self.__Transmission

    @Transmission.setter
    def Transmission(self, Transmission):
        self.__Transmission = Transmission

    @property
    def DriveTrain(self):
        return self.__DriveTrain

    @DriveTrain.setter
    def DriveTrain(self, DriveTrain):
        self.__DriveTrain = DriveTrain
        
        
    def drive(self, driverinput, wheelangle):
        print(f"drive {driverinput} {wheelangle}")
        speed = 0
        acceleration = 0
        return speed, acceleration
