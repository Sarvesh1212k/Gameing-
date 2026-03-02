import streamlit as st
import pandas as pd
from google_play_scraper import search

from utils.helpers import platform_type, parse_installs
@st.cache_data
def load_pc_console():
        df = pd.read_csv("video_game_sales.csv")
        df.columns = df.columns.str.lower()
        df.rename(columns={
            "console":"platform",
            "critic_score":"rating",
            "total_sales":"downloads",
            "img":"image"
        }, inplace=True)
        df["rating"] = df["rating"].fillna(0) / 2
        # df["downloads"] = df["downloads"].fillna(0)
        df["downloads"] = pd.to_numeric(df["downloads"], errors="coerce")

# PC/Console sales are already in Millions
        df["downloads"] = df["downloads"].fillna(10)   # default = 10M
        df.loc[df["downloads"] <= 0, "downloads"] = 10
        


        df["platform_type"] = df["platform"].apply(platform_type)
        df = df[df["rating"] > 0].drop_duplicates("title")
        df["game_id"] = df["title"] + "_pc"
        return df

@st.cache_data(ttl=3600)
def load_mobile():
        rows = []
        for kw in ["top games","action games","racing games"]:
            for app in search(kw, lang="en", country="in", n_hits=30):
                rating = app.get("score")
                installs = parse_installs(app.get("installs"))
                if rating:
                    rows.append({
                        "game_id":app.get("appId"),
                        "title":app.get("title"),
                        "genre":"Mobile",
                        "publisher":app.get("developer"),
                        "developer":app.get("developer"),
                        "rating":rating,
                        "downloads":installs or 500_000,
                        "platform_type":"Mobile",
                        "image":app.get("icon")
                    })
        return pd.DataFrame(rows)

# df_games = pd.concat([load_pc_console(), load_mobile()], ignore_index=True)

def load_all_games():
    return pd.concat([load_pc_console(), load_mobile()], ignore_index=True)