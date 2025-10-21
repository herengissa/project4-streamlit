import pandas as pd

# Ladda datasetet
df = pd.read_csv("data/movie_ratings.csv")

# 1. Beräkna medelbetyg
mean_rating = df["rating"].mean()

# 2. Filtrera filmer efter år
recent_movies = df[df["year"] > 2020]

# 3. Grupp och aggregera: genomsnittligt betyg per genre
avg_rating_by_genre = df.groupby("genre")["rating"].mean()

# Spara resultat
mean_rating_df = pd.DataFrame({"mean_rating": [mean_rating]})
mean_rating_df.to_csv("output/mean_rating.csv", index=False)
recent_movies.to_csv("output/recent_movies.csv", index=False)
avg_rating_by_genre.to_csv("output/avg_rating_by_genre.csv")