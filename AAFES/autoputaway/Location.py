

class Warehouse:
    def __init__(self, name, *locations):
        self.name = name
        self.locations = []
        
        for location in locations:
            self.locations.append(location)
    
    def getLocations(self):
        return self.locations

class Location:
    def __init__(self, name, height):
        self.name = name
        self.max_height = height
        self.loads = []
        self.location_crc = None
        
    def getName(self):
        return self.name
    
    def getHeight(self):
        return self.max_height
    
    def getLoads(self):
        return self.loads
    
    def getLocationCRC(self):
        return self.location_crc
    
class Load:
    def __init__(self, product, amount):
        self.product = product
        self.no_of_cases = amount
        
    def getProduct(self):
        return self.product
    
    def getCases(self):
        return self.no_of_cases
        
class Product:
    def __init__(self, name, crc, per_layer, height):
        self.name = name
        self.crc = crc
        self.cases_per_layer = per_layer
        self.case_height = height
        
    def getName(self):
        return self.name
    
    def getCRC(self):
        return self.crc
    
    def getCasesPerLayer(self):
        return self.cases_per_layer
    
    def getCaseHeight(self):
        return self.case_height

class JDA:
    
    @staticmethod
    def prepareLoad(product, case_amount):
        pallet = Load(product, case_amount)
        return pallet
    
    #This method will only look for locations that are "Not full" or "Empty"
    #Returns: No location found or an appropriate location for the merch
    @staticmethod
    def find_eligible_location(warehouse, pallet):
        for location in warehouse.getLocations():
            if (location.status == "Not Full" and 
            pallet.getProduct().getCRC() == location.getLocationCRC()):
                return location
    
    #Returns: Eligible or Ineligible
    @staticmethod
    def evaluate_potential_status(location, pallet):
        pass
    
    #Returns: success of failure
    @staticmethod
    def addLoad(location, pallet):
        pass
    
    #Prints all the locations in a warehouse, the products contained in them, their CRCs and number of cases
    @staticmethod
    def warehouseLocationSummary():
        pass