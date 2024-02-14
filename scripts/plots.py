import utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

# TODO WRITE HISTOGRAM PLOT CODE; Time series is done
def getTimeSeriesAttendanceNumbers(df_csv):
    FILE_NAME = "00_timeseries_asistencia_por_dia"
    file_path = f"{utils.getResultsFilePath()}" + FILE_NAME

    # Convert the 'fecha_mmddyyyy' column to datetime format
    df_csv['fecha_mmddyyyy'] = pd.to_datetime(df_csv['fecha_mmddyyyy'], format='%A, %B %d, %Y')

    # ? weird bug related to date display within the plot
    print(df_csv['fecha_mmddyyyy'])

    # Group the data by date and count attendance for each date
    attendance_over_time = df_csv.groupby('fecha_mmddyyyy').size().rename('attendance_count')

    print(attendance_over_time)

    fig, axes = plt.subplots(figsize=utils.getPlotSize(), 
                             dpi=utils.getDpiScale())

    # Add vertical dotted lines for each dot
    for date, count in zip(attendance_over_time.index, attendance_over_time.values):
        axes.vlines(x=date, ymin=0, ymax=count, color='seagreen', linestyle='--', alpha=0.5)
    
    axes.scatter(attendance_over_time.index, attendance_over_time.values, 
              color='forestgreen')

    # Set labels and title
    axes.yaxis.set_major_locator(ticker.MaxNLocator(integer=True)) # * Forzar la escala vertical a números enteros
    axes.xaxis.set_tick_params(labelsize=8)
    axes.yaxis.set_tick_params(labelsize=8)
    axes.set_ylim(0, 20) # * Limite de escala
    axes.set_xlabel('Date', fontsize=11)
    axes.set_ylabel('Attendance Count', fontsize=11)
    axes.set_title('Attendance Over Time', fontsize=12)

    # Optionally, set additional properties such as grid lines
    axes.grid(True)

    # Show the plot
    #plt.savefig(file_path)
    #plt.close()
    
    print(f"GRAFICA {file_path} realizada con éxito!")

def main():
    
    # carga del CSV como dataframe
    df_csv = utils.getDatasetDataframe()

    # agregar fondo transparente a las gráficas
    utils.setTransparentPlots(True)

    getTimeSeriesAttendanceNumbers(df_csv)

if __name__ == '__main__':
    main()