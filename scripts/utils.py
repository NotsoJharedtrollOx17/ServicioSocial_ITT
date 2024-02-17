import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

ATTENDANCE_DATA_CSV_FILENAME = "../csv/attendance_data.csv"

def getDatasetDataframe():
    return pd.read_csv(ATTENDANCE_DATA_CSV_FILENAME)

def getResultsFilePath():
    return "../results/"

def getPlotSize():
    return (10, 6)

def getDpiScale():
    return 600

def setTransparentPlots(istransparent=True):
    if istransparent:
        # * permite hacer las graficas con fondo transparente
        plt.rcParams.update({"figure.facecolor": (1, 1, 1, 0)})

        print(f"Succesfully setted plots to have transparent backgrounds!!!")

def setNumericDatesForDataframe(df_csv):
    def convert_to_numeric_date(date_str):
        # Split the date string by comma and space to get the month onwards
        month_onwards = date_str.split(", ", 1)[1]
        # Parse the remaining part into a datetime object
        date_obj = datetime.strptime(month_onwards, "%B %d, %Y")
        # Format the datetime object as a numeric date string
        formatted_date = date_obj.strftime("%m/%d/%Y")

        return formatted_date
    
    df_csv['fecha_mmddyyyy'] = df_csv['fecha_mmddyyyy'].apply(convert_to_numeric_date)

    df_csv.to_csv(ATTENDANCE_DATA_CSV_FILENAME, index=False)

    print(f"Succesfully formatted dates to numeric counterparts for {ATTENDANCE_DATA_CSV_FILENAME}")