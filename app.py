import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ladda data
df = pd.read_csv("data/movie_ratings.csv")

st.title("🎬 Movie Ratings Explorer")

# Visa rådata
st.subheader("Raw Data")
st.dataframe(df)

# Sidebar-filter
st.sidebar.header("Filter")
year_range = st.sidebar.slider("Select Year Range", int(df["year"].min()), int(df["year"].max()), (2010, 2025))
selected_genre = st.sidebar.selectbox("Select Genre", df["genre"].unique())

# Filtrera data
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]
filtered_df = filtered_df[filtered_df["genre"] == selected_genre]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Plot: Genomsnittligt betyg per år
st.subheader("Average Rating Over Time")
avg_rating_by_year = filtered_df.groupby("year")["rating"].mean()

fig, ax = plt.subplots()
avg_rating_by_year.plot(kind="line", ax=ax)
ax.set_ylabel("Average Rating")
st.pyplot(fig)