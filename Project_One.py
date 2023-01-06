import pandas as pd
import numpy as np
import time

CITY_DATA = {'chicago': 'chicago.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # city = input(
    #     "Would You Like To See Data For Chicago , New York, Or Washington?").lower()

    # get user input for month (all, january, february, ... , june)
    # month = input(
    #     "Which Month? January, February, March, April, May or June? or all to no month filter").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # day = (input("Which day?")).lower()
    city = input(
        "Would You Like To See Data For Chicago Or Washington? ").lower().strip()
    while city not in CITY_DATA.keys():
        city = input(
            "Would You Like To See Data For Chicago Or Washington? ").lower().strip()

    month = input(
        "Which Month? January, February, March, April, May or June? or 'all' to no month filter ").lower().strip()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input(
            "Which Month? January, February, March, April, May or June? or 'all' to no month filter ").lower().strip()

    day = (input(
        "Which day? saturday, sunday, monday, tuesday, wednesday, thursday, friday or 'all' To No Day Filter ")).lower().strip()
    while day not in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
        day = (input(
            "Which day? saturday, sunday, monday, tuesday, wednesday, thursday, friday or 'all' To No Day Filter ")).lower().strip()

    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # print(df.isnull().any())
    if city == 'chicago' or city == 'new york city':
        df.fillna(method='ffill', axis=0, inplace=True)
        # print(df.isnull().any())

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # print(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # print(df['month'])
    # print(df['day_of_week'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

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
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print("The Most Common Month Is:", months[common_month - 1])
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The Most Common Day Is:", common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The Most Common Hour Is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most Common Start Station Is: ', common_start_station)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The Most Common End Station Is: ', common_end_station)

    # display most frequent combination of start station and end station trip
    combination = df['Start Station'].astype(
        str) + '\n' + df['End Station'].astype(str)
    most_ferq_comb = combination.mode()[0]
    print('Most Frequent Combination Of Start Station And End Station Trip Is:\n', most_ferq_comb)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time Is:', total_travel_time)
    # display mean travel time
    mean_traver_time = df['Trip Duration'].mean()
    print('The average Travel Time Is:', mean_traver_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print("The Counts Of User Types Is:\n", count_of_user_types)

    # Display counts of gender
    if city != 'washington':
        counts_of_gender = df['Gender'].value_counts()
        print("The Counts Of Gender:\n", counts_of_gender)
    else:
        pass

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_year_of_birth = df['Birth Year'].min()
        print("The Earliest Year Of Birth Is :", earliest_year_of_birth)
        most_recent_year_of_birth = df['Birth Year'].max()
        print("The Most Recent Year Of Birth Is :", most_recent_year_of_birth)
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print("The Most Common Year Of Birth Is :", most_common_year_of_birth)
    else:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_raw_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").strip().lower()
    start_loc = 0

    while view_data != 'no':
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower().strip()
        if view_display == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
