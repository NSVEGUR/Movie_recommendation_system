import pandas as pd

class Preprocess():
	def __init__(self):
		self.df_credits = pd.read_csv("./Input/tmdb_5000_credits.csv")
		self.df_movies = pd.read_csv("./Input/tmdb_5000_movies.csv")
		self.df = self.__merge_csv__()
	
	def __merge_csv__(self):
		self.df_credits.columns = ["id", "title", "cast", "crew"]
		self.df_credits.drop("title", inplace=True, axis=1)
		df = self.df_movies.merge(self.df_credits, on="id")
		return df

	
	def clean_nan(self):
		#Dropping home page column as it contains more null values and not required for our recommendation system
		self.df.drop(["homepage"], axis=1, inplace=True)
		#tagline column is required in content based selections so lets replace its null values with unknown
		self.df["tagline"].fillna("Unknown", inplace=True)
		#Removing overview, release date and runtime null rows as their count is very low
		self.df = self.df.loc[self.df["overview"].notna()]
		self.df = self.df.loc[self.df["runtime"].notna()]
		self.df = self.df.loc[self.df["release_date"].notna()]
	
	def process(self):
		self.clean_nan()
		return self.df




data = Preprocess()
df = data.process()


