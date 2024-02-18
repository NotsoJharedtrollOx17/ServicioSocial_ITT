import utils
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

def getTimeSeriesAttendanceNumbers(df_csv):
    FILE_NAME = "00_timeseries_asistencia_por_dia"
    file_path = f"{utils.getResultsFilePath()}{FILE_NAME}"
    summer_break_date = pd.to_datetime("2023-07-14")  # Example date for the start of summer break
    summer_break_start = pd.to_datetime("2023-06-05")  
    summer_break_end = pd.to_datetime("2023-08-21")

    # Convert 'fecha_mmddyyyy' column to datetime format
    df_csv['fecha_mmddyyyy'] = pd.to_datetime(df_csv['fecha_mmddyyyy'], format='%m/%d/%Y')

    # Group the data by date and count attendance for each date
    attendance_over_time = df_csv.groupby('fecha_mmddyyyy').size().rename('attendance_count')
    
    fig, axes = plt.subplots(figsize=utils.getPlotSize(), dpi=utils.getDpiScale())

    # Optionally, set additional properties such as grid lines
    axes.grid(True, linestyle='--', zorder=1)
    
    # Create a bar graph
    axes.bar(attendance_over_time.index, attendance_over_time.values, color="#029A09", zorder=2)
    
    # Set custom messages for indicating summer break
    #axes.text(summer_break_date, 16, "SUMMER BREAK", color='darkorange', rotation=45, style='italic', va='center', ha='center', fontsize=24)
    axes.text(summer_break_date, 12, "SUMMER BREAK", color="#FF5100", 
              rotation=45, style='italic', va='center', ha='center', fontsize=24, zorder=2)
    axes.text(summer_break_date, 8, "SUMMER BREAK", color="#FF5100", 
              rotation=45, style='italic', va='center', ha='center', fontsize=24, zorder=2)
    axes.text(summer_break_date, 4, "SUMMER BREAK", color="#FF5100", 
              rotation=45, style='italic', va='center', ha='center', fontsize=24, zorder=2)
    #axes.text(summer_break_date, 0, "SUMMER BREAK", color='darkorange', rotation=45, style='italic', va='center', ha='center', fontsize=24)
    
    # Set labels and title
    axes.yaxis.set_major_locator(ticker.MaxNLocator(integer=True)) # * Forzar la escala vertical a números enteros
    axes.xaxis.set_tick_params(labelsize=8)
    axes.yaxis.set_tick_params(labelsize=8)
    axes.set_ylim(0, 16) # * Limite de escala
    axes.set_xlabel('Date', fontsize=11)
    axes.set_ylabel('Attendance Count', fontsize=11)
    axes.set_title('Attendance Over Time (03/02/2023 - 10/20/2023)', fontsize=12)

    # Add vertical lines for the duration of summer vacations
    axes.axvline(x=summer_break_start, color="#FF5100", linestyle='--', label='Summer Break Start', zorder=2)
    axes.axvline(x=summer_break_end, color="#FF5100", linestyle='--', label='Summer Break End',zorder=2)

    # Show the plot
    plt.savefig(file_path)
    plt.close()
    
    print(f"GRAFICA {file_path} realizada con éxito!")

def getHorizontalBarGraphAttendancePerDayOfWeek(df_csv):
    colors = ["#0AFF0A",
              "#04CB0A",
              "#029A09",
              "#026B06",
              "#024002",
              ] # * greenish color gradient

    FILE_NAME = "01_horizontalbar_asistencia_por_dia_semana"
    file_path = f"{utils.getResultsFilePath()}{FILE_NAME}"

        # to datetime format...
    df_csv['fecha_mmddyyyy'] = pd.to_datetime(df_csv['fecha_mmddyyyy'], format='%m/%d/%Y')
    
    # Define the desired order of days of the week
    day_to_numeric = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4
    }

    # Group by day of the week
    attendance_by_day = df_csv.groupby(df_csv['fecha_mmddyyyy'].dt.day_name()).size().reset_index(name='attendance_count')
    
    # Add an extra column assigning numeric values based on the day of the week
    attendance_by_day['day_numeric'] = attendance_by_day['fecha_mmddyyyy'].map(day_to_numeric)

    # Assigning the colors to the values of the dataframe
    attendance_by_day_sorted = attendance_by_day.sort_values(by='attendance_count')
    attendance_by_day_sorted['color'] = [colors[i] for i in range(len(colors))]

    # Sort the DataFrame based on the 'day_numeric' column in ascending order
    attendance_by_day_sorted = attendance_by_day_sorted.sort_values(by='day_numeric', ascending=False)

    fig, axes = plt.subplots(figsize=utils.getPlotSize(), dpi=utils.getDpiScale())
    
    # Optionally, set additional properties such as grid lines
    axes.grid(True, linestyle='--', zorder=1)
    
    # Create horizontal bar graph
    axes.barh(attendance_by_day_sorted['fecha_mmddyyyy'], attendance_by_day_sorted['attendance_count'], 
              color=attendance_by_day_sorted['color'], height=0.5, zorder=2)

    # Set labels and title
    axes.xaxis.set_major_locator(ticker.MaxNLocator(integer=True)) # * Forzar la escala vertical a números enteros
    axes.xaxis.set_tick_params(labelsize=8)
    axes.yaxis.set_tick_params(labelsize=8)
    axes.set_xlabel('Attendance Count', fontsize=11)
    axes.set_ylabel('Day of the Week', fontsize=11)
    axes.set_title('Attendance by Day of the Week', fontsize=12)

        # Show the plot
    plt.savefig(file_path)
    plt.close()

    print(f"GRAFICA {file_path} realizada con éxito!")

def getHorizontalBarGraphAttendancePerTopHourSpans(df_csv):
    colors = ["#0AFF0A",
              "#04d50b",
              "#029A09",
              "#028707",
              "#026205",
              "#024002",
              ] # * greenish color gradient

    FILE_NAME = "02_horizontalbar_asistencia_top6_horarios"
    file_path = f"{utils.getResultsFilePath()}{FILE_NAME}"

    # Concatenate 'hora_inicio' and 'hora_fin' columns
    df_csv['combined_time'] = df_csv['hora_inicio'] + ' - ' + df_csv['hora_fin']
    
    # Grouping the dataframe by "combined_time"
    attendance_by_time = df_csv.groupby('combined_time').size().reset_index(name='attendance_count')
    
    # Assigning the colors to the values of the dataframe
    attendance_by_hour_sorted = attendance_by_time.sort_values(by='attendance_count')
    
    # Filter for attendance values greater than 2
    attendance_by_hour_filtered = attendance_by_hour_sorted[attendance_by_hour_sorted['attendance_count'] > 2]
    
    attendance_by_hour_filtered['color'] = [colors[i] for i in range(len(colors))]
    
    # Sorting the dataframe in ascending order of 'combined_time'
    attendance_by_hour_filtered.sort_values(by='combined_time', ascending=False, inplace=True)

    fig, axes = plt.subplots(figsize=utils.getPlotSize(), dpi=utils.getDpiScale())
    
    # Optionally, set additional properties such as grid lines
    axes.grid(True, linestyle='--', zorder=1)

    # Create horizontal bar graph
    axes.barh(attendance_by_hour_filtered['combined_time'], attendance_by_hour_filtered['attendance_count'], 
              color=attendance_by_hour_filtered['color'], height=0.5, zorder=2)

    # Set labels and title
    axes.xaxis.set_major_locator(ticker.MaxNLocator(integer=True)) # * Forzar la escala vertical a números enteros
    axes.xaxis.set_tick_params(labelsize=8)
    axes.yaxis.set_tick_params(labelsize=8)
    axes.set_xlabel('Attendance Count', fontsize=11)
    axes.set_ylabel('Hour Spans', fontsize=11)
    axes.set_title('Top 6 Attendance Hour Spans', fontsize=12)

    # Show the plot
    plt.savefig(file_path)
    plt.close()

    print(f"GRAFICA {file_path} realizada con éxito!")

def getHorizontalBarGraphAttendancePerTopUniqueStudents(df_csv):
    colors = ["#0AFF0A",
              "#03bb0a",
              "#03bb0a",
              "#03bb0a",
              "#027a07",
              "#024002",
              ] # * greenish color gradient

    FILE_NAME = "03_horizontalbar_asistencia_top6_estudiantes"
    file_path = f"{utils.getResultsFilePath()}{FILE_NAME}"

    # Group the DataFrame by the "matricula" column and calculate the sum of attendance counts for each group
    attendance_by_matricula = df_csv.groupby('matricula').size().reset_index(name="attendance_count")

    # Sort the DataFrame based on the "attendance_count" column in descending order
    top_attendance_records = attendance_by_matricula.sort_values(by='attendance_count', ascending=False).head(6)
    top_attendance_records = top_attendance_records.sort_values(by='attendance_count', ascending=True)

    # setting color
    top_attendance_records['color'] = [colors[i] for i in range(len(colors))]
    
    # masking the 'matricula' values
    top_attendance_records['matricula'] = [f"000{i}" for i in range(len(colors))]

    # reordering for better formatting of the graph
    top_attendance_records = top_attendance_records.sort_values(by='attendance_count', ascending=False)

    fig, axes = plt.subplots(figsize=utils.getPlotSize(), dpi=utils.getDpiScale())
    
    # Optionally, set additional properties such as grid lines
    axes.grid(True, linestyle='--', zorder=1)

    # Create horizontal bar graph
    axes.barh(top_attendance_records['matricula'], top_attendance_records['attendance_count'], 
              color=top_attendance_records['color'], height=0.5, zorder=2)

    # Set labels and title
    axes.xaxis.set_major_locator(ticker.MaxNLocator(integer=True)) # * Forzar la escala vertical a números enteros
    axes.xaxis.set_tick_params(labelsize=8)
    axes.yaxis.set_tick_params(labelsize=8)
    axes.set_xlabel('Attendance Count', fontsize=11)
    axes.set_ylabel('Student ID (masked)', fontsize=11)
    axes.set_title('Top 6 Unique Students\' Attendance', fontsize=12)

    # Show the plot
    plt.savefig(file_path)
    plt.close()

    print(f"GRAFICA {file_path} realizada con éxito!")

def main():
    
    # carga del CSV como dataframe
    df_csv = utils.getDatasetDataframe()

    # agregar fondo transparente a las gráficas
    utils.setTransparentPlots(True)

    getTimeSeriesAttendanceNumbers(df_csv)
    getHorizontalBarGraphAttendancePerDayOfWeek(df_csv)
    getHorizontalBarGraphAttendancePerTopHourSpans(df_csv)
    getHorizontalBarGraphAttendancePerTopUniqueStudents(df_csv)

if __name__ == '__main__':
    main()