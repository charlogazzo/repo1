import math

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
        self.status = "Empty"
        self.number_of_cases = 0
        
    def getLocationName(self):
        return self.name
    
    def getHeight(self):
        return self.max_height
    
    def getLoads(self):
        return self.loads
    
    def getLocationCRC(self):
        return self.location_crc
    
    def setLocationCRC(self, crc):
        self.location_crc = crc
    
    def getStaus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
        
    def getNumberOfCases(self):
        return self.number_of_cases
    
class Load:
    def __init__(self, product, amount):
        self.product = product
        self.no_of_cases = amount
        
    def getProduct(self):
        return self.product
    
    def getCaseCount(self):
        return self.no_of_cases
    
    def setCaseCount(self, count):
        self.no_of_cases = count
        
class Product:
    def __init__(self, name, crc, per_layer, height):
        self.name = name
        self.crc = crc
        self.cases_per_layer = per_layer
        self.case_height = height
        
    def getProductName(self):
        return self.name
    
    def getCRC(self):
        return self.crc
    
    def getCasesPerLayer(self):
        return self.cases_per_layer
    
    # The height of a case is also the height of a layer
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
        
        for location in warehouse.getLocations():
            if location.getstatus() == "Empty":
                return location
            
    #Returns: Eligible or Ineligible
    @staticmethod
    def evaluate_potential_status(location, pallet):
        case_height = pallet.getProduct().getCRC()
        cases_per_layer = pallet.getProduct().getCasesPerLayer()
        current_case_count = 0
        
        for load in location.getLoads():
            current_case_count += load.getCaseCount()
        
        total_cases = current_case_count + pallet.getCaseCount()
        no_of_layers =  math.ceil((total_cases / cases_per_layer))
        potential_height = no_of_layers * case_height
        
        if potential_height > location.getHeight():
            return "Ineligible"
        elif potential_height == location.getHeight():
            return "Eligible_Full"
        else:
            return "Eligible"
        
    # Also write code to tell JDA to set the status to "full"
    # If the maximum height has been reached exactly
    #Returns: success or failure
    @staticmethod
    def addLoad(location, pallet):
        if location.getStatus() == "Empty":
            location.getLoads().append(pallet)
            location.setLocationCRC(pallet.getProduct().getCRC())
            location.setStatus("Not Full")
        
        elif JDA().evaluate_potential_status(location, pallet) == "Eligible_Full":
            location.getLoads().append()
            location.setStatus("Full")
            
        else:
            location.getLoads().append(pallet)
    
    # This method must be run after any load is added to a location        
    @staticmethod
    def calculateNumberOfCases(location):
        case_count = 0
        
        for load in location.getLoads():
            case_count += load.getCaseCount()
        
        location.setCaseCount(case_count)
    
    # Prints all the locations in a warehouse, the products contained in them, their CRCs and number of cases
    # Returns a list of lists showing each location's Product name, CRC, Number of cases in the location and the location status
    @staticmethod
    def warehouseLocationSummary(warehouse):
        output_list = []
        
        for location in warehouse.getLocations():
            location_summary = []
            
            # Remember this is just one location. It could be empty and in such a case, write code to show that
            # it is empty. Remember: Reader friendly output
            if location.getStaus() == "Empty":
                location_summary = [location.getLocationName(), "No products", "", "0", location.getStaus()]
            else:
                location_summary.append(location.getLocationName())
                location_summary.append((location.getLoads()[0]).getProduct().getName())
                location_summary.append(location.getLocationCRC())
                location_summary.append(str(location.getCaseCount()))
                location_summary.append(location.getStaus())
            
            output_list.append(location_summary)
        
        return output_list
        