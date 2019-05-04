import time
import pandas as pd
import numpy as np


"""
######################
python version: 3.7.3
pandas version: 0.24.2
numpy version: 1.16.2
######################
"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }
############### city list as a global variable
cities = ['chicago', 'newyork', 'washington']
############### day list as a global variable
days = ['1', '2', '3', '4', '5', '6', '7']
############### month list as a global variable
months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi! Let\'s explore some US bikeshare data!')
############### get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like to see data for Chicago, New York, or Washington?").strip().lower().replace(" ", "")
        if city in cities:
            break
        else:
            print("Sorry. Type a name of the cities given again")
            continue
############### checking whether to filter the data and filter them
    while True:
        filtering = input("\nWould you like to filter the data by month, day, both, or not at all? Type 'none' for no time filter.")
        if filtering == 'month':
            while True:
                month = input("\nWhich month? January, February, March, April, May, or June?").strip().lower()
                if month in months:
                    break
                else:
                    print("Sorry that is not a valid input")
                    continue
            day = 'all'
            break
        elif filtering == 'day':
            while True:
                day = input("\nWhich day? Please type your reponse as an integer (e.g. 1 = Sunday)")
                if day in days:
                    break
                if day.isalpha():  ############### I added it because if a string input caused a ValueError.
                    print("Sorry that is not a valid input")
                    continue
                else:
                    print("Sorry that is not a valid input")
                    continue
            month = 'all'
            break
        elif filtering == 'both':
            while True:
                month = input("\nWhich month? January, February, March, April, May, or June?").strip().lower()
                if month in months:
                    break
                else:
                    print("Sorry that is not a valid input")
                    continue
            while True:
                day = input("\nWhich day? Please type your reponse as an integer (e.g. 1 = Sunday)")
                if day in days:
                    break
                if day.isalpha(): ############### I added it because if a string input caused a ValueError.
                    print("Sorry that is not a valid input")
                    continue
                else:
                    print("Sorry that is not a valid input")
                    continue
            break
        elif filtering == 'none':
            month = 'all'
            day = 'all'
            print('*'*40)
            print("\nYou have chosen not to filter the data")
            print("\nThe statistics is based on the unfiltered data(all months and days from", city.title() + ")")
            print("\n")
            print('*'*40)
            break
        else:
            print("Sorry. Type a name of the cities given again")
            continue
    print('-'*40)
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        aweek = {'1':'sunday', '2':'monday', '3':'tuesday', '4':'wednesday', '5':'thursday', '6':'friday', '7':'saturday'}

        df = df[df['day_of_week'] == aweek[day].title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    month_ch = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    print('The most common month:', month_ch[common_month])

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week:', common_day)

    # display the most common start hour
    common_start = df['hour'].mode()[0]
    print('The most start time: ' + str(common_start) + ':00' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', '<' + str(common_start_station) + '>')

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:','<' + str(common_end_station) + '>')

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + '_to_' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('The most commonly used combination:', '<' + str(common_combination) + '>')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip = df['Trip Duration'].sum()
    print('The total travel time is:', str(int(total_trip/3600)) + ' hour(s) '+ str(int(total_trip%3600)) + ' minute(s)')
    # display mean travel time
    average_trip = df['Trip Duration'].mean()
    print('The average tral time is:', str(int(average_trip/60)) + ' minute(s)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser types are:',user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender_type = df['Gender'].value_counts()
        print('\nGender types are:\n',gender_type)
    else:
        print('\nThere is no gender information')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        common_year_b = df['Birth Year'].mode().min()
        print('\nThe most common year of birth:\n', common_year_b)
        ############### earliest birth!
        earliest_birth = df['Birth Year'].min()
        print('\nThe most earliest year of birth:\n', earliest_birth)
        ############### recent birth!
        most_recent_birth = df['Birth Year'].max()
        print('\nThe most recent year of birth:\n', most_recent_birth)

    else:
        print('\nThere is no birth information')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to explore the data more? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
