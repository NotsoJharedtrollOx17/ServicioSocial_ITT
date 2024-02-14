import pandas as pd
import matplotlib.pyplot as plt

def getDatasetDataframe():
    ATTENDANCE_DATA_CSV_FILENAME = "../csv/attendance_data.csv"

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
