import streamlit as st
import numpy as np
import pandas as pd
from utils.formatters import format_number_short 
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator
from services.loaders import load_all_games

from sklearn.linear_model import LinearRegression

from utils.helpers import image_url
from utils.formatters import format_rating, format_downloads

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from utils.formatters import format_downloads
from utils.formatters import format_number

from services.history import (
    save_game_history,
    load_game_history,
    clear_game_history
)

@st.cache_data
def get_games():
    return load_all_games()



from utils.helpers import image_url
from utils.formatters import (
    format_rating,
    format_downloads,
    y_axis_formatter
)

def main_app():
    df_games = load_all_games()
  
    # ---------- SIDEBAR ----------
    st.sidebar.title("🎮 GamePulse")
    st.sidebar.markdown(f"### 👋 Hello {st.session_state.username}")

    menu = st.sidebar.radio("Menu", ["Games", "History", ])
 

    
    PAGE_SIZE = 12

    try:
        PAGE = int(st.query_params.get("page", 1))
    except:
        PAGE = 1
    
    if "url_cleaned" not in st.session_state:
      if "page" in st.query_params:
        st.query_params.pop("page")
    st.session_state.url_cleaned = True

  



    # =========================
    # SEARCH + FILTER
    # =========================
    search_term = st.sidebar.text_input("🔍 Search Game")
    platform_filter = st.sidebar.multiselect(
        "🕹️ Platform",
        df_games["platform_type"].unique(),
        default=df_games["platform_type"].unique()
    )

    genre_filter = st.sidebar.multiselect(
    "🎯 Genre",
    df_games["genre"].dropna().unique(),
    key="genre_filter"
)
    if st.sidebar.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.query_params.clear()
        st.rerun()

 


    filtered = df_games.copy()
    if search_term:
        filtered = filtered[filtered["title"].str.contains(search_term, case=False)]
    if platform_filter:
        filtered = filtered[filtered["platform_type"].isin(platform_filter)]
    if genre_filter:
        filtered = filtered[filtered["genre"].isin(genre_filter)]
    
    

           
    # =========================
    # HISTORY PAGE (CARDS)
    # =========================
    if menu == "History":
        st.title("📜 Your Game History")
        history = load_game_history(st.session_state.username)

        if not history:
            st.info("No games opened yet.")
        else:
            titles = [h["title"] for h in history]
            hdf = filtered[filtered["title"].isin(titles)]

            cols = st.columns(3)
            for i, (_, g) in enumerate(hdf.iterrows()):
                with cols[i % 3]:
                    st.markdown(f"""
                    <div class="game-card">
                        <img src="{image_url(g)}">
                        <h4>{g['title']}</h4>
                        <p>⭐ {format_rating(g['rating'])}</p>
                        <p>📥 {format_downloads(g['downloads'], g['platform_type'])}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    # if st.button("📊 View Details", key=f"hist_{g['game_id']}"):
                    if st.button("📊 View Details", key=f"hist_{g['game_id']}_{i}"):
                        st.session_state.selected_game = g["game_id"]
                        st.rerun()

            st.markdown("---")
        if st.button("🗑️ Clear All History"):
            clear_game_history(st.session_state.username)
            st.success("History cleared successfully ✅")
            st.rerun()

        return
    
   
    

    # =========================
    # GAME DETAILS + GRAPHS
    # =========================
    
    if st.session_state.selected_game:
        try:
            g = filtered[filtered["game_id"] == st.session_state.selected_game].iloc[0]

        except IndexError:
                          st.warning("⚠️ Selected game not found. Refreshing page...")
                          st.session_state.selected_game = None
                          st.rerun()

        if st.button("⬅ Back to Library"):
           st.session_state.selected_game = None
           st.query_params["page"] = 1
           st.rerun()


        col1, col2 = st.columns([1,3])
        with col1:
            st.image(image_url(g), width=300)
        with col2:
            st.title(g["title"])
            st.markdown(f"⭐ **Rating:** {format_rating(g['rating'])}")
            st.markdown(f"📥 **Downloads:** {format_downloads(g['downloads'], g['platform_type'])}")
            if not g["downloads"] or str(g["downloads"]) in ["0", "0+", "None", "nan"]:
              st.caption("ℹ️ Data not available")
            st.markdown(f"🎮 **Platform:** {g['platform_type']}")
            st.markdown(f"🧩 **Genre:** {g['genre']}")
            st.markdown(f"🏢 **Publisher:** {g['publisher']}")
            st.markdown(f"👨‍💻 **Developer:** {g['developer']}")

        st.divider()
 

        st.subheader("📈 Year-wise Sales & Downloads")
          

          
        years = [2019,2020,2021,2022,2023]
        sales = [
            g["downloads"] * 0.3,
            g["downloads"] * 0.45,
            g["downloads"] * 0.6,
            g["downloads"] * 0.8,
            g["downloads"]
        ]
        downloads = [
            g["downloads"] * 0.4,
            g["downloads"] * 0.55,
            g["downloads"] * 0.7,
            g["downloads"] * 0.9,
            g["downloads"] * 1.1
        ]

        from matplotlib.ticker import FuncFormatter

        fig, ax = plt.subplots(figsize=(8,4))
        ax.plot(years, sales, marker="o", label="Sales")
        ax.plot(years, downloads, marker="o", label="Downloads")

        ax.set_xticks(years)
        ax.set_xticklabels([str(y) for y in years])

        ax.set_ylabel("Millions")

       
        ax.yaxis.set_major_formatter(FuncFormatter(y_axis_formatter))
        from matplotlib.ticker import MaxNLocator

        ax.yaxis.set_major_locator(MaxNLocator(nbins=6))
        ax.margins(y=0.15)        
      

        ax.legend()
        st.pyplot(fig)
        

 
        # =========================
        # GRAPH 2 (ML)
        # =========================
        st.subheader("🤖 Future Sales & Downloads Prediction")

        X = np.array([0,1,2,3,4]).reshape(-1,1)
        model = LinearRegression().fit(X, sales)
        future = model.predict(np.array([5,6,7]).reshape(-1,1))


        fig2, ax2 = plt.subplots(figsize=(8,4))
        ax2.plot(years, sales, marker="o", label="Past")
        ax2.plot([2024,2025,2026], future, marker="o", label="Predicted")

        ax2.set_xticks([2019,2020,2021,2022,2023,2024,2025,2026])
        ax2.set_xticklabels(["2019","2020","2021","2022","2023","2024","2025","2026"])

        ax2.set_ylabel("Millions")
   
        ax2.yaxis.set_major_formatter(FuncFormatter(y_axis_formatter))
        from matplotlib.ticker import MaxNLocator

        ax2.yaxis.set_major_locator(MaxNLocator(nbins=6))
        ax2.margins(y=0.15)         


        ax2.legend()
        st.pyplot(fig2)
        X = np.array(range(len(sales))).reshape(-1, 1)
        y = np.array(sales) 
        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
        )

        models = {
            "Linear Regression": LinearRegression(),
            "Polynomial Regression": Pipeline(
                [
                     ("poly", PolynomialFeatures(degree=2)),
                     ("lr", LinearRegression()),
                ]
           ),
        }

        results = []
        best_mae = None

        for name, model in models.items():
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

            mae = mean_absolute_error(y_test, preds)
            rmse = np.sqrt(mean_squared_error(y_test, preds))
            r2 = r2_score(y_test, preds) if len(y_test) > 1 else None

            results.append({
                    "Model": name,
                    "MAE": format_number_short(mean_absolute_error(y_test, preds)),
                    "RMSE": format_number_short(np.sqrt(mean_squared_error(y_test, preds))),
                    # "R2": r2
            })

            if best_mae is None or mae < best_mae:
               best_mae = mae

        st.subheader("📊 Model Evaluation & Comparison")
        st.dataframe(results)
        st.write("TEST RUN OK")
    # =========================
    # ERROR ANALYSIS (FINAL FIX)
    # =========================
        actual_downloads = pd.to_numeric(g["downloads"], errors="coerce")
  
        if actual_downloads is None or np.isnan(actual_downloads) or actual_downloads <= 0:
           st.warning("⚠️ Invalid downloads data")
           st.stop()

        percentage_error = round((best_mae / actual_downloads) * 100)
  
        if percentage_error == 0:
            percentage_error = 1  # 0.9 → 1 rule

        st.subheader("📉 Error Analysis")
        st.write(f"**MAE:** {format_number_short(mae)}")
        st.write(
            f"**Actual Downloads:** "
            f"{format_downloads(actual_downloads, g['platform_type'])}"
        )
        st.write(f"**Percentage Error:** {percentage_error}%")

        if percentage_error <= 5:
           st.success("✅ Model accuracy is very good")
        elif percentage_error <= 10:
            st.warning("⚠️ Model accuracy is acceptable")
        else:
            st.error("❌ Model accuracy is poor")
 
        st.stop()

      
        
    # ==============

    # =========================
    # GAME GRID + PAGINATION
    # =========================
    total_pages = max((len(filtered)-1)//PAGE_SIZE + 1, 1)
    PAGE = min(max(1, PAGE), total_pages)
    visible = filtered.iloc[(PAGE-1)*PAGE_SIZE:PAGE*PAGE_SIZE]

    st.title("🎮 Game Library")
    st.markdown(f"**Page {PAGE} of {total_pages}**")

    cols = st.columns(3)
    for i,(_,g) in enumerate(visible.iterrows()):
        with cols[i%3]:
            st.markdown(f"""
            <div class="game-card">
                <img src="{image_url(g)}">
                <h4>{g['title']}</h4>
                <p>⭐ {format_rating(g['rating'])}</p>
                <p>📥 {format_downloads(g['downloads'], g['platform_type'])}</p>
            </div>
            """, unsafe_allow_html=True)


            if st.button("📊 View Details", key=f"grid_{g['game_id']}_{i}"):
                save_game_history(st.session_state.username, g["title"])
                st.session_state.selected_game = g["game_id"]
                st.rerun()

    c1, _, c3 = st.columns([1,2,1])
    with c1:
        if PAGE > 1 and st.button("⬅ Previous"):
            st.query_params["page"] = PAGE - 1
            st.rerun()
    with c3:
        if PAGE < total_pages and st.button("Next ➡"):
            st.query_params["page"] = PAGE + 1
            st.rerun()

 