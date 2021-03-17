import pandas as pd

csvPath = "C:/DataFiles/Covid/covidTransformed.csv"
csvPathOut = "C:/DataFiles/Covid/covidConverted.csv"


def ConvertDataTypes(csvPath):
    dfNonConv = pd.read_csv(csvPath)
    dfNonConv.info()

    dfNonConv = dfNonConv.fillna(0)

    convert_dict = {
        'iso_code': str,
        'continent': str,
        'location': str,
        'date': str,
        'total_cases': int,
        'new_cases': int,
        'new_cases_smoothed': float,
        'total_deaths': int,
        'new_deaths': int,
        'new_deaths_smoothed': float,
        'total_cases_per_million': float,
        'new_cases_per_million': float,
        'new_cases_smoothed_per_million': float,
        'total_deaths_per_million': float,
        'new_deaths_per_million': float,
        'new_deaths_smoothed_per_million': float,
        'total_vaccinations': int,
        'people_vaccinated': int,
        'people_fully_vaccinated': int,
        'new_vaccinations': int,
        'new_vaccinations_smoothed': float,
        'total_vaccinations_per_hundred': float,
        'people_vaccinated_per_hundred': float,
        'people_fully_vaccinated_per_hundred': float,
        'new_vaccinations_smoothed_per_million': float,
        'population': int,
        'population_density': float,
        'median_age': float,
        'aged_65_older': float,
        'aged_70_older': float
    }

    dfNonConv = dfNonConv.astype(convert_dict)

    dfNonConv.info()

    dfNonConv.to_csv(csvPathOut, index=False)


if __name__ == "__main__":
    ConvertDataTypes(csvPath)