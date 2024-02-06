# * Import proper Data Analysis pipeline tools
import pandas as pd

def getAttendanceNumbersPerWeek(df_csv):
    
    # to datetime format...
    df_csv['fecha_mmddyyyy'] = pd.to_datetime(df_csv['fecha_mmddyyyy'], 
                                              format='%A, %B %d, %Y')
    
    # new column to display the day of the week
    # TODO review starting day and end day of each workweek
    df_csv['day_of_week'] = df_csv['fecha_mmddyyyy'].dt.day_name()
    df_csv['start_workweek'] = df_csv.groupby([
        df_csv['fecha_mmddyyyy'].dt.isocalendar().week])['fecha_mmddyyyy'].transform('min')
    df_csv['end_workweek'] = df_csv.groupby([
        df_csv['fecha_mmddyyyy'].dt.isocalendar().week])['fecha_mmddyyyy'].transform('max')

    # grouping by week, counting the attendance registers
    attendance_by_week = df_csv.groupby([df_csv['fecha_mmddyyyy'].
                                         dt.isocalendar().week, 
                                         'start_workweek', 'end_workweek']).size().reset_index(
                                             name='attendance_count')
    
    print("ATTENDANCE BY WEEK: ")
    print(attendance_by_week)

def main():
    ATTENDANCE_DATA_CSV_FILENAME = "../csv/attendance_data.csv"

    df_csv = pd.read_csv(ATTENDANCE_DATA_CSV_FILENAME)

    #print(df_csv)

    getAttendanceNumbersPerWeek(df_csv)

if __name__ == '__main__':
    main()