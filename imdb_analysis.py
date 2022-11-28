import pandas as pd
import requests, io

RATINGSURL = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
TITLESURL = 'https://datasets.imdbws.com/title.basics.tsv.gz'
TOP_N = 15
NUM_VOTES = 100

def get_file_data(url):
    file_from_url = requests.get(url)


    return file_from_url.content

def get_top_n_movies(top_n, min_votes, df_ratings, df_titles):
    df_titles_main = df_titles[['tconst', 'titleType', 'originalTitle']]
    df_ratings['Rank'] = (df_ratings['numVotes'] / df_ratings['numVotes'].mean()) * df_ratings['averageRating']
    df_rank = df_ratings[df_ratings['numVotes'] >= min_votes].sort_values('Rank', ascending = False)
    df_ranked_titles = df_rank.merge(df_titles_main, on='tconst')
    df_top_n_movies_data = df_ranked_titles[df_ranked_titles['titleType'].str.match('movie')].head(top_n)
    df_top_n_movies_list = df_top_n_movies_data['originalTitle'].tolist()
    
    
    return df_top_n_movies_data, df_top_n_movies_list

if __name__ == '__main__':

    df_ratings = pd.read_csv(io.BytesIO(get_file_data(RATINGSURL)), sep = ('\t'), compression ='gzip', low_memory = False)
    df_titles = pd.read_csv(io.BytesIO(get_file_data(TITLESURL)), sep = ('\t'), compression ='gzip', low_memory = False)

    top_15_movies_data, top_15_movies_list = get_top_n_movies(TOP_N, NUM_VOTES, df_ratings, df_titles)

    print(top_15_movies_data)
    print(top_15_movies_list)