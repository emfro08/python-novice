def print_hello():
    """This function provides me a hello""" #create documentation and when we use tab to know function, we can already know how that do
    print("hello")
    
def return_combined_date(year, month, day):
    """return ISO 8601 DATE FORMAT
    https://fr.wikipedia.org/wiki/ISO_8601
    Parameter
    -----
    year = int
        the year of interest
    month = int
        the  month of interest (! between 1 and 12)
    day = int
        the day of interest
    """
    assert month <= 12 #only 12 months in a year
    assert day <=31 #months have max 31 days
    return str (year) + '-' + str(month)+ '-' + str(day) 
    
    
    #Fill in the blanks to create a function that takes a single filename as an argument, 
#loads the data in the file named by the argument, and returns the minimum value of column gdpPercap_1972 in that data:
    
import pandas


def min_in_data(filename, column_name): #choose a file, read it, choose column, choose value of min column #give filename for reuse
    """provide country and value with minimal value
    Parameters
    -----
    document you code !
    """
    data= pandas.read_csv(filename, index_col = "country")
    min_date = data[column_name].min() #always for this column from 1972 of choose to column_name
    min_country = data[column_name].idxmin()
    return min_date, min_country
