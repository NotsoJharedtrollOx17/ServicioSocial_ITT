import pandas as pd
from utils import getDatasetDataframe

def getAttendanceNumbersPerStartAndFinishTime(df_csv):
    # Concatenate 'hora_inicio' and 'hora_fin' columns
    df_csv['combined_time'] = df_csv['hora_inicio'] + ' - ' + df_csv['hora_fin']
    
    # Grouping the dataframe by "combined_time"
    attendance_by_time = df_csv.groupby('combined_time').size().reset_index(name='attendance_count')
    
    # Sorting the dataframe in ascending order of 'combined_time'
    attendance_by_time.sort_values(by='combined_time', ascending=True, inplace=True)

    # Filter for attendance values greater than 2
    attendance_by_time_filtered = attendance_by_time[attendance_by_time['attendance_count'] > 2]

    # Display the result
    print("\nATTENDANCE BY Start and Finish Time (TOP 6 MOST FREQUENT TIMESPANS):")
    print(attendance_by_time_filtered)

def getAttendanceNumbersPerStartTime(df_csv):
    # Grouping the dataframe by "hora_inicio"
    attendance_by_start_time = df_csv.groupby('hora_inicio'
                                              ).size().reset_index(name='attendance_count')
    
    # Sorting the dataframe in descending order
    attendance_by_start_time.sort_values(by='hora_inicio', ascending=False, inplace=True)

    # Display the result
    print("\nATTENDANCE BY StartTime:")
    print(attendance_by_start_time)

def getAttendanceNumbersPerFinishTime(df_csv):
    # Grouping the dataframe by "hora_inicio"
    attendance_by_start_time = df_csv.groupby('hora_fin'
                                              ).size().reset_index(name='attendance_count')
    
    # Sorting the dataframe in descending order
    attendance_by_start_time.sort_values(by='hora_fin', ascending=False, inplace=True)

    # Display the result
    print("\nATTENDANCE BY FinishTime:")
    print(attendance_by_start_time)

def getAttendanceNumbersPerDayOfTheWeek(df_csv):

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

    # Sort the DataFrame based on the 'day_numeric' column in ascending order
    attendance_by_day_sorted = attendance_by_day.sort_values(by='day_numeric')

    # Display the result
    print("\nATTENDANCE BY DAY:")
    print(attendance_by_day_sorted)

def getAttendanceNumbersPerMatricula(df_csv):
    # Group the DataFrame by the "matricula" column and calculate the sum of attendance counts for each group
    attendance_by_matricula = df_csv.groupby('matricula').size().reset_index(name="attendance_count")

    # Display the result
    print("\nATTENDANCE BY MATRICULA:")
    print(attendance_by_matricula)

    # Sort the DataFrame based on the "attendance_count" column in descending order
    top_ten_attendance_records = attendance_by_matricula.sort_values(by='attendance_count', ascending=False).head(10)
    
    # Display the result
    print("\nTOP 10 ATTENDANCE BY MATRICULA:")
    print(top_ten_attendance_records)

def getAttendanceRateByWeekRecurrentStudents(df_csv):
    # Convert the 'fecha_mmddyyyy' column to datetime format
    df_csv['fecha_mmddyyyy'] = pd.to_datetime(df_csv['fecha_mmddyyyy'], format='%m/%d/%Y')

    # Group by student, week, and count the number of attendances per week
    student_week_attendance = df_csv.groupby(['matricula', df_csv['fecha_mmddyyyy'].dt.isocalendar().week]).size()

    # Filter students who attended at least twice in a week
    recurrent_students = student_week_attendance[student_week_attendance >= 2].reset_index(level=1)

    # Count the number of unique students that were recurrent
    unique_recurrent_students = recurrent_students.index.nunique()

    # Count the number of unique total students
    unique_total_students = df_csv['matricula'].nunique()

    # Calculate the recurrent student's weekly attendance rate
    recurrent_student_attendance_rate = (unique_recurrent_students / unique_total_students) * 100

    print(f"\nAchieved recurrent student's weekly attendance rate of: {round(recurrent_student_attendance_rate, 0)}%")

def getAttendanceRateByStartAndFinishTime(df_csv):
# Concatenate 'hora_inicio' and 'hora_fin' columns
    df_csv['combined_time'] = df_csv['hora_inicio'] + ' - ' + df_csv['hora_fin']
    
    # Grouping the dataframe by "combined_time"
    attendance_by_time = df_csv.groupby('combined_time').size().reset_index(name='attendance_count')
    
    # Sorting the dataframe in ascending order of 'combined_time'
    attendance_by_time.sort_values(by='combined_time', ascending=True, inplace=True)

    # Filter for attendance values greater than 2
    attendance_by_time_filtered = attendance_by_time[attendance_by_time['attendance_count'] > 2]

    # Aggregate all counts for the filtered attendendance time spans
    total_attendance_by_time_filtered = attendance_by_time_filtered['attendance_count'].sum()

    # Count the number of total students
    total_students = df_csv.shape[0]

    # Calculate the recurrent student's weekly attendance rate
    top_attendance_by_time_rate = (total_attendance_by_time_filtered / total_students) * 100

    print(f"\nAchieved TOP 6 Time Spans' attendance rate of: {round(top_attendance_by_time_rate, 0)}%")

def getTotalUniqueStudents(df_csv):
    # Count the number of unique total students
    total_unique_students = df_csv['matricula'].nunique()

    print(f"\nAchieved attendance total of: {total_unique_students} unique students!")

def main():

    # * Loads dataset
    df_csv = getDatasetDataframe()

    getTotalUniqueStudents(df_csv)
    getAttendanceRateByWeekRecurrentStudents(df_csv)
    getAttendanceRateByStartAndFinishTime(df_csv)
    getAttendanceNumbersPerDayOfTheWeek(df_csv)
    getAttendanceNumbersPerMatricula(df_csv)
    getAttendanceNumbersPerStartTime(df_csv)
    getAttendanceNumbersPerFinishTime(df_csv)
    getAttendanceNumbersPerStartAndFinishTime(df_csv)

if __name__ == '__main__':
    main()