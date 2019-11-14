'US bikeshare Project 02:'
'Prepared By : BENOTSMANE ASMA'
'Import all the necessary package and Function for the execution of this program'

import time
import pandas as pd
import numpy as np
from calendar import day_name,month_name
from datetime import datetime
from datetime import time as Time
import matplotlib.pyplot as plt
'%matplotlib is library which produces statistic figure in variety hardcopy formats and interactive envirments across platforms'



#define the function that return the city and corresponding csv filename related to the user input:

def get_city():
    '''Returns city and filename related to (Chicago, New York and Washington) according to user input,
        while loop for  managing incorrect input.
        Args:    none.
        Returns: city: (str) lowercase of input city.file: (str) corresponding csv filename.
    '''

    # Allows  user to introduce the city he/she want to work with using while loop for managing invalid input
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n''Would you like to see data for Chicago, New York, or Washington?\n').lower()
        #check  if input string is one of the listed cities if not ask user to re-enter again
        if city not in ('chicago', 'new york', 'washington'):
            print('\nYou didn\'t enter availabe city. Please enter valid city name provided in options.\n'
    'Return to the original input request:')
        else:
            break
    # Use the input to select a filename corresponding to city
    if city == 'chicago':
        file = 'chicago.csv'
    elif city == 'new york':
        file = 'new_york_city.csv'
    else:
        file = 'washington.csv'

    return city, file
#Ask user to select time period filter
def get_time_period():
    '''Asks the user for the time filter use the wile loop for handling invalid entries .
    Args:
        none.
    Returns:
        (str) inputted type of filter.
    '''
    # Choosing filters that fit the needs , while loop for managing incorrect input
    while True:
        time_period = input('\nWould you like to filter the data: by month, day, both or '
    'not at all? Type "none" for no time filter.(be patient ! it will take some time)\n').lower()
        # Confirm if input string is one of the listed options and ask to input again if not mentioned in the options
        if time_period not in ('month', 'day', 'both', 'none'):
            print('\nYou didn\'t enter available filter.Please enter month, day, both or none.'
                  '\nReturn to the original input request:')
        else:
            break
    # Return user input as (str) lower case
    return time_period

def get_month():
    '''Returns month between January and June, basing on user input, while managing
       incorrect input.
    Args:
        none.
    Returns:
        (int) month as its index of month_name ('January' = 1)
    '''
    # Ask user to input Month Filter while loop for managing incorrect input
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
        # Confirm if input string is one of the filtred months and ask again if not
        if month not in month_name[:7]:
            print('\nYou didn\'t enter available month. Please enter one of the months listed.\n'
                  'Return to the original input request:')
        else:
            break
    # Return user input as (str) title case
    return list(month_name).index(month)

def get_day():
    '''Asks the user for a day and returns the corresponding index, while managing for incorrect input.
    Args:
        none.
    Returns:
        (int) day of the week as its index of day_name ('Monday' = 0).
    '''
    # Ask user for day filter using while loop for managing incorrect input
    while True:
        day = input('\nWhich day? Please enter a day of the week Monday,Tuesday,wednesday,thursday,Friday,Saturday,Sunday.'
                    '\n').title()
        # Confirm if input string is one of the days of the week and ask again if not
        if day not in day_name:
            print('\nYou didn\'t enter  available day. Please enter one of the '
                  'days of the week.\n'
                  'Return to the original input request:')
        else:
            break
    # Return (int) of day's index in day_name
    return list(day_name).index(day)

#Print out header that indicates city name and filters type used.

def print_header(city, filter_type, month_filter=None, day_filter=None):
    '''Prints header that indicatses city name and any filters used.
    Args:
        city: (str) city name.
        filter_type: (str) 'none', 'month', 'day', or 'both'.
        month_filter: (int) optional, index of selected month in month_name ('January' = 1).
        day_filter: (int) optional, index of selected day in day_name ('Monday' = 0).
    Returns:
        optional.
    '''
    if filter_type == 'none':
        print('\n--- Printing US Bikeshare Statistics for', city.title(), '---'
              '\n    (No filters used)\n')
    if filter_type == 'month':
        print('\n--- Printing US Bikeshare Statistics for', city.title(), '---'
              '\n    (Filter: Month - {})\n'.format(month_name[month_filter]))
    if filter_type == 'day':
        print('\n--- Printing US Bikeshare Statistics for', city.title(), '---'
              '\n    (Filter: Day - {})\n'.format(day_name[day_filter]))
    if filter_type == 'both':
        print('\n--- Printing US Bikeshare Statistics for', city.title(), '---'
              '\n    (Filters: Month - {}, Day - {})\n'.format(
                  month_name[month_filter], day_name[day_filter]))

# we plot pie chart by plt.pie()method for statistics image representation
def pie_chart(var_count, var_name, total_count, title):
    '''Creates a pie chart from two values.
    Args:
        var_count: (int) count of variable.
        var_name: (str) variable name.
        total_count: (int) total category count from which variable was selected.
        title: (str) title for chart.
    '''
    values = [var_count, total_count - var_count]
    labels = [var_name]
    colors = ['r','b','g']
    plt.subplots(figsize=(5,5))
    plt.pie(x=values, labels=labels, colors= colors)
    plt.title(title)

#Statistic computed
#1- Time Informations
#1.1-Popular month

def popular_month(df, city, trip_count, run_time_list):
    '''Prints the most popular start month, and its count, from df.
       Appends 'run time info' to a list for future printing.
    Args:
        df: Pandas DataFrame.
        run_time_list: (list).
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''

    start_time = time.time()
    df_time = df.dt.month
    popular_month = df_time.mode().loc[0]
    popular_month_count = df_time.value_counts().loc[popular_month]
    run_time_list.append(
        "Calculating the most popular start month took %s seconds."
        % round((time.time() - start_time), 4)
    )
    print(
        "Most popular month to start a trip:         {}  (Trips: {:,})"
        .format(month_name[popular_month], popular_month_count)
        )

    return run_time_list

   #1.2-Popular day :
def popular_day(df, city, trip_count, run_time_list):
    '''Prints the most popular start day, and its count, from df.
       Appends 'run time info' to a list for future printing.
    Args:
        df: Pandas DataFrame.
        run_time_list: (list).
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    popular_day = df.mode().loc[0]
    popular_day_count = df.value_counts().loc[popular_day]
    run_time_list.append(
        "Calculating the most popular start day took %s seconds."
        % round((time.time() - start_time), 4)
    )
    print(
        "Most popular day to start a trip:           {}  (Trips: {:,})"
        .format(day_name[popular_day], popular_day_count)
        )

    return run_time_list

      #1.3- Popular Hour
def popular_hour(df, city, trip_count, run_time_list):
    '''Prints the most popular start hour, and its count, from df.
       Appends 'run time info' to a list for future printing.
    Args:
        df: Pandas DataFrame.
        run_time_list: (list).
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    df_time = df.dt.hour
    popular_hour = df_time.mode().loc[0]
    convert_hour = Time(hour=popular_hour)
    popular_hour_count = df_time.value_counts().loc[popular_hour]

    # Save run-time info and print stats
    run_time_list.append(
        "Calculating the most popular start hour took %s seconds."
        % round((time.time() - start_time), 4)
    )
    print(
        "Most popular hour to start a trip:          {}  (Trips: {:,})"
        .format(convert_hour, popular_hour_count)
        )

    return run_time_list

   #2-Station Informations
    #2.1-Popular Start Station:
def popular_start_station(df, city, trip_count, run_time_list):
    '''Prints the most popular start station, and its count, from df.
       Appends 'run time info' to a list for future printing.
    Args:
        df: Pandas DataFrame.
        run_time_list: (list).
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    popular_station = df.mode().loc[0]
    popular_start_count = df.value_counts().loc[popular_station]
    # Save run-time info and print stats
    run_time_list.append(
        "Calculating the most popular start station took %s seconds."
        % round((time.time() - start_time), 4)
    )
    print(
        "Most popular start station:            {}  (Trips: {:,})"
        .format(popular_station, popular_start_count)
        )

    return run_time_list

    #2.2-Popular End Station:
def popular_end_station(df, city, trip_count, run_time_list):
    '''Prints the most popular end station, and its count, from df.
       Appends 'run time info' to a list for future printing.
    Args:
        df: Pandas DataFrame.
        run_time_list: (list).
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    popular_station = df.mode().loc[0]
    popular_start_count = df.value_counts().loc[popular_station]
    # Save run-time info and print stats
    run_time_list.append(
        "Calculating the most popular end station took %s seconds."
        % round((time.time() - start_time), 4)
    )
    print(
        "Most popular end station:              {}  (Trips: {:,})"
        .format(popular_station, popular_start_count)
        )

    return run_time_list

     #2.3- Popular Trip :
def popular_trip(df, city, trip_count, run_time_list):
    '''Prints the most popular trip, and its count, from df.
       Appends 'run time info' to a list for future printing.

    Args:
        df: Pandas DataFrame.
        run_time_list: (list).
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    popular_station = df.mode().loc[0]
    popular_start_count = df.value_counts().loc[popular_station]
    run_time_list.append(
        "Calculating the most popular trip took %s seconds."
        % round((time.time() - start_time), 4)
    )
    print(
        "Most popular trip:            {}  (Trips: {:,})"
        .format(popular_station, popular_start_count)
        )

    return run_time_list

    #3- Trip Durations :
def trip_duration(df, trip_count, run_time_list):
    '''Prints the overall and average trip duration, from df.
       Appends 'run time info' to a list for future printing.

    Args:
        df: Pandas DataFrame.
        run_time_list: (list).
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    total_duration = df.sum()
    average_trip = total_duration/trip_count
    # Convert total trip duration to hours
    total_duration = round(total_duration/3600, 4)
    # Convert average_trip to hr, min, sec format
    m, s = divmod(average_trip, 60)
    h, m = divmod(m, 60)
    # Do not report hours if hours is 0
    if h == 0:
        average_trip = "{}min {}sec".format(int(m), round(s, 2))
    else:
        average_trip = "{}hr {}min {}sec".format(int(h), int(m), round(s, 2))
    # Save run-time info and print stats
    run_time_list.append(
        "Calculating the trip duration took %s seconds."
        % round((time.time() - start_time), 4)
    )
    print('Total trip duration:                   {:,} hours'
          .format(total_duration))
    print('Average trip duration:                 {}'.format(average_trip))

    return run_time_list

     #4-User Information
       #4.1- User Info

def user_info(df, city, run_time_list):
    '''Prints the count for two or three user types and total number of users, from df.
       Appends 'run time info' to a list for future printing.
    Args:
        df: Pandas DataFrame.
        column: (str) column name.
        run_time_list: (list).
        city: (str) name of city for df.
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    # counts the user type
    user_count = df['user_type'].value_counts()
    user_index = user_count.index

    if user_index.nunique() == 2:
        user_one_type, user_two_type = user_index
        user_one_count = user_count.loc[user_one_type]
        user_two_count = user_count.loc[user_two_type]
        print('Number of "{}" type users:       {:,}\n'
              'Number of "{}" type users:     {:,}'
              .format(
                  user_one_type, user_one_count, user_two_type, user_two_count
                  )
             )

        values = [user_one_count, user_two_count]
        labels = [user_one_type, user_two_type]
        colors = ['r','b','g']
        plt.subplots(figsize=(5, 5))
        plt.pie(x=values, labels=labels, colors = colors)
        plt.title("The differents user type who take trip for {}".format(city.title()))
    # Save run-time info and print stats
    run_time_list.append(
        "Calculating the most popular trip took %s seconds."
        % round((time.time() - start_time), 4)
    )

    return run_time_list

    #4.2-Gender Information :
def gender_info(df, column, city, run_time_list):
    '''Checks df for column.
       If column exists, prints the count for three gender types in data.
       If not, prints a statement indicating this.
    Args:
        df: Pandas DataFrame.
        column: (str) column name.
        city: (str) name of city for df.
        run_time_list: (list).
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    if column not in df:
        print('There is no gender information for this set of data.')
    else:
        # Fill missing values
        df[column].fillna('Unknown', inplace=True)
        # Find user types and counts
        gender_count = df[column].value_counts()
        gender_index = gender_count.index
        gender_type_one, gender_type_two, gender_type_three = gender_index
        gender_one_count = gender_count.loc[gender_type_one]
        gender_two_count = gender_count.loc[gender_type_two]
        gender_three_count =gender_count.loc[gender_type_three]

        print('Number of trips taken by users of {} gender:     {:,}\n'
              'Number of trips taken by users of {} gender:      {:,}\n'
              'Nubmer of trips taken by users of {} gender:        {:,}'
              .format(
                  gender_type_one, gender_one_count,
                  gender_type_two, gender_two_count,
                  gender_type_three, gender_three_count
                  )
             )

        values = [gender_one_count, gender_two_count, gender_three_count]
        labels = [gender_type_one, gender_type_two, gender_type_three]
        colors = ['g','b','r']
        plt.subplots(figsize=(5, 5))
        plt.pie(x=values, labels=labels, colors =colors)
        plt.title("The different gender take trip for  {}".format(city.title()))

    run_time_list.append(
        'Calculating the user gender counts took %s seconds.' % round((time.time() - start_time), 4)
        )

    return run_time_list

     #4.3- Birth year information
def birth_year_info(df, column, city, run_time_list):
    '''Checks df for column.
       If column exists, prints oldest and youngest user, and most common birth year.
       If not, prints a statement indicating this.

    Args:
        df: Pandas DataFrame.
        column: (str) column name.
        city: (str) name of city for df.
        run_time_list: (list).
    Returns:
        run_time_list: (list) collection of run-time info.
    '''
    start_time = time.time()
    if column not in df:
        print('There is no birth year information for this set of data.')
    else:
        # Drop missing values
        df[column].dropna(inplace=True)

        # Find youngest user with 'reality' check
        young = df[column].max().astype(int)
        if (2017 - young) < 5:
            alt_young = pd.Series(df.birth_year.unique()).nlargest(n=2).iloc[1].astype(int)
            print('Birth year of youngest user:           {} '
                  '\n(Age: {} - This result may be due to user data entry error. '
                  'The next youngest birth year is {})'
                  .format(young, 2017 - young, alt_young))
        else:
            print('Birth year of youngest user:           {} (Age: {})\n'
                  .format(young, 2017 - young))

        # Find oldest user with 'reality' check
        old = df[column].min().astype(int)
        if (2017 - old) > 75:
            alt_old = pd.Series(df.birth_year.unique()).nsmallest(n=2).iloc[1].astype(int)
            print('Birth year of oldest user:           {} '
                  '\n(Age: {} - This result may be due to user data entry error. '
                  'The next oldest birth year is {})'
                  .format(old, 2017 - old, alt_old))
        else:
            print('Birth year of oldest user:           {} (Age: {})\n'
                  .format(old, 2017 - old))

        plt.subplots(figsize=(5, 5))
        df[column].hist()
        xlabel=('birth years')
        ylabel=('number of user')
        plt.title("Birth Years of the user for {}".format(city.title()))


        pop_year = df[column].mode().loc[0].astype(int)
        pop_year_count = df[column].value_counts().loc[pop_year]

        print('Most frequent birth year:              {}  (Users: {:,})'
              .format(pop_year, pop_year_count))

    run_time_list.append(
        'Calculating the user birth year counts took %s seconds.'
        % round((time.time() - start_time), 4)
    )
    return run_time_list


def print_trip_info(df, city, trip_count, run_time_list):
    '''Combines functions duration_info, station_info, and trip_info under '---Trip Info---'.
       Appends 'run time info' to a list for future printing.

    Args:
        df: Pandas DataFrame.
        city: (str) name of city for df.
        trip_count: (int) number of rows in df.
        run_time_list: (list).
    Returns:
        run_time_list: (list).
    '''
    print('\n----Trip Information----')
    run_time_list = popular_start_station(df.start_station, city, trip_count, run_time_list)
    run_time_list = popular_end_station(df.end_station, city, trip_count, run_time_list)
    run_time_list = popular_trip(df.trip, city, trip_count, run_time_list)
    run_time_list = trip_duration(df.trip_duration, trip_count, run_time_list)

    return run_time_list

def print_user_info(df, column1, column2, city, run_time_list):
    '''Combines functions user_info, gender_info, and birth_year_info under '---User Info---'.
       Appends 'run time info' to a list for future printing.

    Args:
        df: Pandas DataFrame.
        column1: (str) column name for gender_info().
        column2: (str) column name for birth_year_info().
        city: (str) name of city for df.
        run_time_list: (list).
    Returns:
        run_time_list: (list).
    '''
    print('\n---- User Information ----')
    run_time_list = user_info(df, city, run_time_list)
    run_time_list = gender_info(df, column1, city, run_time_list)
    run_time_list = birth_year_info(df, column2, city, run_time_list)

    return run_time_list

#---------Display Data ------------#

def display_data(df):
    '''Provides the user the option of viewing five lines of data, repeating this upon request
       until the user responds with 'no'.

    Args:
        Pandas DataFrame.
    Returns:
        none.
    '''
    i = 0
    show_data = input('\nWould you like to see five lines of raw data? Type \'yes\' or \'no\'.\n')
    while show_data.lower() == 'yes':
        print(df.iloc[i:i + 5])
        i += 5
        show_data = input(
            '\nWould you like to see five more lines of raw data? Type \'yes\' or \'no\'.\n'
            )
#------------------mains()--------------#

def main():
    '''Provides statistics on start times, trips and users for bikeshare data from
       Chicago, New York and Washington based on user input.
    Args:
        none.
    Returns:
        none.
    '''
    city, file = get_city()
    time_period = get_time_period()
    # read csv file
    df = pd.read_csv(file)
    #rename by replacing space with underscore
    df.rename(columns={'Start Time': 'start_time', 'End Time': 'end_time',
                       'Trip Duration': 'trip_duration', 'Start Station': 'start_station',
                       'End Station': 'end_station', 'User Type': 'user_type', 'Gender': 'gender',
                       'Birth Year': 'birth_year'}, inplace=True)

    df['start_time'] = pd.to_datetime(df.start_time)
    df['weekday'] = df.start_time.apply(datetime.weekday)
    df['trip'] = df.start_station + " to " + df.end_station
    # Create list to collect run-time info
    run_time_list = []
  # time period filter == none
    if time_period == 'none':
        trip_count = df.shape[0]
        print_header(city, time_period)
        # Show Start Time stats
        print('---Trip  Information---'
              '\nTotal Trips: {:,}'.format(trip_count))
        run_time_list = popular_month(df.start_time, city, trip_count, run_time_list)
        run_time_list = popular_day(df.weekday, city, trip_count, run_time_list)
        run_time_list = popular_hour(df.start_time, city, trip_count, run_time_list)
        # Show Trip stats
        run_time_list = print_trip_info(df, city, trip_count, run_time_list)
        # Show User start_stats
        run_time_list = print_user_info(df, 'gender', 'birth_year', city, run_time_list)
        # Print out the run_time_info
        print('\n---Run Time Information---')
        for element in run_time_list:
            print(element)

        plt.show()
   #time period filter == month
    if time_period == 'month':
        month = get_month()
        # Update the dataframe according to the filter
        df = df.loc[df.start_time.dt.month == month]
        trip_count = df.shape[0]
        print_header(city, time_period, month_filter=month)
        # Show Start Time stats
        print('---Trip  Information ---'
              '\nTotal Trips: {:,}'.format(trip_count))
        run_time_list = popular_day(df.weekday, city, trip_count, run_time_list)
        run_time_list = popular_hour(df.start_time, city, trip_count, run_time_list)
        # Show Trip stats
        run_time_list = print_trip_info(df, city, trip_count, run_time_list)
        # Show User start_stats
        run_time_list = print_user_info(df, 'gender', 'birth_year', city, run_time_list)
        # Print out the run_time_info
        print('\n---Run Time Information---')
        for element in run_time_list:
            print(element)

        plt.show()
#time period filter ==day
    if time_period == 'day':
        # Update the dataframe according to the filter
        day = get_day()
        df = df.loc[df.weekday == day]
        trip_count = df.shape[0]
        print_header(city, time_period, day_filter=day)
        # Show Start Time stats
        print('---Trip  Infomation ---'
              '\nTotal Trips: {:,}'.format(trip_count))
        run_time_list = popular_hour(df.start_time, city, trip_count, run_time_list)

        # Show Trip stats
        run_time_list = print_trip_info(df, city, trip_count, run_time_list)

        # Show User start_stats
        run_time_list = print_user_info(df, 'gender', 'birth_year', city, run_time_list)

        # Print out the run_time_info
        print('\n---Run Time Information ---')
        for element in run_time_list:
            print(element)

        plt.show()
 #time period filter == both
    if time_period == 'both':
        # Update the dataframe according to the filter
        month = get_month()
        day = get_day()
        df = df.loc[df.start_time.dt.month == month]
        df = df.loc[df.weekday == day]
        trip_count = df.shape[0]
        print_header(city, time_period, month_filter=month, day_filter=day)
        # Show Start Time stats
        print('----Trip  Information----'
              '\nTotal Trips: {:,}'.format(trip_count))
        run_time_list = popular_hour(df.start_time, city, trip_count, run_time_list)
        # Show Trip stats
        run_time_list = print_trip_info(df, city, trip_count, run_time_list)
        # Show User start_stats
        run_time_list = print_user_info(df, 'gender', 'birth_year', city, run_time_list)
        # Print out the run_time_info
        print('\n---Run Time Informtion---')
        for element in run_time_list:
            print(element)

        plt.show()

    # Display five lines of data at a time if user specifies that  he/she would like to
    display_data(df)

    # Restart?
    restart = input('\nWould you like to restart again? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        main()
    else:
        print   ('Thanks for using this application.Hope you enjoyed the interactive session.welcome again !')

if __name__ == "__main__":
    main()
