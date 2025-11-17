import duckdb
from duckdb import DuckDBPyConnection
import pandas as pd
import streamlit as st

"""
Goal is to provide a space where data is made and then filtered, data will be returned and cached.
The cached data will only be changed when filters in sidebar are selected.
"""


@st.cache_resource
def load_duckdb() -> DuckDBPyConnection:
    con = duckdb.connect(":memory:")
    con.sql("load postgres;")
    con.sql(
        f"ATTACH 'dbname={st.secrets['database']['DB_NAME']} user={st.secrets['database']['DB_USER']} host={st.secrets['database']['DB_HOST']} password={st.secrets['database']['DB_PASSWORD']} port={st.secrets['database']['DB_PORT']}' AS supabase (TYPE postgres, SCHEMA 'public');"
    )
    return con


def get_genre_data() -> list[str]:
    con = load_duckdb()

    genre_query = """
    select
    distinct trim(lower(trim(UNNEST(STRING_SPLIT(trim(genre), ','))))) AS genre,
    from supabase.anime 
    """

    available_genres = con.sql(genre_query).df()
    available_genres["genre"].dropna(ignore_index=True, inplace=True)
    available_genres["genre"] = available_genres["genre"].sort_values(ascending=True)
    return available_genres["genre"].tolist()


def get_type_data() -> pd.DataFrame:
    con = load_duckdb()

    type_query = """
    SELECT
    type,
    count(type) as type_popularity
    from supabase.anime
    group by type
    order by type_popularity desc
    """

    types_df = con.sql(type_query).df()
    return types_df


def get_anime_data() -> pd.DataFrame:
    con = load_duckdb()

    anime_df = con.sql("select * from supabase.anime;").df()
    anime_df["genre"] = anime_df["genre"].str.strip()
    anime_df["genre"] = anime_df["genre"].str.lower()

    return anime_df
