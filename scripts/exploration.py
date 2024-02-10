# * Import proper Data Analysis pipeline tools
import pandas as pd

def getAttendanceNumbersPerDayOfTheWeek(df_csv):

    # to datetime format...
    df_csv['fecha_mmddyyyy'] = pd.to_datetime(df_csv['fecha_mmddyyyy'], 
                                              format='%A, %B %d, %Y')
    
    # Define the desired order of days of the week
    desired_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Create a mapping of the day names to their corresponding position in the desired order
    order_mapping = {day: idx for idx, day in enumerate(desired_order)}

    # Group by day of the week
    attendance_by_day = df_csv.groupby(df_csv['fecha_mmddyyyy'].dt.day_name()).size().reset_index(name='attendance_count')

    # Apply the custom sorting key based on the desired order
    attendance_by_day_sorted = df_csv.sort_values(by='fecha_mmddyyyy', key=lambda x: x.map(order_mapping))

    # Display the result
    print("ATTENDANCE BY DAY:")
    print(attendance_by_day_sorted)

def getAttendanceNumbersPerMatricula(df_csv):
    # Group the DataFrame by the "matricula" column and calculate the sum of attendance counts for each group
    attendance_by_matricula = df_csv.groupby('matricula').size().reset_index(name="attendance_count")

    # Display the result
    print("ATTENDANCE BY MATRICULA:")
    print(attendance_by_matricula)

    # Sort the DataFrame based on the "attendance_count" column in descending order
    top_ten_attendance_records = attendance_by_matricula.sort_values(by='attendance_count', ascending=False).head(10)
    
    # Display the result
    print("TOP 10 ATTENDANCE BY MATRICULA:")
    print(top_ten_attendance_records)


def main():
    ATTENDANCE_DATA_CSV_FILENAME = "../csv/attendance_data.csv"

    df_csv = pd.read_csv(ATTENDANCE_DATA_CSV_FILENAME)

    #print(df_csv)

    getAttendanceNumbersPerDayOfTheWeek(df_csv)
    getAttendanceNumbersPerMatricula(df_csv)

if __name__ == '__main__':
    main()