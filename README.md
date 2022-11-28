# Daemon IMDb Top 15 Movies Analysis

A Python application using the Pandas library for an IMDb analysis.

1) Selects constants for functions.

2) First get_data function uses the requests library to ingest data from URLs.

3) Next the get_top_n_movies function accepts 4 parameters and has the following behaviour:

    i) Creates a dataframe of title names with only the three columns we need for analysis.
    ii) Assigns a rank to the the ratings dataframe based of given calculation and appends these results into a new column: 'Rank'.
    iii) Sorts data based of the 'Rank' column in descending order, where the numVotes is atleast the minimum specified (100).
    iv) Joins the titles dataframes onto the appended ratings dataframe on primary key: 'tconst'.
    v) Produces a dataframe of the top n (15) titles where the titleType column is restricted to 'movie' where the minimum number of votes is m (100).
    vi) Produces a list of only the movie titles from v).

4) The script for the unit test and the unit test results are also included. There are four tests which check that the functions work as intended.
