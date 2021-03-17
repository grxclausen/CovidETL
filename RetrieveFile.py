import requests
import csv
import pandas as pd

def DownloadFile(covidDownloadedFile):
    try:
        # OurWorldInData.com switched to Johns Hopkins data on 11/30/2020
        # The schema and data in the file are the same.
        url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

        covid = requests.get(url, allow_redirects=True)
        open(covidDownloadedFile, 'wb').write(covid.content)
        print("*** Download Successful ***")
    except:
        print("*** Download Failed ***")
# End of DownloadFile

def PrintHeader(covidDownloadedFile):
    with open(covidDownloadedFile, "r") as csvFile:
        covidCsv = csv.reader(csvFile, delimiter=',')
        header = next(covidCsv)

        # Iterate through columns
        print("------------ Columns in original file ------------")
        for row in header:
            print(row)
        print("--------------------------------------------------")
# End of PrintHeader

def CleanFile(covid_downloaded_file, covid_transformed_file):
    # Create the initial dataframe
    df = pd.read_csv(covid_downloaded_file)

    exception_list = open('exceptions.txt', 'r')
    Lines = exception_list.readlines()

    colListToKeep = []
    # Strips the newline character
    for line in Lines:
        no_nl = line.strip()
        colListToKeep.append(no_nl)

    # Define a set of columns to keep
    '''colListToKeep = set(['iso_code'
                         ,'continent'
                         ,'location'
                         ,'date'
                         ,'total_cases'
                         ,'new_cases'
                         ,'new_cases_smoothed'
                         ,'new_deaths_smoothed'
                         ,'total_deaths'
                         ,'new_deaths'
                         ,'total_cases_per_million'
                         ,'new_cases_per_million'
                         ,'new_cases_smoothed_per_million'
                         ,'total_deaths_per_million'
                         ,'new_deaths_per_million'
                         ,'new_deaths_smoothed_per_million'
                         ,'total_tests'
                         ,'new_tests'
                         ,'population'
                         ,'total_vaccinations'
                         ,'people_vaccinated'
                         ,'new_vaccinations'])
    '''

    # Initialize a list of columns to be removed
    colListToRemove = []

    # Get the list of columns (header)
    colList = list(df)
    print("-------------------- Columns Removed -------------------------------------")
    for row in colList:
        if row not in colListToKeep:
            colListToRemove.append(row)
            print(row)
    print("--------------------------------------------------------------------------")

    # Drop the unwanted columns
    df_trans = df.drop(columns=colListToRemove)
    print(list(df_trans))

    # Export the dataframe to a CSV.
    df_trans.to_csv(covid_transformed_file, index=False)
# End of CleanFile

if __name__ == "__main__":

    # The original file downloaded
    covidDownloadedFile = "C:/DataFiles/Covid/CovidDownloaded.csv"

    # Unwanted columns removed
    covidTransformedFile = "C:/DataFiles/Covid/CovidTransformed.csv"

    DownloadFile(covidDownloadedFile)
    PrintHeader(covidDownloadedFile)
    CleanFile(covidDownloadedFile, covidTransformedFile)