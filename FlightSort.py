#In order to properly use the database and sort it, we need to import pandas
import pandas as pd

#Since the webscraper is currently not working, this part of the project is using a database from Kaggle, which contains the data of multiple flights https://www.kaggle.com/datasets/dilwong/flightprices

#Read the data into the file and clean the data
#While there are 11 different columns in the dataset, we will only focus on 4 of them

class Flight():
    def __init__(self, filename):
        """Initializes the Flight class and creates table of 4 main factors
    
        Args:
            filename: the name of the csv file that will be read into the code"""
        data = pd.read_csv(filename)
        self.result = data[["Source", "Destination", "Price", "Date_of_Journey"]]
        
    def __str__(self):
        return "Here is your destination information:"
    
    def flight_info(self, destination):
        """Takes the flight info based on the destination
        
        Args: 
            destination(str): the user input of flight destination
        
        Returns:
            flight_results: the flight data for only the inputted destination"""
        flight_results = self.result[self.result["Destination"] == destination]
        return flight_results
    
    def cheapest(self, data):
        """Gives the 5 cheapest flights
        
        Args: 
            data(table): table containing flight data
        
        Returns: 
            table containing the 5 cheapest flights"""
        data.sort_values("Price", ascending = True)
        return data.head(5)

def main():
    """Asks for user input for the destination of flight and creates flight data
    
    Args:
        none
        
    Returns:
        the 5 cheapest flights from the database based on user input"""
    destination = input("What is the destination of your flight\n")
    flight = Flight("Data_Train.csv")
    get_info = flight.flight_info(destination)
    get_cheapest = flight.cheapest(get_info)
    print(flight.__str__())
    print(get_cheapest)

main()
        
        
        
    
        
       
        
        