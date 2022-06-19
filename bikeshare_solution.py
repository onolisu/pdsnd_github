import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city = input('\nDo you want to explore the bikeshare data of Chicago, New York City or Washington?\n').lower()
    while city not in CITY_DATA:
        city = input('\nSorry! This is not a valid input. Please select a city among Chicago, New York City or Washington:\n').lower()

    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month of data do you want to look at? Type a month from January to June. Type "all" if you want to look at all months.\n').title()
    while month not in months:
        month = input('\nSorry! This is not a valid input. Please type a month from January to June or type "all" if you want to look at all months.\n').title()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nDo you want to look at data on a specific day of the week? Type a day of the week. Type "all" if you want to look at all week days.\n').title()
    while day not in days:
        day = input('\nSorry! This is not a valid input. Please type a day of the week (e.g. Monday) or type "all" if you want to look at all days.\n').title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "All" to apply no month filter
        (str) day - name of the day of week to filter by, or "All" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of the Week'] = df['Start Time'].dt.day_name()

    if month != 'All':
        df = df[df['Month'] == month]
    if day!= 'All':
        df = df[df['Day of the Week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    time.sleep(2)
    start_time = time.time()

    # display the most common month
    print('\nThe most popular month of travel is:', df['Month'].mode()[0])

    # display the most common day of week
    print('\nThe most popular day of week to travel is:', df['Day of the Week'].mode()[0])

    # display the most common start hour
    print('\nThe most popular start hour (in 24-hour clock) of travel is:', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    time.sleep(2)
    start_time = time.time()

    # display most commonly used start station
    print('\nThe most popular start station is:', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nThe most popular end station is:', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('\nThe most popular combination of start and end station is:', (df['Start Station'] + ' and ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    time.sleep(2)
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('\nThe total trip duration is:', total_time, 'minutes or {} days {} hours and {} minutes'.format(total_time // (60 * 24), total_time % (60 * 24) // 60, total_time % (60 *24) % 60))

    # display mean travel time
    average_time = df['Trip Duration'].mean()
    print('\nThe average trip duration is:', average_time, 'minutes or {} hours and {} minutes'.format(average_time // 60, average_time % 60))

    print("\nThis took %s seconds." % (time.time() - start_time))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    time.sleep(2)
    start_time = time.time()

    # Display counts of user types
    print('\nThe user type profile in the selected dataset is:\n', df['User Type'].value_counts())

    # Display counts of gender
    if city == 'washington':
        return
    else:
        print('\nThe gender profile in the selected dataset is:\n', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    print('\nThe earliest year of birth for the users is:', int(df['Birth Year'].min()))
    print('\nThe most recent year of birth for the users is:', int(df['Birth Year'].max()))
    print('\nThe most common year of birth for the users is:', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))


def review_raw_data(df):
    """Displays selected raw data upon request. 5 rows at a time."""
    display = input('\nWould you like to see the raw data? Enter yes or no.\n').lower()
    while display != 'yes' and display != 'no':
        display = input('\nSorry! This is not a valid input. Would you like to see the raw data? Enter yes or no.\n').lower()
    if display == 'no':
        return
    if display == 'yes':
        print('\nThere is a total of {} rows of data.'.format(len(df.index)))
        print('\nDisplaying the first 5 rows of data...\n', df.head())

        # Ask if the user want to keep looking at raw data. Display 5 rows of data at a time until the user says 'no' or there is not more data to display.
        start_line = 5
        while start_line < len(df.index):
            display = input('\nWould you like to keep looking at the raw data? Enter yes or no.\n').lower()
            while display != 'yes' and display != 'no':
                display = input('\nSorry! This is not a valid input. Would you like to keep looking at the raw data? Enter yes or no.\n').lower()
            if display == 'no':
                return
            elif display == 'yes' and start_line + 5 < len(df.index):
                print('\nDisplaying the rows {} to {}...\n'.format(start_line + 1, start_line + 5), df[start_line : start_line + 5])
                start_line += 5
            else: 
                print('\nDisplaying the rows {} to {}...\n'.format(start_line + 1, len(df.index)), df[start_line : ])
                start_line += 5


def main():
    while True:
        global city
        city, month, day = get_filters()
        print('\nBased on your request, we will now review data in the following city and time :\nCity: {}, Month: {}, Day: {}'.format(city.title(), month, day))
        print('-'*40)
        df = load_data(city, month, day)

        time_stats(df)
        print('-'*40)

        station_stats(df)
        print('-'*40)

        trip_duration_stats(df)
        print('-'*40)

        user_stats(df)
        print('-'*40)

        review_raw_data(df)
        print('-'*40)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart != 'yes' and restart != 'no':
                restart = input('\nSorry! This is not a valid input. Would you like to restart? Enter yes or no.\n').lower()
        if restart == 'no':
            print('\nThank you for using our program! Have a great day!\n')
            break


if __name__ == "__main__":
	main()
