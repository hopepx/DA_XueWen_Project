#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse SEA region over a span of 10 years from 2007 to 2017 Including User Inputs
#Name: <Tan Xue Wen>
#Group Name: <NS>
#Class: <PN2004Y>
#Date: <16/7/2020>
#Version: <3.8>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd 

#import matplotlib for graphical conversion 
import matplotlib.pyplot as pit
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #print total number of countries in dataframe by counting the number of columns 
  print("Total number of countries:", str(len(df.columns) - 2))

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  #initializing dataframe for SEA region
  sea_region = df.iloc[348:, 0:9]

  #display selected region
  print("\n\n" + "Southeast Asia region.")

  #displays number of countries in the region by counting the number of columns
  print("Total number of countries:", str(len(sea_region.columns) - 2))

  #displays countries and year range
  print("The countries in the region are shown below.")
  print("Year range: 2007 - 2017" + "\n")

  #displays dataframe of SEA region
  print(sea_region)

  #Removing Year and Month
  newsea = sea_region.drop(columns=['Year', 'Month'])

  #Convert dtypes from object to int
  newsea[newsea.columns] = newsea[newsea.columns].astype(int)

  #Total up the number of visitors in each countries
  TotalSEA = newsea.sum()

  #Sort the total number in descending order
  Sortednewsea = TotalSEA.sort_values(ascending=False)

  #Resetting the dtypes back to objects
  Sortednewsea = Sortednewsea.reset_index()

  #Adding in column labels
  Sortednewsea.columns = ['Country', 'Visitors']


  #displays top 3 countries of the region
  print("\n" + "The Top 3 S.E.A region countries total visitors to Singapore from 2007-2017:" + "\n")
  top3_country = (Sortednewsea.head(3))
  top3_country.index = ['Most Visted →', 'Second Most Visted → ', 'Third Most Visted →']
  print(top3_country)
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  activities = ['Indonesia', 'Malaysia', 'Philippines']
  slices = [27572424, 11337420, 6548622]
  #colours = ['r', 'g', 'm']

  pit.pie(slices,
        labels=activities,
        startangle=180,
        shadow=True,
        explode=(0, 0, 0),
        autopct='%1.2f%%')

  pit.legend()

  pit.show() 


  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':



  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################