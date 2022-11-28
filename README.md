# Daemon
A Pyhton application using Pandas library for an IMDb analysis

1) Selects constants which can be changed later for the python application.
2) first function uses requests to ingest data from URL.
3) function get_top_n_movies accepts 4 parameters.
 i) Creates a dataframe of title names with only the three columns we need for analysis.
 ii) Assigns a rank to the the ratings dataframe based of given calculation and appends these results into a new column 'Rank'.
 iii) Sorts data based of the ranking column in descending order, where the numVotes is atleast the minimum specified.
