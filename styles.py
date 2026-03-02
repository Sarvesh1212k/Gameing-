
STYLE = """
<style>
/* Global reset for auth page only */
body {
    background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%) !important;
    min-height: 100vh;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* Hide Streamlit chrome ONLY on auth page */
#MainMenu, footer, .stDeployButtonContainer {visibility: hidden;}
.stApp { 
    padding-top: 3rem;
    background: transparent !important;
}

/* Main auth container */
.auth-container {
    max-width: 1000px;
    margin: 2rem auto;
    display: flex;
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.25);
    background: white;
    min-height: 600px;
}

/* Left panel - Branding */
.auth-brand {
    flex: 1;
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
    padding: 3rem;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.auth-brand h1 {
    font-weight: 800;
    font-size: 2.8rem;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    text-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
.auth-brand p {
    font-size: 1.2rem;
    opacity: 0.9;
    max-width: 400px;
    line-height: 1.6;
}
.auth-brand-logo {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    text-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Right panel - Forms */
.auth-forms {
    flex: 1;
    padding: 3rem;
    display: flex;
    flex-direction: column;
}

/* Tabs styling */
.stTabs [data-baseweb="tab-list"] {
    gap: 1.5rem;
    border-bottom: 1px solid #edf2f7;
    padding-bottom: 1.5rem;
    margin-bottom: 2rem;
}
.stTabs [data-baseweb="tab"] {
    padding: 0.75rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #718096;
    border-radius: 0;
    border: none;
    position: relative;
}
.stTabs [aria-selected="true"] {
    color: #4338ca;
}
.stTabs [aria-selected="true"]::after {
    content: '';
    position: absolute;
    bottom: -1.5rem;
    left: 0;
    width: 100%;
    height: 3px;
    background: #4338ca;
    border-radius: 3px 3px 0 0;
}

/* Form elements */
.stTextInput > div > div > input {
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 0.9rem 1.2rem;
    font-size: 1.05rem;
    transition: all 0.3s ease;
}
.stTextInput > div > div > input:focus {
    border-color: #4338ca;
    box-shadow: 0 0 0 3px rgba(67, 56, 202, 0.15);
    background: white;
}

/* Labels */
label[data-baseweb="label"] {
    color: #4a5568 !important;
    font-weight: 600 !important;
    margin-bottom: 0.6rem !important;
    font-size: 0.95rem !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(to right, #4338ca, #3730a3);
    border: none;
    border-radius: 12px;
    padding: 0.85rem 1.5rem;
    font-weight: 600;
    font-size: 1.05rem;
    color: white;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px -3px rgba(67, 56, 202, 0.3);
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 20px -3px rgba(67, 56, 202, 0.4);
    background: linear-gradient(to right, #3730a3, #312e81);
}
.stButton > button:active {
    transform: translateY(0);
}

/* Secondary buttons */
.stButton:nth-last-of-type(1) > button {
    background: transparent !important;
    border: 2px solid #cbd5e1 !important;
    color: #4a5568 !important;
    font-weight: 600;
    box-shadow: none !important;
    margin-top: 1.2rem;
}
.stButton:nth-last-of-type(1) > button:hover {
    background: #f1f5f9 !important;
    border-color: #94a3b8 !important;
    color: #1e293b !important;
}

/* Forgot password link */
.forgot-link {
    text-align: center;
    margin-top: 1.5rem;
}
.forgot-link a {
    color: #4338ca;
    text-decoration: none;
    font-weight: 500;
    transition: all 0.2s;
    display: inline-block;
}
.forgot-link a:hover {
    text-decoration: underline;
    color: #3730a3;
    transform: translateX(2px);
}

/* Divider */
.divider {
    display: flex;
    align-items: center;
    text-align: center;
    margin: 1.8rem 0;
}
.divider::before,
.divider::after {
    content: '';
    flex: 1;
    border-bottom: 1px solid #e2e8f0;
}
.divider span {
    padding: 0 10px;
    color: #a0aec0;
    font-size: 0.9rem;
}

/* Social login buttons */
.social-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 0.8rem;
    font-weight: 500;
    color: #4a5568;
    transition: all 0.2s;
}
.social-btn:hover {
    background: #edf2f7;
    border-color: #cbd5e1;
}

/* Responsive design */
@media (max-width: 768px) {
    .auth-container {
        flex-direction: column;
        min-height: auto;
        border-radius: 0;
        box-shadow: none;
        background: transparent;
    }
    .auth-brand {
        border-radius: 0;
        padding: 2rem 1.5rem;
    }
    .auth-forms {
        padding: 2rem 1.5rem;
    }
}
              .game-card {
        background:#fff;
        border:1px solid #e6e6e6;
        border-radius:12px;
        padding:15px;
        margin-bottom:18px;
        box-shadow:0 2px 6px rgba(0,0,0,0.05);
    }
    .game-card img {
        border-radius:10px;
        width:100%;
        height:180px;
        object-fit:cover;
    }
       div.stButton > button {
    width:170px;
    height:48px;
    font-size:16px;
    font-weight:600;
    border-radius:14px;
    background:linear-gradient(135deg,#4facfe,#00f2fe);
    color:white;
    border:none;

    
</style>
""" 


#         X_train, X_test, y_train, y_test = train_test_split(
#             X, y, test_size=0.2, random_state=42
#         )

#         models = {
#              "Linear Regression": LinearRegression(),
#               "Polynomial Regression": Pipeline([
#              ("poly", PolynomialFeatures(degree=2)),
#              ("lr", LinearRegression())
#         ])
#         }

#         results = []

#         for name, m in models.items():
#          m.fit(X_train, y_train)
#         preds = m.predict(X_test)

#         mae = mean_absolute_error(y_test, preds)
#         rmse = np.sqrt(mean_squared_error(y_test, preds))

#         r2 = None
#         if len(y_test) > 1:
#          r2 = round(r2_score(y_test, preds), 2)

#         results.append({
#         "Model": name,
#         "MAE": round(mean_absolute_error(y_test, preds), 2),
#         "RMSE": round(np.sqrt(mean_squared_error(y_test, preds)), 2),
#         "R2": r2
#         })

#         st.subheader("📊 Model Evaluation & Comparison")
#         st.dataframe(results)
# # =========================
# # PERCENTAGE ERROR + DONUT GRAPH
# # =========================

#         actual_downloads = pd.to_numeric(g["downloads"], errors="coerce")

#         if actual_downloads is not None and not np.isnan(actual_downloads) and actual_downloads > 0:
#            percentage_error = round((mae / actual_downloads) * 100)
#            if percentage_error == 0:
#                percentage_error = 1  # 0.9 → 1 rule

#            st.subheader("📉 Error Analysis")

#            st.write(f"**MAE:** {format_number(mae)}")
#            st.write(
#               f"**Actual Downloads:** "
#             f"{format_downloads(actual_downloads, g['platform_type'])}"
#            )
#            st.write(f"**Percentage Error:** {percentage_error}%")

#            if percentage_error <= 5:
#               st.success("✅ Model accuracy is very good")
#            elif percentage_error <= 10:
#               st.warning("⚠️ Model accuracy is acceptable")
#            else:
#               st.error("❌ Model accuracy is poor")

#     else:
#       st.warning("⚠️ Invalid downloads data")