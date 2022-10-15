# Code created by Helen Donohoe on 10 October 2022 & submited as Project 2 for Udacity course 'Programming for Data Science with Python'

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york, washington).
    cities = ('chicago','new york','washington')
    cities_set = set(cities)

    while True:
        city = str(input('Would you like to see data for "Chicago", "New York", or "Washington"?\n')).lower()
        if city not in cities_set:
            print('\nThat\'s not a valid city. Try again!')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    months = ('all','january','february','march','april','may','june')
    months_set = set(months)

    while True:
        month = str(input('Which month?\nEnter full month name (i.e. type January, February, March, April, May, June, or all)\n')).lower()
        if month not in months_set:
            print('\nThat\'s not a valid month. Try again!')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday')
    days_set = set(days)

    while True:
        day = str(input('Which day?\nEnter full day of week name or "all" for no day of week filter (i.e. type Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all)\n')).lower()
        if day not in days_set:
            print('\nThat\'s not a valid day of week. Try again!')
        else:
            break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station']+' to '+df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts()
    pm_name = popular_month.index[0]
    pm_count = popular_month.values[0]
    print('Most popular month:',pm_name,', Count:',pm_count)

    # display the most common day of week
    popular_day = df['day_of_week'].value_counts()
    pd_name = popular_day.index[0]
    pd_count = popular_day.values[0]
    print('Most popular day of week:',pd_name,', Count:',pd_count)

    # display the most common start hour
    popular_hour = df['hour'].value_counts()
    ph_name = popular_hour.index[0]
    ph_count = popular_hour.values[0]
    print('Most popular hour:',ph_name,', Count:',ph_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_station_start = df['Start Station'].value_counts()
    pss_name = popular_station_start.index[0]
    pss_count = popular_station_start.values[0]
    print('Most popular start station:',pss_name,', Count:',pss_count)

    # display most commonly used end station
    popular_station_end = df['End Station'].value_counts()
    pse_name = popular_station_end.index[0]
    pse_count = popular_station_end.values[0]
    print('Most popular end station:',pse_name,', Count:',pse_count)

    # display most frequent combination of start station and end station trip
    popular_trip = df['trip'].value_counts()
    pt_name = popular_trip.index[0]
    pt_count = popular_trip.values[0]
    print('Most popular trip:',pt_name,', Count:',pt_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_durn_sum_sec = np.sum(df['Trip Duration'])
    trip_durn_sum_hrs = np.sum(df['Trip Duration']) / 3600
    print('Total travel time:',trip_durn_sum_sec,'seconds or',round(trip_durn_sum_hrs,2),'hours')

    # display mean travel time
    trip_durn_av_sec = np.mean(df['Trip Duration'])
    trip_durn_av_mins = np.mean(df['Trip Duration']) / 60
    print('Average travel time:',int(round(trip_durn_av_sec,0)),'seconds or',round(trip_durn_av_mins,2),'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n',user_types,'\n')

    # Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print('Counts of genders:\n',genders,'\n')
    except:
        print('Gender data not available for this city')

    # Display earliest, most recent, and most common year of birth
    try:
        dob_year_earliest = np.min(df['Birth Year'])
        dob_year_latest = np.max(df['Birth Year'])
        dob_years = df['Birth Year'].value_counts()
        print('Earliest year of birth:',int(dob_year_earliest),'\nMost recent year of birth:',int(dob_year_latest),'\nMost common year of birth:',int(dob_years.index[0]))
    except:
        print('Year of birth data not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of individal data at a time"""

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        pd.set_option('display.max_columns',200)
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('Do you wish to continue? Enter yes or no:').lower()
        if view_data != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
