import streamlit as st
import pandas as pd
from app.data import get_anime_data, get_genre_data, get_type_data
from app.charts import get_charts

st.header(":blue[MyAnimeList (MAL)] Dashboard")


if "original_anime_df" not in st.session_state:
    st.session_state["original_anime_df"] = get_anime_data()

if "genres" not in st.session_state:
    st.session_state["genres"] = get_genre_data()

if "types" not in st.session_state:
    st.session_state["types"] = get_type_data()


@st.cache_data()
def anime_data_copy():
    return st.session_state["original_anime_df"].copy()


anime_df_to_process: pd.DataFrame = anime_data_copy()


with st.sidebar:
    st.session_state["genres_selected"] = st.multiselect(
        ":blue[What genres would you like!]", st.session_state["genres"]
    )

    st.session_state["types_selected"] = st.multiselect(
        ":blue[What formats do you want to account for?]", st.session_state["types"]
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


original_df = st.session_state["original_anime_df"]

AGGREGATIONS = {
    "Average": "mean",
    "Median": "median",
    "Minimum": "min",
    "Maximum": "max",
}

METRIC_SPECS = [
    {"column": "rating", "label": "Rating", "format": ".2f"},
    {"column": "members", "label": "Members", "format": ".0f"},
]

metric_data = []

# 2. Calculate all metrics in a loop
for spec in METRIC_SPECS:
    col_name = spec["column"]
    value_format = spec["format"]
    
    if anime_df_to_process.empty:
        for agg_label in AGGREGATIONS:
             metric_data.append({
                "label": f"{agg_label} {spec['label']}",
                "value": 0,
                "delta": 0,
                "value_format": value_format,
            })
        continue

    for agg_label, agg_func_name in AGGREGATIONS.items():
        agg_func = getattr(pd.Series, agg_func_name)

        current_value = agg_func(anime_df_to_process[col_name])
        original_value = agg_func(original_df[col_name])
        
        delta = current_value - original_value

        metric_data.append({
            "label": f"{agg_label} {spec['label']}",
            "value": current_value,
            "delta": delta,
            "value_format": value_format,
        })


# Display Rating Metrics
st.subheader(":blue[Rating Metrics]")
cols_rating = st.columns(4)
for i, data in enumerate(metric_data[:4]):
    cols_rating[i].metric(
        label=data["label"],
        value=f"{data['value']:{data['value_format']}}",
        delta=f"{data['delta']:{data['value_format']}}",
    )

st.subheader(":blue[Member Count Metrics]")
cols_members = st.columns(4)
for i, data in enumerate(metric_data[4:8]):
    cols_members[i].metric(
        label=data["label"],
        value=f"{data['value']:{data['value_format']}}",
        delta=f"{data['delta']:{data['value_format']}}",
    )


charts = get_charts(anime_df_to_process)
for chart in charts:
    st.plotly_chart(chart)


with st.expander("Anime Dataframe", icon=":material/dataset:"):
    st.dataframe(anime_df_to_process, hide_index=True, column_config=column_configs)