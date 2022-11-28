
import unittest
import pandas as pd
import requests, io, imdb_analysis

class TestImdbAnalysis(unittest.TestCase):

    def setUp(self):
        ratingsurl = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
        titlesurl = 'https://datasets.imdbws.com/title.basics.tsv.gz'

        self.df_ratings = pd.read_csv(io.BytesIO(imdb_analysis.get_file_data(ratingsurl)), sep = '\t', compression = 'gzip', low_memory = False)
        self.df_titles = pd.read_csv(io.BytesIO(imdb_analysis.get_file_data(titlesurl)), sep = '\t', compression = 'gzip', low_memory = False)

    def test_movie_data_rows(self):

        data_rows, _ = imdb_analysis.get_top_n_movies(5, 100, self.df_ratings, self.df_titles)

        self.assertEqual(len(data_rows), 5)

    def test_movie_list(self):

        _ , data_list = imdb_analysis.get_top_n_movies(10, 100, self.df_ratings, self.df_titles)

        self.assertEqual(len(data_list), 10)

    def test_only_movies(self):

        data_rows, _ = imdb_analysis.get_top_n_movies(20, 100, self.df_ratings, self.df_titles)

        types = data_rows['titleType'].unique().tolist()

        self.assertEqual(types, ['movie'])

    def test_num_votes(self): 
        
        data_rows, _ = imdb_analysis.get_top_n_movies(5, 100, self.df_ratings, self.df_titles)

        self.assertGreaterEqual(data_rows['numVotes'].min(), 100)

        
if __name__ == '__main__':
    unittest.main()
