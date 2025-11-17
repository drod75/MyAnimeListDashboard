import plotly.express as px


def types_pie_chart(df):
    types = df.groupby("type")["type"].count().reset_index(name="count")

    fig = px.pie(
        types,
        values="count",
        names="type",
        title="Anime Format Pie Chart",
        subtitle="A chart to showcase the types of formats available for anime.",
    )
    return fig


def genre_bar_chart(df):
    genres = df["genre"].str.split(",").explode("")
    genres = genres.to_frame()
    genres["genre"] = genres["genre"].str.strip()
    genres["genre"] = genres["genre"].str.lower()
    genres_gb = genres.groupby("genre")["genre"].count().reset_index(name="count")
    genres_gb.sort_values(by="count", ascending=False, inplace=True)
    genres_gb = genres_gb.iloc[:-1]

    fig = px.bar(
        genres_gb.head(10),
        x="genre",
        y="count",
        title="Top 10 Genres",
        subtitle="A plot of the top 10 genres within Anime on MAL.",
        color="genre",
    )
    return fig


def get_charts(df):
    types_pie = types_pie_chart(df)
    genre_bar = genre_bar_chart(df)
    return [types_pie, genre_bar]
