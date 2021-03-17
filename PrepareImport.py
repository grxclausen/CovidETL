import pyodbc

def GetMaxCovidDate():
    cnxn = None

    cnxn_str = ("Driver={SQL Server Native Client 11.0};"
        "Server=localhost;"
        "Database=Covid;"
        "Trusted_Connection=yes;")

    cnxn = pyodbc.connect(cnxn_str)
    cursor = cnxn.cursor()

    cursor.execute("SELECT dbo.Get_Max_Collected_On();")

    max_date = cursor.fetchone()
    print(max_date)
    cursor.close()

    return max_date[0]

if __name__ == '__main__':
    maxDate = GetMaxCovidDate()