import streamlit as st
import pandas as pd
from app.data import get_anime_data, get_genre_data, get_type_data

st.header(":blue[MyAnimeList (MAL)] Dashboard")

if "original_anime_df" not in st.session_state:
    st.session_state["original_anime_df"] = get_anime_data()

if "genres" not in st.session_state:
    st.session_state["genres"] = get_genre_data()

if "types" not in st.session_state:
    st.session_state["types"] = get_type_data()

anime_df_to_process: pd.DataFrame = st.session_state["original_anime_df"].copy()

with st.sidebar:
    st.session_state["genres_selected"] = st.multiselect(
        ":blue[What genres would you like!]", st.session_state["genres"]['genres'].to_list()
    )

    types_df: pd.DataFrame = st.session_state["types"]
    st.session_state["types_selected"] = st.multiselect(
        ":blue[What formats do you want to account for?]", types_df["type"].to_list()
    )

    st.session_state["members_ranges"] = st.slider(
        label=":blue[What range of members for the anime do you want?]",
        min_value=st.session_state["original_anime_df"]["members"].min(),
        max_value=st.session_state["original_anime_df"]["members"].max(),
        value=(
            st.session_state["original_anime_df"]["members"].min(),
            st.session_state["original_anime_df"]["members"].max(),
        ),
        format="%.0f",
    )

    st.session_state["id_ranges"] = st.slider(
        label=":blue[What range of Anime IDs do you want?]",
        min_value=st.session_state["original_anime_df"]["anime_id"].min(),
        max_value=st.session_state["original_anime_df"]["anime_id"].max(),
        value=(
            st.session_state["original_anime_df"]["anime_id"].min(),
            st.session_state["original_anime_df"]["anime_id"].max(),
        ),
        format="%.0f",
    )


if st.session_state["genres_selected"]:
    genres_string: str = "|".join(st.session_state["genres_selected"])
    anime_df_to_process = anime_df_to_process[
        anime_df_to_process["genre"].str.contains(genres_string)
    ]

if st.session_state["types_selected"]:
    anime_df_to_process = anime_df_to_process[
        anime_df_to_process["type"].isin(st.session_state["types_selected"])
    ]

if st.session_state["members_ranges"]:
    anime_df_to_process = anime_df_to_process[
        anime_df_to_process["members"].between(
            st.session_state["members_ranges"][0],
            st.session_state["members_ranges"][1],
            inclusive="both",
        )
    ]

if st.session_state["id_ranges"]:
    anime_df_to_process = anime_df_to_process[
        anime_df_to_process["anime_id"].between(
            st.session_state["id_ranges"][0],
            st.session_state["id_ranges"][1],
            inclusive="both",
        )
    ]


column_configs = {}
for col in anime_df_to_process.columns:
    if col == "rating":
        column_configs[col] = st.column_config.ProgressColumn(
            "Rating",
            help="Star rating of the Anime.",
            min_value=0,
            max_value=10,
            format="⭐ %.2f",
        )
    else:
        column_configs[col] = st.column_config.Column(
            label=col.replace("_", " ").title(), help=f"The {col} of the Anime."
        )

with st.expander("Anime Dataframe", icon=":material/dataset:"):
    st.dataframe(anime_df_to_process, hide_index=True, column_config=column_configs)
